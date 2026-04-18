#!/usr/bin/env python3
"""Process incoming newsletter emails for ai-topics-cn.

Reads emails from ~/Maildir/new/, extracts links, scrapes content,
saves raw articles to inbox/newsletters/ for later wiki triage.

Adapted from ai-topics/scripts/process_email.py for the Chinese AI wiki.
"""
import email
import email.policy
import os
import re
import sys
import json
import hashlib
import subprocess
import logging
from pathlib import Path
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from urllib.parse import urlparse

import httpx
from bs4 import BeautifulSoup
from readability import Document

# Config
MAILDIR_NEW = Path.home() / "Maildir" / "new"
MAILDIR_CUR = Path.home() / "Maildir" / "cur"
MAILDIR_PROCESSED = Path.home() / "Maildir" / "processed"
REPO_DIR = Path.home() / "ai-topics-cn"
INBOX_DIR = REPO_DIR / "inbox" / "newsletters"
WIKI_RAW = REPO_DIR / "wiki" / "raw" / "articles"
LOG_FILE = Path.home() / "logs" / "newsletter_processor.log"
PROCESSED_DB = Path.home() / ".hermes" / "processed_emails.json"

# Setup logging
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger(__name__)

HTTP_HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; HermesBot/1.0; +https://hermes-china-digest.exe.xyz)",
    "Accept": "text/html,application/xhtml+xml",
}


def load_processed() -> set:
    """Load set of already-processed message IDs."""
    if PROCESSED_DB.exists():
        data = json.loads(PROCESSED_DB.read_text())
        return set(data.get("message_ids", []))
    return set()


def save_processed(ids: set):
    """Save processed message IDs."""
    PROCESSED_DB.parent.mkdir(parents=True, exist_ok=True)
    PROCESSED_DB.write_text(json.dumps({"message_ids": list(ids)}, indent=2))


def extract_links_from_html(html: str) -> list[str]:
    """Extract HTTP(S) links from HTML email body."""
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if href.startswith(("http://", "https://")):
            parsed = urlparse(href)
            skip_domains = [
                "unsubscribe", "manage", "preferences", "tracking",
                "click.", "list-manage", "mailchimp", "beehiiv.com/unsubscribe",
            ]
            skip_paths = [
                "/unsubscribe", "/manage", "/preferences", "/privacy",
                "/terms", "/about", "/contact",
            ]
            domain = parsed.netloc.lower()
            path = parsed.path.lower()
            if any(s in domain for s in skip_domains):
                continue
            if any(path.startswith(s) for s in skip_paths):
                continue
            links.append(href)
    seen = set()
    unique = []
    for link in links:
        if link not in seen:
            seen.add(link)
            unique.append(link)
    return unique


def extract_links_from_text(text: str) -> list[str]:
    """Extract URLs from plain text."""
    urls = re.findall(r'https?://[^\s<>"\')]+', text)
    return list(dict.fromkeys(urls))


def scrape_url(url: str) -> dict | None:
    """Scrape a URL and extract readable content."""
    try:
        with httpx.Client(timeout=30, follow_redirects=True, headers=HTTP_HEADERS) as client:
            resp = client.get(url)
            resp.raise_for_status()
    except Exception as e:
        log.warning(f"Failed to fetch {url}: {e}")
        return None

    content_type = resp.headers.get("content-type", "")
    if "text/html" not in content_type:
        log.info(f"Skipping non-HTML: {url} ({content_type})")
        return None

    try:
        doc = Document(resp.text)
        title = doc.short_title() or "Untitled"
        summary_html = doc.summary()
        soup = BeautifulSoup(summary_html, "html.parser")
        content = soup.get_text(separator="\n", strip=True)
    except Exception as e:
        log.warning(f"Failed to parse {url}: {e}")
        return None

    if len(content) < 100:
        log.info(f"Skipping short content ({len(content)} chars): {url}")
        return None

    return {
        "url": url,
        "title": title,
        "content": content,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
    }


def url_to_filename(url: str) -> str:
    """Generate a filesystem-safe filename from URL."""
    h = hashlib.md5(url.encode()).hexdigest()[:8]
    parsed = urlparse(url)
    domain = parsed.netloc.replace("www.", "")
    slug = re.sub(r"[^a-z0-9]+", "-", parsed.path.lower()).strip("-")[:60]
    return f"{domain}--{slug}--{h}"


