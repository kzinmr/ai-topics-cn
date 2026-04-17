#!/usr/bin/env python3
"""Build wiki entity skeleton pages for X/Twitter accounts (Chinese AI space).

For each account in x-accounts.yaml:
1. If blog URL provided: fetch about page + discover/fetch RSS
2. Generate a wiki entity skeleton page with known info
3. The skeleton is designed to be enriched by an agent or human researcher

Entity pages are written in Japanese with source_lang: zh-CN frontmatter,
matching the convention of the Chinese AI Topics wiki (source material in
Chinese, wiki prose in Japanese).

Usage:
  python3 build_x_wiki.py                    # Process all
  python3 build_x_wiki.py --dry-run           # Preview without writing
  python3 build_x_wiki.py --handle @karminski3  # Process single account
  python3 build_x_wiki.py --enrich            # Print enrichment prompt
"""

import argparse
import json
import logging
import re
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse

try:
    import yaml
except ImportError:
    sys.exit("ERROR: PyYAML is required. Install with: pip install pyyaml")

try:
    import httpx
except ImportError:
    httpx = None  # type: ignore[assignment]

try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None  # type: ignore[assignment,misc]

try:
    from readability import Document as ReadabilityDocument
except ImportError:
    ReadabilityDocument = None  # type: ignore[assignment,misc]

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

ACCOUNTS_PATH = Path.home() / "ai-topics-cn" / "config" / "feeds" / "x-accounts.yaml"
WIKI_ENTITIES = Path.home() / "ai-topics-cn" / "wiki" / "entities"
WIKI_INDEX = Path.home() / "ai-topics-cn" / "wiki" / "index.md"
WIKI_LOG = Path.home() / "ai-topics-cn" / "wiki" / "log.md"
OUTPUT_JSON = Path(__file__).resolve().parent / "cache" / "x_accounts.json"

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------

HTTP_HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; AITopicsCNBot/1.0)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


def _check_http_deps() -> bool:
    """Return True if HTTP dependencies are available."""
    if httpx is None:
        log.warning("httpx not installed — blog fetching disabled (pip install httpx)")
        return False
    if BeautifulSoup is None:
        log.warning(
            "beautifulsoup4 not installed — HTML parsing disabled "
            "(pip install beautifulsoup4)"
        )
        return False
    return True


def fetch_page(url: str, timeout: int = 20) -> str | None:
    """Fetch a URL, return text or None."""
    if httpx is None:
        return None
    try:
        with httpx.Client(
            timeout=timeout, follow_redirects=True, headers=HTTP_HEADERS
        ) as c:
            r = c.get(url)
            r.raise_for_status()
            return r.text
    except Exception as e:
        log.warning("  Fetch failed %s: %s", url, e)
        return None


def discover_rss(blog_url: str, html: str | None = None) -> str | None:
    """Try to discover an RSS/Atom feed URL from a blog."""
    if not blog_url or BeautifulSoup is None:
        return None

    if html is None:
        html = fetch_page(blog_url)
    if not html:
        return None

    soup = BeautifulSoup(html, "html.parser")

    # Look for <link rel="alternate" type="...rss/atom..."> tags
    for link in soup.find_all("link", rel="alternate"):
        link_type = link.get("type", "")
        if "rss" in link_type or "atom" in link_type or "xml" in link_type:
            href = link.get("href", "")
            if href:
                return urljoin(blog_url, href)

    # Probe common feed paths
    parsed = urlparse(blog_url)
    base = f"{parsed.scheme}://{parsed.netloc}"
    common_paths = ["/feed", "/rss", "/atom.xml", "/feed.xml", "/rss.xml", "/index.xml"]
    for path in common_paths:
        url = base + path
        try:
            with httpx.Client(
                timeout=10, follow_redirects=True, headers=HTTP_HEADERS
            ) as c:
                r = c.head(url)
                ct = r.headers.get("content-type", "")
                if r.status_code == 200 and (
                    "xml" in ct or "rss" in ct or "atom" in ct
                ):
                    return url
        except Exception:
            continue

    return None


