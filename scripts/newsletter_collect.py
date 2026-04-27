#!/usr/bin/env python3
"""Collect Nana newsletter emails and checkpoint them for split cron jobs.

This script is the collection stage only. It fetches unread IMAP messages,
extracts article links, saves raw article markdown under the wiki raw area,
saves newsletter digests under inbox/newsletters, and writes a checkpoint to
HERMES_HOME/cron/data/newsletter/latest.json for the triage job.

It intentionally does not create curated wiki pages and does not commit.
"""

from __future__ import annotations

import email
import email.policy
import hashlib
import imaplib
import json
import logging
import os
import re
import sys
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.parse import urlparse

IMPORT_ERRORS: list[str] = []

try:
    import httpx
except ImportError as exc:  # pragma: no cover - depends on runtime image
    httpx = None
    IMPORT_ERRORS.append(f"httpx: {exc}")

try:
    from bs4 import BeautifulSoup
except ImportError as exc:  # pragma: no cover - depends on runtime image
    BeautifulSoup = None
    IMPORT_ERRORS.append(f"bs4: {exc}")

try:
    from readability import Document
except ImportError as exc:  # pragma: no cover - depends on runtime image
    Document = None
    IMPORT_ERRORS.append(f"readability: {exc}")


HERMES_HOME = Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes"))
PROFILE_ROOT = HERMES_HOME.parent
AI_TOPICS_REPO = Path(os.environ.get("AI_TOPICS_REPO", str(PROFILE_ROOT / "ai-topics-cn")))
WIKI_ROOT = Path(os.environ.get("WIKI_ROOT", str(AI_TOPICS_REPO / "wiki")))
WIKI_RAW = WIKI_ROOT / "raw" / "articles"
INBOX_DIR = AI_TOPICS_REPO / "inbox" / "newsletters"
LOG_FILE = PROFILE_ROOT / "logs" / "newsletter_collect.log"
PROCESSED_DB = HERMES_HOME / "processed_emails.json"
CHECKPOINT_DIR = HERMES_HOME / "cron" / "data" / "newsletter"
LATEST_PATH = CHECKPOINT_DIR / "latest.json"

IMAP_HOST = os.environ.get("EMAIL_IMAP_HOST")
IMAP_PORT = int(os.environ.get("EMAIL_IMAP_PORT", "993"))
IMAP_USER = os.environ.get("EMAIL_ADDRESS")
IMAP_PASS = os.environ.get("EMAIL_PASSWORD")
IMAP_FOLDER = os.environ.get("EMAIL_FOLDER", "INBOX")
IMAP_PROCESSED = os.environ.get("EMAIL_PROCESSED_FOLDER", "Processed")
MAX_MESSAGES = int(os.environ.get("EMAIL_MAX_MESSAGES", "50"))
MAX_LINKS = int(os.environ.get("EMAIL_MAX_LINKS", "20"))
EXCERPT_CHARS = int(os.environ.get("NEWSLETTER_EXCERPT_CHARS", "200"))

HTTP_HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; HermesBot/1.0)",
    "Accept": "text/html,application/xhtml+xml",
}

LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stderr),
    ],
)
log = logging.getLogger(__name__)


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def run_id() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def load_processed() -> set[str]:
    if PROCESSED_DB.exists():
        data = json.loads(PROCESSED_DB.read_text(encoding="utf-8"))
        return set(data.get("message_ids", []))
    return set()