def save_article(article: dict, date_str: str) -> Path:
    """Save article as markdown in wiki/raw/articles/."""
    WIKI_RAW.mkdir(parents=True, exist_ok=True)
    fname = url_to_filename(article["url"])
    filepath = WIKI_RAW / f"{fname}.md"

    frontmatter = (
        f"---\n"
        f"title: \"{article['title']}\"\n"
        f"url: \"{article['url']}\"\n"
        f"fetched_at: {article['fetched_at']}\n"
        f"source_date: {date_str}\n"
        f"tags: [newsletter, auto-ingested]\n"
        f"source_lang: zh-CN\n"
        f"---\n\n"
    )
    body = f"# {article['title']}\n\nSource: {article['url']}\n\n{article['content']}\n"
    filepath.write_text(frontmatter + body, encoding="utf-8")
    log.info(f"Saved raw article: {filepath.name}")
    return filepath


def save_eml_copy(filepath: Path, date_str: str, subject: str) -> Path:
    """Save a copy of the .eml file to inbox/newsletters/."""
    INBOX_DIR.mkdir(parents=True, exist_ok=True)
    safe_subj = re.sub(r'[^a-zA-Z0-9\u4e00-\u9fff\-_ ]', '', subject)[:60].strip()
    dest = INBOX_DIR / f"{date_str}--{safe_subj or 'newsletter'}.eml"
    # Avoid overwrite
    if dest.exists():
        h = hashlib.md5(filepath.name.encode()).hexdigest()[:6]
        dest = INBOX_DIR / f"{date_str}--{safe_subj or 'newsletter'}--{h}.eml"
    import shutil
    shutil.copy2(filepath, dest)
    log.info(f"Saved .eml copy: {dest.name}")
    return dest


def save_digest(articles: list[dict], email_subject: str, from_addr: str, date_str: str):
    """Save newsletter digest summary to inbox/newsletters/."""
    INBOX_DIR.mkdir(parents=True, exist_ok=True)
    safe_subj = re.sub(r'[^a-zA-Z0-9\u4e00-\u9fff\-_ ]', '', email_subject)[:50].strip()
    fname = f"{date_str}--{safe_subj or 'newsletter'}.md"
    filepath = INBOX_DIR / fname

    if filepath.exists():
        h = hashlib.md5(email_subject.encode()).hexdigest()[:6]
        fname = f"{date_str}--{safe_subj or 'newsletter'}--{h}.md"
        filepath = INBOX_DIR / fname

    lines = [
        f"---\n",
        f"title: \"{email_subject}\"\n",
        f"from: \"{from_addr}\"\n",
        f"date: {date_str}\n",
        f"type: newsletter-digest\n",
        f"processed: {datetime.now(timezone.utc).isoformat()}\n",
        f"articles_scraped: {len(articles)}\n",
        f"tags: [newsletter, auto-ingested]\n",
        f"---\n\n",
        f"# {email_subject}\n\n",
        f"**From:** {from_addr}\n",
        f"**Date:** {date_str}\n",
        f"**Articles scraped:** {len(articles)}\n\n",
        f"---\n\n",
    ]
    for i, art in enumerate(articles, 1):
        lines.append(f"## {i}. {art['title']}\n\n")
        lines.append(f"- **URL:** {art['url']}\n")
        lines.append(f"- **Length:** {len(art['content'])} chars\n\n")
        preview = art["content"][:500].replace("\n", "\n> ")
        lines.append(f"> {preview}\n\n")

    filepath.write_text("".join(lines), encoding="utf-8")
    log.info(f"Saved digest: {filepath}")