def extract_about_info(blog_url: str) -> dict:
    """Fetch blog and about page, extract author info."""
    info: dict = {"bio": "", "about_url": "", "meta_author": ""}
    if not blog_url or BeautifulSoup is None:
        return info

    parsed = urlparse(blog_url)
    base = f"{parsed.scheme}://{parsed.netloc}"
    about_paths = ["/about", "/about/", "/about-me", "/about.html", ""]

    for path in about_paths:
        url = base + path if path else blog_url
        html = fetch_page(url)
        if not html:
            continue

        soup = BeautifulSoup(html, "html.parser")

        # Extract meta tags
        for meta in soup.find_all("meta"):
            name_attr = meta.get("name", "").lower()
            prop_attr = meta.get("property", "").lower()
            content = meta.get("content", "").strip()
            if content and name_attr in ("author", "twitter:creator"):
                info["meta_author"] = content
            if content and prop_attr in ("og:site_name", "article:author"):
                if not info["meta_author"]:
                    info["meta_author"] = content

        # Extract about page content
        if path and ReadabilityDocument is not None:
            try:
                doc = ReadabilityDocument(html)
                about_soup = BeautifulSoup(doc.summary(), "html.parser")
                text = about_soup.get_text(separator="\n", strip=True)
                if len(text) > 50:
                    info["bio"] = text[:2000]
                    info["about_url"] = url
                    break
            except Exception:
                pass

    return info


def extract_feed_topics(rss_url: str) -> list[str]:
    """Fetch RSS/Atom feed and return recent post titles."""
    if not rss_url:
        return []
    xml_text = fetch_page(rss_url)
    if not xml_text:
        return []

    titles: list[str] = []
    try:
        # Strip default namespace to simplify parsing
        xml_clean = re.sub(r'\sxmlns[^"]*"[^"]*"', "", xml_text)
        root = ET.fromstring(xml_clean)

        # RSS 2.0
        for item in root.iter("item"):
            t = item.findtext("title", "").strip()
            if t:
                titles.append(t)

        # Atom
        if not titles:
            for entry in root.iter("entry"):
                t_el = entry.find("title")
                if t_el is not None and t_el.text:
                    titles.append(t_el.text.strip())
    except ET.ParseError as e:
        log.warning("  Feed parse error %s: %s", rss_url, e)

    return titles[:20]


# ---------------------------------------------------------------------------
# Slug / skeleton generation
# ---------------------------------------------------------------------------


def slugify(text: str) -> str:
    """Convert text to a URL/filename-safe slug."""
    s = text.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")[:80]


def generate_skeleton(
    account: dict, about: dict, rss_url: str, topics: list[str]
) -> str:
    """Generate a wiki entity skeleton page in Japanese with zh-CN source_lang."""
    name = account.get("name", "") or account["handle"].lstrip("@")
    handle = account["handle"].lstrip("@")
    blog_url = account.get("blog", "")
    github = account.get("github", "")
    today = datetime.now().strftime("%Y-%m-%d")
    notes = account.get("notes", "")

    # Build tag list: always include person + x-account + china-ai ecosystem tags
    tag_list = ["person", "x-account", "china-ai"]
    for t in account.get("topics", []):
        if t not in tag_list:
            tag_list.append(t)

    aliases = [f"@{handle}"]
    if name != handle:
        aliases.append(handle)

    # --- Build the page ---
    tags_str = ", ".join(tag_list)
    aliases_json = json.dumps(aliases, ensure_ascii=False)

    page = f"""---
title: "{name} \u2014 TODO: Short description"
created: {today}
updated: {today}
tags: [{tags_str}]
aliases: {aliases_json}
source_lang: zh-CN
status: skeleton
x_handle: "@{handle}"
---

# {name}

> **X/Twitter**: [@{handle}](https://x.com/{handle})
"""

    if blog_url:
        page += f"> **Blog**: [{blog_url}]({blog_url})\n"
    if rss_url:
        page += f"> **RSS**: [{rss_url}]({rss_url})\n"
    if about.get("about_url"):
        page += f"> **About**: [{about['about_url']}]({about['about_url']})\n"
    if github:
        page += f"> **GitHub**: [{github}](https://github.com/{github})\n"

    if notes:
        page += f"\n> **Notes**: {notes}\n"

    page += "\n## Overview\n\n"
    page += "TODO: Research and fill in background, expertise, and notable contributions.\n"

    if about.get("bio"):
        page += f"\n### Bio (scraped from about page)\n\n{about['bio'][:1500]}\n"

    page += "\n## Core Ideas\n\n"
    page += "TODO: Identify key themes and positions from their X posts and blog.\n"

    if topics:
        topic_list = "\n".join(f"- {t}" for t in topics[:15])
        page += f"\n### Recent Posts\n\n{topic_list}\n"

    page += "\n## Notable Works\n\n"
    page += "TODO: List key projects, papers, talks, or articles.\n"

    page += "\n## Related\n\n"
    page += "- [[related-page]]\n"

    return page