def save_processed(ids: set[str]) -> None:
    PROCESSED_DB.parent.mkdir(parents=True, exist_ok=True)
    PROCESSED_DB.write_text(
        json.dumps({"message_ids": sorted(ids)}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def clean_filename(value: str, fallback: str = "newsletter") -> str:
    safe = re.sub(r"[^a-zA-Z0-9\u4e00-\u9fff\-_ ]", "", value)
    safe = re.sub(r"\s+", "-", safe).strip("-")[:60]
    return safe or fallback


def display_path(path: Path) -> str:
    try:
        return "~/wiki/" + path.relative_to(WIKI_ROOT).as_posix()
    except ValueError:
        pass
    try:
        return "~/ai-topics-cn/" + path.relative_to(AI_TOPICS_REPO).as_posix()
    except ValueError:
        return str(path)


def yaml_quote(value: str) -> str:
    return json.dumps(value or "", ensure_ascii=False)


def extract_links_from_html(html: str) -> list[str]:
    if BeautifulSoup is None:
        log.warning("Cannot parse HTML email because bs4 is unavailable")
        return []
    soup = BeautifulSoup(html, "html.parser")
    links: list[str] = []
    for anchor in soup.find_all("a", href=True):
        href = anchor["href"].strip()
        if not href.startswith(("http://", "https://")):
            continue
        parsed = urlparse(href)
        domain = parsed.netloc.lower()
        path = parsed.path.lower()
        skip_domains = [
            "unsubscribe",
            "manage",
            "preferences",
            "tracking",
            "click.",
            "list-manage",
            "mailchimp",
            "beehiiv.com/unsubscribe",
        ]
        skip_paths = [
            "/unsubscribe",
            "/manage",
            "/preferences",
            "/privacy",
            "/terms",
            "/about",
            "/contact",
        ]
        if any(part in domain for part in skip_domains):
            continue
        if any(path.startswith(part) for part in skip_paths):
            continue
        links.append(href)
    return list(dict.fromkeys(links))


def extract_links_from_text(text: str) -> list[str]:
    urls = re.findall(r'https?://[^\s<>"\')]+', text)
    return list(dict.fromkeys(urls))


def scrape_url(url: str) -> dict | None:
    if httpx is None or BeautifulSoup is None or Document is None:
        log.warning("Cannot scrape %s because newsletter dependencies are unavailable", url)
        return None
    try:
        with httpx.Client(timeout=30, follow_redirects=True, headers=HTTP_HEADERS) as client:
            response = client.get(url)
            response.raise_for_status()
    except Exception as exc:
        log.warning("Failed to fetch %s: %s", url, exc)
        return None

    content_type = response.headers.get("content-type", "")
    if "text/html" not in content_type:
        log.info("Skipping non-HTML: %s (%s)", url, content_type)
        return None

    try:
        doc = Document(response.text)
        title = doc.short_title() or "Untitled"
        summary_html = doc.summary()
        soup = BeautifulSoup(summary_html, "html.parser")
        content = soup.get_text(separator="\n", strip=True)
    except Exception as exc:
        log.warning("Failed to parse %s: %s", url, exc)
        return None

    if len(content) < 100:
        log.info("Skipping short content (%s chars): %s", len(content), url)
        return None

    return {
        "url": url,
        "title": title,
        "content": content,
        "fetched_at": now_utc(),
    }


def url_to_filename(url: str) -> str:
    digest = hashlib.md5(url.encode("utf-8")).hexdigest()[:8]
    parsed = urlparse(url)
    domain = parsed.netloc.replace("www.", "")
    slug = re.sub(r"[^a-z0-9]+", "-", parsed.path.lower()).strip("-")[:60]
    return f"{domain}--{slug}--{digest}.md"


def save_article(article: dict, date_str: str) -> Path:
    WIKI_RAW.mkdir(parents=True, exist_ok=True)
    path = WIKI_RAW / url_to_filename(article["url"])
    frontmatter = (
        "---\n"
        f"title: {yaml_quote(article['title'])}\n"
        f"url: {yaml_quote(article['url'])}\n"
        f"fetched_at: {article['fetched_at']}\n"
        f"source_date: {date_str}\n"
        "tags: [newsletter, auto-ingested]\n"
        "source_lang: zh-CN\n"
        "---\n\n"
    )
    body = f"# {article['title']}\n\nSource: {article['url']}\n\n{article['content']}\n"
    path.write_text(frontmatter + body, encoding="utf-8")
    log.info("Saved raw article: %s", display_path(path))
    return path


def save_digest(
    articles: list[dict],
    links: list[str],
    email_subject: str,
    from_addr: str,
    message_id: str,
    date_str: str,
) -> Path:
    INBOX_DIR.mkdir(parents=True, exist_ok=True)
    safe_subject = clean_filename(email_subject)
    digest = hashlib.sha1((message_id or email_subject).encode("utf-8")).hexdigest()[:8]
    path = INBOX_DIR / f"{date_str}--{safe_subject}--{digest}.md"

    lines = [
        "---\n",
        f"title: {yaml_quote(email_subject)}\n",
        f"from: {yaml_quote(from_addr)}\n",
        f"message_id: {yaml_quote(message_id)}\n",
        f"date: {date_str}\n",
        "type: newsletter-digest\n",
        f"processed: {now_utc()}\n",
        f"links_found: {len(links)}\n",
        f"articles_scraped: {len(articles)}\n",
        "tags: [newsletter, auto-ingested]\n",
        "---\n\n",
        f"# {email_subject}\n\n",
        f"**From:** {from_addr}\n",
        f"**Date:** {date_str}\n",
        f"**Links found:** {len(links)}\n",
        f"**Articles scraped:** {len(articles)}\n\n",
        "---\n\n",
    ]
    for index, article in enumerate(articles, start=1):
        lines.append(f"## {index}. {article['title']}\n\n")
        lines.append(f"- **URL:** {article['url']}\n")
        lines.append(f"- **Raw:** {article['raw_path']}\n")
        lines.append(f"- **Length:** {article['length']} chars\n\n")
        preview = article.get("excerpt", "").replace("\n", "\n> ")
        if preview:
            lines.append(f"> {preview}\n\n")

    if not articles and links:
        lines.append("## Links\n\n")
        for link in links[:MAX_LINKS]:
            lines.append(f"- {link}\n")

    path.write_text("".join(lines), encoding="utf-8")
    log.info("Saved digest: %s", display_path(path))
    return path


def extract_message_body(msg) -> tuple[str | None, str | None]:
    html_body = None
    text_body = None
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            if content_type == "text/html" and not html_body:
                html_body = part.get_content()
            elif content_type == "text/plain" and not text_body:
                text_body = part.get_content()
    else:
        content_type = msg.get_content_type()
        if content_type == "text/html":
            html_body = msg.get_content()
        elif content_type == "text/plain":
            text_body = msg.get_content()
    return html_body, text_body


def message_date(msg) -> str:
    try:
        parsed = parsedate_to_datetime(msg.get("Date", ""))
        return parsed.strftime("%Y-%m-%d")
    except Exception:
        return datetime.now().strftime("%Y-%m-%d")


def process_email_message(msg, source_label: str) -> dict:
    msg_id = msg.get("Message-ID") or source_label
    subject = msg.get("Subject", "(no subject)")
    from_addr = msg.get("From", "")
    date_str = message_date(msg)

    log.info("Processing %s: %s", source_label, subject)
    html_body, text_body = extract_message_body(msg)
    links = extract_links_from_html(html_body) if html_body else extract_links_from_text(text_body or "")
    log.info("Found %d links", len(links))

    articles: list[dict] = []
    for url in links[:MAX_LINKS]:
        scraped = scrape_url(url)
        if not scraped:
            continue
        raw_path = save_article(scraped, date_str)
        content = scraped.get("content", "")
        articles.append({
            "title": scraped.get("title", ""),
            "url": scraped.get("url", ""),
            "raw_path": display_path(raw_path),
            "length": len(content),
            "excerpt": content[:EXCERPT_CHARS],
            "fetched_at": scraped.get("fetched_at"),
        })

    digest_path = save_digest(articles, links, subject, from_addr, msg_id, date_str)
    return {
        "ok": True,
        "message_id": msg_id,
        "source_label": source_label,
        "subject": subject,
        "from": from_addr,
        "date": date_str,
        "links_found": len(links),
        "articles_scraped": len(articles),
        "digest_path": display_path(digest_path),
        "articles": articles,
    }


def missing_env() -> list[str]:
    required = {
        "EMAIL_IMAP_HOST": IMAP_HOST,
        "EMAIL_ADDRESS": IMAP_USER,
        "EMAIL_PASSWORD": IMAP_PASS,
    }
    return [key for key, value in required.items() if not value]


def runtime_errors() -> list[str]:
    errors = [f"Missing required env vars: {', '.join(missing_env())}"] if missing_env() else []
    if IMPORT_ERRORS:
        errors.append("Missing Python dependencies: " + "; ".join(IMPORT_ERRORS))
    return errors


def ensure_folder_exists(mailbox: imaplib.IMAP4_SSL, folder: str) -> None:
    typ, _ = mailbox.create(folder)
    if typ not in ("OK", "NO"):
        log.warning("Unexpected response creating folder %r: %s", folder, typ)


def make_empty_summary(ok: bool, run: str, error: str | None = None) -> dict:
    summary = {
        "ok": ok,
        "run_id": run,
        "collected_at": now_utc(),
        "processed_count": 0,
        "skipped_count": 0,
        "processed_messages": [],
        "skipped_messages": [],
        "errors": [],
        "checkpoint_path": str(LATEST_PATH),
    }
    if error:
        summary["errors"].append(error)
    return summary


def process_all_unseen(run: str) -> dict:
    errors = runtime_errors()
    if errors:
        summary = make_empty_summary(False, run)
        summary["errors"].extend(errors)
        return summary

    processed_ids = load_processed()
    new_processed: set[str] = set()
    processed_messages: list[dict] = []
    skipped_messages: list[dict] = []
    errors: list[dict] = []

    log.info("Connecting to %s:%s as %s", IMAP_HOST, IMAP_PORT, IMAP_USER)
    with imaplib.IMAP4_SSL(IMAP_HOST, IMAP_PORT) as mailbox:
        mailbox.login(IMAP_USER, IMAP_PASS)
        ensure_folder_exists(mailbox, IMAP_PROCESSED)

        typ, _ = mailbox.select(IMAP_FOLDER)
        if typ != "OK":
            return make_empty_summary(False, run, f"Cannot select folder {IMAP_FOLDER!r}")

        typ, data = mailbox.uid("SEARCH", "UNSEEN")
        if typ != "OK":
            return make_empty_summary(False, run, "UNSEEN search failed")

        uids = data[0].split()[:MAX_MESSAGES]
        log.info("Found %d unseen message(s); cap=%d", len(uids), MAX_MESSAGES)

        for uid in uids:
            uid_text = uid.decode()
            try:
                typ, msg_data = mailbox.uid("FETCH", uid, "(RFC822)")
                if typ != "OK" or not msg_data or not msg_data[0]:
                    errors.append({"uid": uid_text, "error": "fetch failed"})
                    continue

                raw = msg_data[0][1]
                msg = email.message_from_bytes(raw, policy=email.policy.default)
                msg_id = msg.get("Message-ID") or f"uid-{uid_text}"

                if msg_id in processed_ids:
                    skipped_messages.append({"uid": uid_text, "message_id": msg_id, "reason": "already_processed"})
                    mailbox.uid("COPY", uid, IMAP_PROCESSED)
                    mailbox.uid("STORE", uid, "+FLAGS", r"(\Seen \Deleted)")
                    continue

                result = process_email_message(msg, source_label=f"uid={uid_text}")
                processed_messages.append(result)
                new_processed.add(msg_id)

                typ, _ = mailbox.uid("COPY", uid, IMAP_PROCESSED)
                if typ != "OK":
                    errors.append({"uid": uid_text, "error": f"COPY to {IMAP_PROCESSED!r} failed: {typ}"})
                typ, _ = mailbox.uid("STORE", uid, "+FLAGS", r"(\Seen \Deleted)")
                if typ != "OK":
                    errors.append({"uid": uid_text, "error": f"STORE Deleted failed: {typ}"})
            except Exception as exc:
                log.error("Error processing uid=%s: %s", uid_text, exc, exc_info=True)
                errors.append({"uid": uid_text, "error": str(exc)})

        mailbox.expunge()

    if new_processed:
        processed_ids.update(new_processed)
        save_processed(processed_ids)

    return {
        "ok": True,
        "run_id": run,
        "collected_at": now_utc(),
        "processed_count": len(processed_messages),
        "skipped_count": len(skipped_messages),
        "processed_messages": processed_messages,
        "skipped_messages": skipped_messages,
        "errors": errors,
        "checkpoint_path": str(LATEST_PATH),
    }


def write_checkpoint(summary: dict) -> dict:
    CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)
    run = summary.get("run_id") or run_id()
    archive_path = CHECKPOINT_DIR / f"newsletter_collect_{run}.json"
    summary["archive_path"] = str(archive_path)
    payload = json.dumps(summary, ensure_ascii=False, indent=2)
    LATEST_PATH.write_text(payload, encoding="utf-8")
    archive_path.write_text(payload, encoding="utf-8")
    return summary


def main() -> int:
    run = run_id()
    try:
        summary = process_all_unseen(run)
    except imaplib.IMAP4.error as exc:
        log.error("IMAP error: %s", exc)
        summary = make_empty_summary(False, run, f"IMAP error: {exc}")
    except Exception as exc:
        log.error("Unexpected error: %s", exc, exc_info=True)
        summary = make_empty_summary(False, run, f"Unexpected error: {exc}")

    summary = write_checkpoint(summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