def git_commit_if_changed():
    """Git add and commit if there are changes."""
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain", "inbox/newsletters/", "wiki/raw/articles/"],
            cwd=REPO_DIR, capture_output=True, text=True,
        )
        if not result.stdout.strip():
            log.info("No changes to commit")
            return

        subprocess.run(
            ["git", "add", "inbox/newsletters/", "wiki/raw/articles/"],
            cwd=REPO_DIR, check=True, capture_output=True,
        )
        date_str = datetime.now().strftime("%Y-%m-%d")
        subprocess.run(
            ["git", "commit", "-m", f"inbox: newsletter digest {date_str}"],
            cwd=REPO_DIR, check=True, capture_output=True,
        )
        subprocess.run(
            ["git", "push"],
            cwd=REPO_DIR, check=True, capture_output=True,
        )
        log.info("Git commit & push done")
    except subprocess.CalledProcessError as e:
        log.warning(f"Git operation failed: {e.stderr.decode() if e.stderr else e}")


def process_email_file(filepath: Path) -> bool:
    """Process a single email file. Returns True if processed."""
    log.info(f"Processing: {filepath.name}")

    raw = filepath.read_bytes()
    msg = email.message_from_bytes(raw, policy=email.policy.default)

    subject = msg.get("Subject", "(no subject)")
    from_addr = msg.get("From", "")
    delivered_to = msg.get("Delivered-To", "")

    log.info(f"  From: {from_addr}")
    log.info(f"  Subject: {subject}")
    log.info(f"  Delivered-To: {delivered_to}")

    # Get date
    try:
        date = parsedate_to_datetime(msg.get("Date", ""))
        date_str = date.strftime("%Y-%m-%d")
    except Exception:
        date_str = datetime.now().strftime("%Y-%m-%d")

    # Save .eml copy
    save_eml_copy(filepath, date_str, subject)

    # Extract body
    html_body = None
    text_body = None

    if msg.is_multipart():
        for part in msg.walk():
            ct = part.get_content_type()
            if ct == "text/html" and not html_body:
                html_body = part.get_content()
            elif ct == "text/plain" and not text_body:
                text_body = part.get_content()
    else:
        ct = msg.get_content_type()
        if ct == "text/html":
            html_body = msg.get_content()
        elif ct == "text/plain":
            text_body = msg.get_content()

    # Extract links
    links = []
    if html_body:
        links = extract_links_from_html(html_body)
    elif text_body:
        links = extract_links_from_text(text_body)

    log.info(f"  Found {len(links)} links")

    # Scrape top links (limit to avoid overload)
    MAX_LINKS = 20
    articles = []
    for url in links[:MAX_LINKS]:
        article = scrape_url(url)
        if article:
            save_article(article, date_str)
            articles.append(article)

    log.info(f"  Scraped {len(articles)} articles")

    # Save digest summary
    save_digest(articles, subject, from_addr, date_str)

    return True


def process_all_new():
    """Process all emails in Maildir/new/ and Maildir/cur/."""
    for d in [MAILDIR_NEW, MAILDIR_CUR, MAILDIR_PROCESSED]:
        d.mkdir(parents=True, exist_ok=True)

    processed_ids = load_processed()
    new_processed = set()

    all_files = []
    for d in [MAILDIR_NEW, MAILDIR_CUR]:
        if d.exists():
            all_files.extend(sorted(d.iterdir()))

    if not all_files:
        log.info("No new emails")
        return

    log.info(f"Found {len(all_files)} email(s) to check")

    for filepath in all_files:
        if not filepath.is_file():
            continue

        msg_id = filepath.name
        if msg_id in processed_ids:
            # Already processed, move to processed/
            try:
                filepath.rename(MAILDIR_PROCESSED / filepath.name)
            except Exception:
                pass
            continue

        try:
            if process_email_file(filepath):
                new_processed.add(msg_id)
                try:
                    filepath.rename(MAILDIR_PROCESSED / filepath.name)
                except Exception as e:
                    log.warning(f"Failed to move {filepath.name}: {e}")
                continue
        except Exception as e:
            log.error(f"Error processing {filepath.name}: {e}", exc_info=True)

        # Failed → move to cur/
        try:
            if filepath.parent != MAILDIR_CUR:
                filepath.rename(MAILDIR_CUR / filepath.name)
        except Exception as e:
            log.warning(f"Failed to move {filepath.name} to cur/: {e}")

    if new_processed:
        processed_ids.update(new_processed)
        save_processed(processed_ids)
        log.info(f"Processed {len(new_processed)} new email(s)")

    # Git commit all changes
    git_commit_if_changed()


if __name__ == "__main__":
    process_all_new()