def generate_enrich_prompt(written: list[dict]) -> str:
    """Generate a prompt to request enrichment of skeleton pages."""
    if not written:
        return ""

    names = "\n".join(
        f"- `wiki/entities/{w['file']}` ({w['name']}, @{w['handle']})"
        for w in written
    )

    return f"""以下の新しいエンティティページのスケルトンを追加しました。
それぞれリサーチして充実させてください。

{names}

各ページについて：
1. X/Twitterでの活動内容・影響力を調査
2. ブログがあれば最近の記事内容を分析
3. 所属組織・プロジェクト・主要な貢献を特定
4. Core Ideas セクションにその人物の思想・主張をまとめる
5. Related セクションに関連エンティティ/コンセプトへのwikilinkを追加
6. frontmatterの status: skeleton を削除
7. title の "TODO: Short description" を実際の説明に置き換え
8. 完了したらコミット＆プッシュ

1ページずつ順番に処理してください。"""


# ---------------------------------------------------------------------------
# Account loading
# ---------------------------------------------------------------------------


def load_accounts(path: Path, handle_filter: str | None = None) -> list[dict]:
    """Load accounts from the YAML config file."""
    if not path.exists():
        log.error("Accounts file not found: %s", path)
        return []
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    accounts = data.get("accounts", [])
    if handle_filter:
        handle_filter = handle_filter.lstrip("@").lower()
        accounts = [
            a
            for a in accounts
            if a["handle"].lstrip("@").lower() == handle_filter
        ]
    return accounts


# ---------------------------------------------------------------------------
# Processing
# ---------------------------------------------------------------------------


