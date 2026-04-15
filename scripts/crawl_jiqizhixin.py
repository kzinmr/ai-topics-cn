#!/usr/bin/env python3
"""Jiqizhixin (机器之心) crawler for LLM/AI Agent topics.

Crawls jiqizhixin.com — China's #1 AI media outlet — for latest articles
with deep technical analysis of papers and industry developments.
Outputs structured markdown files.

Usage:
    python scripts/crawl_jiqizhixin.py
    python scripts/crawl_jiqizhixin.py --limit 20 --query "大语言模型"
    python scripts/crawl_jiqizhixin.py --dry-run

Notes:
    Requires curl_cffi for TLS-fingerprint impersonation (the site blocks
    plain httpx/requests).  Install with: pip install curl_cffi
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from curl_cffi import requests as cffi_requests
except ImportError:
    sys.exit(
        "curl_cffi is required but not installed.\n"
        "Install it with:  pip install curl_cffi"
    )

from bs4 import BeautifulSoup, Tag

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parent.parent
OUTBOX = ROOT_DIR / "inbox" / "jiqizhixin"

# API endpoints (discovered from the SPA's network calls)
API_ARTICLES = "https://www.jiqizhixin.com/api/article_library/articles.json"
API_ARTICLE_DETAIL = "https://www.jiqizhixin.com/api/article_library/articles/{slug}.json"

DEFAULT_SEARCH_QUERIES = [
    "LLM",
    "大语言模型",
    "AI Agent",
    "智能体",
    "RAG",
    "大模型",
    "MCP function calling",
    "coding agent",
    "DeepSeek",
    "prompt engineering",
]

AI_KEYWORDS = [
    "大语言模型", "LLM", "AI Agent", "智能体", "RAG", "大模型", "GPT",
    "Claude", "Gemini", "开源模型", "微调", "fine-tuning", "fine tuning",
    "提示工程", "prompt", "推理", "inference", "Transformer", "注意力机制",
    "向量数据库", "embedding", "多模态", "RLHF", "对齐", "AI安全", "AGI",
    "Qwen", "通义千问", "DeepSeek", "百川", "文心一言", "Kimi", "豆包",
    "Anthropic", "OpenAI", "Mistral", "Llama", "混元", "MCP",
    "function calling", "tool use", "代码生成", "编程助手", "Copilot",
    "Cursor", "coding agent", "ChatGPT", "langchain", "llamaindex",
]

_KW_PATTERN = re.compile(
    "|".join(re.escape(k) for k in AI_KEYWORDS),
    re.IGNORECASE,
)

IMPERSONATE = "chrome"  # curl_cffi browser impersonation profile


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def log(msg: str) -> None:
    print(f"[jiqizhixin] {msg}", file=sys.stderr, flush=True)


def is_ai_related(text: str) -> bool:
    return bool(_KW_PATTERN.search(text))


def matched_keywords(text: str) -> list[str]:
    return list({m.group() for m in _KW_PATTERN.finditer(text)})


def slug(title: str) -> str:
    """Create a short filesystem-safe slug from a title."""
    h = hashlib.md5(title.encode()).hexdigest()[:8]
    safe = re.sub(r"[^\w\u4e00-\u9fff]+", "-", title)[:60].strip("-")
    return f"{safe}-{h}"


def clean_html(html: str) -> str:
    """Convert HTML to plain text via BeautifulSoup."""
    if not html:
        return ""
    soup = BeautifulSoup(html, "html.parser")
    # Remove images, scripts, styles
    for tag in soup.find_all(["script", "style", "img"]):
        tag.decompose()
    text = soup.get_text(separator="\n")
    # Collapse multiple blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def truncate(text: str, max_len: int = 1500) -> str:
    if len(text) <= max_len:
        return text
    return text[:max_len].rsplit("\n", 1)[0] + "\n\n…(内容已截断)"


def parse_date(date_str: str) -> str:
    """Parse jiqizhixin date format to YYYY-MM-DD.

    Handles formats like:
      - '2026/04/15 11:30'
      - '2026-04-15 10:19:26'
      - '2026-04-15'
    """
    if not date_str:
        return datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")
    try:
        # Try slash format first
        for fmt in ("%Y/%m/%d %H:%M", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
            try:
                return datetime.strptime(date_str, fmt).strftime("%Y-%m-%d")
            except ValueError:
                continue
        # Fallback: extract just the date portion
        m = re.match(r"(\d{4})[/-](\d{2})[/-](\d{2})", date_str)
        if m:
            return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    except Exception:
        pass
    return datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")


def sleep_random(lo: float = 2.0, hi: float = 3.0) -> None:
    time.sleep(random.uniform(lo, hi))


# ---------------------------------------------------------------------------
# HTTP client (curl_cffi with Chrome TLS fingerprint)
# ---------------------------------------------------------------------------

def build_session() -> cffi_requests.Session:
    """Create a curl_cffi session that impersonates Chrome.

    jiqizhixin.com uses TLS fingerprinting and blocks plain httpx/requests.
    curl_cffi with browser impersonation bypasses this.
    """
    session = cffi_requests.Session(impersonate=IMPERSONATE)
    session.headers.update({
        "Accept": "application/json, text/html, */*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Referer": "https://www.jiqizhixin.com/articles",
    })
    return session


# ---------------------------------------------------------------------------
# API calls
# ---------------------------------------------------------------------------

def fetch_article_list(
    session: cffi_requests.Session,
    page: int = 1,
    per: int = 20,
    keyword: str | None = None,
    sort: str = "overall",
) -> dict:
    """Fetch the paginated article list from the API.

    Returns the full response dict with keys:
        success, articles, tags, totalCount, hasNextPage, ...
    """
    params: dict[str, Any] = {
        "page": page,
        "per": per,
    }
    if keyword:
        params["keyword"] = keyword
        params["sort"] = sort
        params["published"] = 0
    try:
        resp = session.get(API_ARTICLES, params=params, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except Exception as exc:
        log(f"  Error fetching article list (page={page}): {exc}")
        return {"success": False, "articles": [], "hasNextPage": False}


def fetch_article_detail(
    session: cffi_requests.Session,
    article_slug: str,
) -> dict | None:
    """Fetch full article content for a given slug.

    Returns dict with keys:
        title, author, copyright, published_at, description,
        cover_image_url, likes_count, liked, content, seo
    """
    url = API_ARTICLE_DETAIL.format(slug=article_slug)
    try:
        resp = session.get(url, timeout=30)
        if resp.status_code == 404:
            log(f"  Article not found: {article_slug}")
            return None
        resp.raise_for_status()
        return resp.json()
    except Exception as exc:
        log(f"  Error fetching article detail '{article_slug}': {exc}")
        return None


# ---------------------------------------------------------------------------
# Normalise article data
# ---------------------------------------------------------------------------

def extract_article_info(
    listing_item: dict,
    detail: dict | None = None,
) -> dict | None:
    """Normalise a listing-API item (optionally enriched with detail) into
    a common dict, or return None to skip."""
    title = listing_item.get("title", "")
    article_slug = listing_item.get("slug", "")
    tag_list = listing_item.get("tagList", [])
    author_name = listing_item.get("author", "机器之心")
    published_at = listing_item.get("publishedAt", "")
    category = listing_item.get("category", "")
    listing_content = listing_item.get("content", "")  # truncated excerpt

    if not title:
        return None

    # Build the combined text for keyword matching
    combined = f"{title} {listing_content} {' '.join(tag_list)}"

    # If we have the detail, use its richer content for matching too
    detail_content_html = ""
    likes_count = 0
    if detail:
        detail_content_html = detail.get("content", "")
        likes_count = detail.get("likes_count", 0)
        # Author may be a dict in detail
        author_obj = detail.get("author", {})
        if isinstance(author_obj, dict):
            author_name = author_obj.get("name", author_name)
        elif isinstance(author_obj, str):
            author_name = author_obj
        # Use detail published_at (more precise)
        if detail.get("published_at"):
            published_at = detail["published_at"]
        # SEO keywords
        seo = detail.get("seo", {})
        if isinstance(seo, dict):
            seo_kws = seo.get("keywords", [])
            if isinstance(seo_kws, list):
                tag_list = list(dict.fromkeys(tag_list + seo_kws))
        # Enrich combined text
        detail_text = clean_html(detail_content_html)
        combined = f"{title} {detail_text} {' '.join(tag_list)}"

    if not is_ai_related(combined):
        return None

    # Build excerpt
    if detail_content_html:
        excerpt = clean_html(detail_content_html)
    else:
        excerpt = listing_content
    excerpt = truncate(excerpt, 1500)

    # Date
    date = parse_date(published_at)

    # URL
    url = f"https://www.jiqizhixin.com/articles/{article_slug}" if article_slug else ""

    # Matched AI keywords
    ai_tags = matched_keywords(combined)
    all_tags = list(dict.fromkeys(ai_tags + [t for t in tag_list if t]))

    return {
        "title": title,
        "url": url,
        "author": author_name,
        "date": date,
        "score": likes_count,
        "excerpt": excerpt,
        "tags": all_tags,
        "slug": article_slug,
        "category": category,
    }


# ---------------------------------------------------------------------------
# Markdown output
# ---------------------------------------------------------------------------

def item_to_markdown(item: dict) -> str:
    tags_str = json.dumps(item["tags"], ensure_ascii=False)
    lines = [
        "---",
        f'title: "{item["title"]}"',
        "source: jiqizhixin",
        f'url: "{item["url"]}"',
        f'author: "{item["author"]}"',
        f"date: {item['date']}",
        f"score: {item['score']}",
        f"tags: {tags_str}",
        "---",
        "",
        f"# {item['title']}",
        "",
        item["excerpt"] if item["excerpt"] else "(暂无摘要)",
        "",
    ]
    if item["tags"]:
        lines.append("## 涉及话题")
        for t in item["tags"]:
            lines.append(f"- {t}")
        lines.append("")
    if item["url"]:
        lines.append(f"[原文链接]({item['url']})")
        lines.append("")
    return "\n".join(lines)


def save_item(item: dict, dry_run: bool = False) -> Path | None:
    """Write a single item to a markdown file. Returns the path or None."""
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{today}-{slug(item['title'])}.md"
    path = OUTBOX / filename
    md = item_to_markdown(item)
    if dry_run:
        log(f"  [dry-run] would write {path.name}")
        return path
    OUTBOX.mkdir(parents=True, exist_ok=True)
    path.write_text(md, encoding="utf-8")
    return path


# ---------------------------------------------------------------------------
# Main crawl logic
# ---------------------------------------------------------------------------

def crawl(
    queries: list[str] | None = None,
    limit: int = 30,
    dry_run: bool = False,
) -> list[dict]:
    """Run the full crawl.  Returns list of saved items."""
    if queries is None:
        queries = DEFAULT_SEARCH_QUERIES

    saved: list[dict] = []
    seen_slugs: set[str] = set()
    session = build_session()

    def try_save(listing_item: dict, source_label: str) -> bool:
        """Attempt to normalise and save an item.  Returns True if saved."""
        if len(saved) >= limit:
            return False

        article_slug = listing_item.get("slug", "")
        if article_slug in seen_slugs:
            return False
        seen_slugs.add(article_slug)

        title = listing_item.get("title", "")
        listing_content = listing_item.get("content", "")
        tag_list = listing_item.get("tagList", [])
        combined_quick = f"{title} {listing_content} {' '.join(tag_list)}"

        # Quick pre-filter before fetching detail
        if not is_ai_related(combined_quick):
            return False

        # Fetch full article content for richer excerpts
        detail = None
        if article_slug:
            detail = fetch_article_detail(session, article_slug)
            sleep_random(1.5, 2.5)

        item = extract_article_info(listing_item, detail=detail)
        if not item:
            return False

        save_item(item, dry_run=dry_run)
        saved.append(item)
        log(f"  ✓ [{source_label}] {item['title'][:50]}")
        return True

    # --- 1. Latest articles (multiple pages) ---
    pages_to_fetch = max(1, (limit + 19) // 20)  # enough pages to find matches
    pages_to_fetch = min(pages_to_fetch, 5)  # cap at 5 pages (100 articles)

    for page in range(1, pages_to_fetch + 1):
        if len(saved) >= limit:
            break
        log(f"Fetching latest articles (page {page})...")
        data = fetch_article_list(session, page=page, per=20)
        articles = data.get("articles", [])
        log(f"  Got {len(articles)} articles")

        for art in articles:
            if len(saved) >= limit:
                break
            try_save(art, f"latest-p{page}")

        if not data.get("hasNextPage", False):
            break
        sleep_random(2, 3)

    # --- 2. Keyword searches (optional, uses search API) ---
    for query in queries:
        if len(saved) >= limit:
            break
        log(f"Searching: {query}")
        data = fetch_article_list(
            session, page=1, per=20, keyword=query, sort="overall",
        )
        articles = data.get("articles", [])
        log(f"  Got {len(articles)} results for '{query}'")

        for art in articles:
            if len(saved) >= limit:
                break
            try_save(art, f"search:{query}")

        sleep_random(2, 3)

    session.close()
    return saved


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Crawl jiqizhixin.com (机器之心) for AI/LLM articles",
    )
    parser.add_argument(
        "--limit", type=int, default=30,
        help="Maximum number of items to save (default: 30)",
    )
    parser.add_argument(
        "--query", type=str, default=None,
        help="Custom search query (added to defaults, or used alone)",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Don't write files, just show what would be saved",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> list[dict]:
    args = parse_args(argv)
    queries = [args.query] if args.query else None

    log(f"Starting jiqizhixin crawl (limit={args.limit}, dry_run={args.dry_run})")
    saved = crawl(
        queries=queries,
        limit=args.limit,
        dry_run=args.dry_run,
    )
    log(f"Done. Saved {len(saved)} items.")

    # Summary to stdout
    print(f"\n## 机器之心 crawl summary — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"\nTotal items: {len(saved)}\n")
    for i, item in enumerate(saved, 1):
        score = item.get("score", 0)
        print(
            f"{i}. **{item['title'][:60]}** "
            f"(❤️ {score}) — {item['url']}"
        )

    return saved


if __name__ == "__main__":
    main()