def process_account(account: dict, can_fetch: bool) -> dict:
    """Process a single X account: fetch blog info and RSS if possible."""
    handle = account["handle"].lstrip("@")
    name = account.get("name", handle)
    blog_url = account.get("blog", "")
    rss_url = account.get("rss", "")

    log.info("Processing: @%s (%s)", handle, name)

    about: dict = {"bio": "", "about_url": "", "meta_author": ""}
    topics: list[str] = []

    if can_fetch and blog_url:
        log.info("  Fetching blog: %s", blog_url)
        about = extract_about_info(blog_url)

        if not rss_url:
            log.info("  Discovering RSS...")
            rss_url = discover_rss(blog_url) or ""
            if rss_url:
                log.info("  Found RSS: %s", rss_url)

    if can_fetch and rss_url:
        log.info("  Fetching feed: %s", rss_url)
        topics = extract_feed_topics(rss_url)
        log.info("  Got %d post titles", len(topics))

    if can_fetch:
        time.sleep(0.5)  # politeness delay

    return {
        "account": account,
        "about": about,
        "rss_url": rss_url,
        "topics": topics,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build wiki entity skeletons for X accounts (Chinese AI space)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview without writing files",
    )
    parser.add_argument(
        "--handle",
        type=str,
        help="Process single handle (e.g. @karminski3)",
    )
    parser.add_argument(
        "--enrich",
        action="store_true",
        help="Print enrichment prompt for written skeletons",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing entity pages",
    )
    args = parser.parse_args()

    accounts = load_accounts(ACCOUNTS_PATH, args.handle)
    log.info("Loaded %d accounts from %s", len(accounts), ACCOUNTS_PATH)

    if not accounts:
        log.error("No accounts found")
        sys.exit(1)

    can_fetch = _check_http_deps()
    WIKI_ENTITIES.mkdir(parents=True, exist_ok=True)

    results: list[dict] = []
    written: list[dict] = []

    for account in accounts:
        handle = account["handle"].lstrip("@")
        name = account.get("name", handle)
        slug = slugify(name)
        filepath = WIKI_ENTITIES / f"{slug}.md"

        # Skip existing unless --force
        if filepath.exists() and not args.force:
            log.info("  Skipping %s.md (exists, use --force to overwrite)", slug)
            continue

        result = process_account(account, can_fetch)
        results.append(result)

        page = generate_skeleton(
            account, result["about"], result["rss_url"], result["topics"]
        )

        if args.dry_run:
            log.info("  [DRY RUN] Would write: %s", filepath.name)
            print(f"\n{'=' * 60}\n{filepath.name}\n{'=' * 60}")
            print(page[:500] + "..." if len(page) > 500 else page)
        else:
            filepath.write_text(page, encoding="utf-8")
            log.info("  Wrote: %s", filepath.name)
            written.append(
                {"name": name, "handle": handle, "slug": slug, "file": filepath.name}
            )

    # Save raw results to JSON cache
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)

    existing_cache: list = []
    if OUTPUT_JSON.exists():
        try:
            existing_cache = json.loads(OUTPUT_JSON.read_text(encoding="utf-8"))
        except Exception:
            pass
    existing_cache.extend(results)
    OUTPUT_JSON.write_text(
        json.dumps(existing_cache, indent=2, default=str, ensure_ascii=False),
        encoding="utf-8",
    )
    log.info("Saved raw data to %s", OUTPUT_JSON)

    if not args.dry_run and written:
        # --- Update wiki/index.md ---
        entity_lines = "\n".join(
            f"- [[entities/{w['slug']}|{w['name']}]] (@{w['handle']})"
            for w in sorted(written, key=lambda x: x["name"].lower())
        )
        try:
            index = WIKI_INDEX.read_text(encoding="utf-8")
            marker = "### X/Twitter Accounts"
            if marker in index:
                idx = index.index(marker) + len(marker)
                next_heading = index.find("\n### ", idx)
                if next_heading == -1:
                    next_heading = index.find("\n## ", idx)
                if next_heading == -1:
                    next_heading = len(index)
                existing_section = index[idx:next_heading]
                index = (
                    index[:idx]
                    + existing_section.rstrip()
                    + "\n"
                    + entity_lines
                    + "\n"
                    + index[next_heading:]
                )
            else:
                # Append new section at end of Entity Pages or at end
                entity_marker = "## Entity Pages"
                if entity_marker in index:
                    # Find next ## after Entity Pages
                    eidx = index.index(entity_marker) + len(entity_marker)
                    next_h2 = index.find("\n## ", eidx)
                    if next_h2 == -1:
                        next_h2 = len(index)
                    index = (
                        index[:next_h2]
                        + f"\n\n{marker}\n{entity_lines}\n"
                        + index[next_h2:]
                    )
                else:
                    index += f"\n\n{marker}\n{entity_lines}\n"
            WIKI_INDEX.write_text(index, encoding="utf-8")
            log.info("Updated wiki/index.md")
        except Exception as e:
            log.warning("Could not update index: %s", e)

        # --- Append to wiki/log.md ---
        today = datetime.now().strftime("%Y-%m-%d")
        handles = ", ".join(f"@{w['handle']}" for w in written)
        log_entry = (
            f"\n## [{today}] x-wiki | Added {len(written)} X account skeleton(s)\n\n"
            f"Accounts: {handles}\n"
            f"Source: `scripts/build_x_wiki.py`\n"
        )
        try:
            with open(WIKI_LOG, "a", encoding="utf-8") as f:
                f.write(log_entry)
            log.info("Updated wiki/log.md")
        except Exception as e:
            log.warning("Could not update log: %s", e)

        log.info("Done: %d skeleton page(s) written", len(written))

    # Print enrichment prompt
    if args.enrich or (not args.dry_run and written):
        all_written = written if written else [
            {
                "name": a.get("name", a["handle"].lstrip("@")),
                "handle": a["handle"].lstrip("@"),
                "slug": slugify(a.get("name", a["handle"].lstrip("@"))),
                "file": slugify(a.get("name", a["handle"].lstrip("@"))) + ".md",
            }
            for a in accounts
        ]
        prompt = generate_enrich_prompt(all_written)
        if prompt:
            print(f"\n{'=' * 60}")
            print("ENRICHMENT PROMPT:")
            print(f"{'=' * 60}")
            print(prompt)
            print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
