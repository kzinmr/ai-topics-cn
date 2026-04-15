#!/usr/bin/env python3
"""36kr crawler for LLM/AI Agent topics.

Crawls 36kr (36氪) AI section for AI-related tech articles.
Extracts article data from window.initialState embedded in the HTML.
Outputs structured markdown files suitable for a knowledge wiki.

Usage:
    python scripts/crawl_36kr.py
    python scripts/crawl_36kr.py --limit 20
    python scripts/crawl_36kr.py --dry-run
    python scripts/crawl_36kr.py --no-detail
    python scripts/crawl_36kr.py --query "大模型"
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import httpx

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parent.parent
OUTBOX = ROOT_DIR / "inbox" / "36kr"

LISTING_URL = "https://36kr.com/information/AI/"
ARTICLE_URL_TPL = "https://36kr.com/p/{item_id}"

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

USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def log(msg: str) -> None:
    """Print progress message to stderr."""
    print(f"[36kr] {msg}", file=sys.stderr, flush=True)


def is_ai_related(text: str) -> bool:
    """Check whether *text* contains any AI/LLM keyword."""
    return bool(_KW_PATTERN.search(text))


def matched_keywords(text: str) -> list[str]:
    """Return de-duplicated list of AI keywords found in *text*."""
    return list({m.group() for m in _KW_PATTERN.finditer(text)})


def ts_to_date(ts: int | float | str) -> str:
    """Convert a timestamp to YYYY-MM-DD. Handles seconds and milliseconds."""
    try:
        v = int(ts)
        if v > 1e12:
            v = v // 1000
        return datetime.fromtimestamp(v, tz=timezone.utc).strftime("%Y-%m-%d")
    except Exception:
        return datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")


def slug(title: str) -> str:
    """Create a short filesystem-safe slug from a title."""
    h = hashlib.md5(title.encode()).hexdigest()[:8]
    safe = re.sub(r"[^\w\u4e00-\u9fff]+", "-", title)[:60].strip("-")
    return f"{safe}-{h}"


def clean_html(html: str) -> str:
    """Rough HTML → plain-text conversion."""
    text = re.sub(r"<br\s*/?>", "\n", html)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"&nbsp;", " ", text)
    text = re.sub(r"&lt;", "<", text)
    text = re.sub(r"&gt;", ">", text)
    text = re.sub(r"&amp;", "&", text)
    text = re.sub(r"&quot;", '"', text)
    text = re.sub(r"&#(\d+);", lambda m: chr(int(m.group(1))), text)
    return text.strip()


def truncate(text: str, max_len: int = 1500) -> str:
    if len(text) <= max_len:
        return text
    return text[:max_len].rsplit("\n", 1)[0] + "\n\n…(内容已截断)"


def build_client() -> httpx.Client:
    return httpx.Client(
        headers={
            "User-Agent": random.choice(USER_AGENTS),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Referer": "https://36kr.com/",
            "DNT": "1",
        },
        timeout=30,
        follow_redirects=True,
    )


def sleep_random(lo: float = 2.0, hi: float = 3.0) -> None:
    time.sleep(random.uniform(lo, hi))


# ---------------------------------------------------------------------------
# Extract window.initialState from HTML
# ---------------------------------------------------------------------------

def extract_initial_state(html: str) -> dict | None:
    """Parse the window.initialState JSON blob from a 36kr HTML page.

    36kr embeds state as ``window.initialState={...}`` (a potentially huge
    JSON object).  A simple regex can't reliably capture the entire blob
    because of nested braces and quoted strings, so we locate the opening
    brace and then walk forward with brace-counting.
    """
    # Find the assignment – skip references like ``window.initialState &&``
    # 36kr uses window.initialState={...} (no spaces)
    m = re.search(r"window\.initialState\s*=\s*(\{)", html)
    if not m:
        return None

    start = m.start(1)
    depth = 0
    i = start
    length = len(html)

    while i < length:
        ch = html[i]
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                break
        elif ch == '"':
            # Skip over string contents (respecting backslash escapes)
            i += 1
            while i < length:
                sc = html[i]
                if sc == '\\':
                    i += 1  # skip escaped character
                elif sc == '"':
                    break
                i += 1
        i += 1

    if depth != 0:
        log("  Brace-counting failed to find matching '}' for initialState")
        return None

    json_str = html[start:i + 1]

    try:
        return json.loads(json_str)
    except json.JSONDecodeError as exc:
        log(f"  JSON parse error for initialState ({len(json_str)} chars): {exc}")
        return None


# ---------------------------------------------------------------------------
# 36kr listing page
# ---------------------------------------------------------------------------

def fetch_listing(client: httpx.Client) -> list[dict]:
    """Fetch the AI section listing page and return article items."""
    log(f"Fetching listing: {LISTING_URL}")
    try:
        resp = client.get(LISTING_URL)
        resp.raise_for_status()
    except Exception as exc:
        log(f"  Error fetching listing page: {exc}")
        return []

    state = extract_initial_state(resp.text)
    if not state:
        log("  Could not extract window.initialState from listing page")
        return []

    # Navigate the nested data structure
    try:
        item_list = (
            state
            .get("information", {})
            .get("informationList", {})
            .get("itemList", [])
        )
    except (AttributeError, TypeError):
        item_list = []

    if not item_list:
        log("  No items found in informationList.itemList")
        # Try alternative paths in case the structure differs
        try:
            # Some 36kr pages nest differently
            for key in state:
                val = state[key]
                if isinstance(val, dict):
                    for k2 in val:
                        v2 = val[k2]
                        if isinstance(v2, dict) and "itemList" in v2:
                            item_list = v2["itemList"]
                            if item_list:
                                log(f"  Found items via alternative path: {key}.{k2}.itemList")
                                break
                if item_list:
                    break
        except Exception:
            pass

    log(f"  Got {len(item_list)} items from listing page")
    return item_list


# ---------------------------------------------------------------------------
# 36kr article detail page
# ---------------------------------------------------------------------------

def fetch_article_detail(client: httpx.Client, item_id: int | str) -> dict | None:
    """Fetch a single article detail page and return article data dict."""
    url = ARTICLE_URL_TPL.format(item_id=item_id)
    try:
        resp = client.get(url)
        resp.raise_for_status()
    except Exception as exc:
        log(f"  Error fetching article {item_id}: {exc}")
        return None

    state = extract_initial_state(resp.text)
    if not state:
        log(f"  Could not extract initialState from article {item_id}")
        return None

    try:
        detail = (
            state
            .get("articleDetail", {})
            .get("articleDetailData", {})
            .get("data", {})
        )
    except (AttributeError, TypeError):
        detail = {}

    if not detail:
        log(f"  No detail data found for article {item_id}")
        return None

    return detail


# ---------------------------------------------------------------------------
# Normalise listing item into common shape
# ---------------------------------------------------------------------------

def extract_article_info(
    raw: dict,
    detail: dict | None = None,
) -> dict | None:
    """Normalise a 36kr listing item (and optional detail) into a common dict.

    Returns None if the article is not AI-related or lacks essential data.
    """
    material = raw.get("templateMaterial", {})
    item_id = raw.get("itemId") or material.get("itemId", "")
    title = material.get("widgetTitle", "") or ""
    summary = material.get("summary", "") or ""
    author = material.get("authorName", "") or "36氪"
    publish_ts = material.get("publishTime", 0)

    if not title:
        return None

    url = ARTICLE_URL_TPL.format(item_id=item_id) if item_id else ""
    date = ts_to_date(publish_ts) if publish_ts else datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")

    # Build body text from detail page if available
    body = ""
    if detail:
        widget_content = detail.get("widgetContent", "") or ""
        body = clean_html(widget_content)
        # Prefer detail-level metadata if richer
        if not title and detail.get("widgetTitle"):
            title = detail["widgetTitle"]
        if not summary and detail.get("summary"):
            summary = detail["summary"]
        if detail.get("author"):
            author = detail["author"]
        if detail.get("publishTime"):
            date = ts_to_date(detail["publishTime"])

    # Combine all text for keyword matching
    combined = f"{title} {summary} {body}"
    if not is_ai_related(combined):
        return None

    # Build excerpt
    if body:
        excerpt = truncate(body, 1400)
    elif summary:
        excerpt = summary
    else:
        excerpt = "(暂无摘要)"

    tags = matched_keywords(combined)

    return {
        "title": title,
        "url": url,
        "author": author,
        "date": date,
        "score": 0,
        "excerpt": excerpt,
        "tags": tags,
        "item_id": str(item_id),
    }


# ---------------------------------------------------------------------------
# Markdown output
# ---------------------------------------------------------------------------

def item_to_markdown(item: dict) -> str:
    tags_str = json.dumps(item["tags"], ensure_ascii=False)
    lines = [
        "---",
        f'title: "{item["title"]}"',
        "source: 36kr",
        f'url: "{item["url"]}"',
        f'author: "{item["author"]}"',
        f"date: {item['date']}",
        f"score: {item['score']}",
        f"tags: {tags_str}",
        "---",
        "",
        f"# {item['title']}",
        "",
        item["excerpt"],
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
    limit: int = 30,
    dry_run: bool = False,
    fetch_detail: bool = True,
    query: str | None = None,
) -> list[dict]:
    """Run the full crawl. Returns list of saved items."""
    saved: list[dict] = []
    seen_ids: set[str] = set()
    client = build_client()

    # --- 1. Fetch AI section listing ---
    listing_items = fetch_listing(client)
    if not listing_items:
        log("No listing items retrieved. Aborting.")
        client.close()
        return saved

    sleep_random(2, 3)

    for raw in listing_items:
        if len(saved) >= limit:
            break

        material = raw.get("templateMaterial", {})
        item_id = str(raw.get("itemId") or material.get("itemId", ""))
        title = material.get("widgetTitle", "") or ""
        summary = material.get("summary", "") or ""

        if not item_id or not title:
            continue

        if item_id in seen_ids:
            continue
        seen_ids.add(item_id)

        # If a custom query is supplied, do a pre-filter on title/summary
        if query:
            if query.lower() not in f"{title} {summary}".lower():
                continue

        # Optionally fetch full article body
        detail = None
        if fetch_detail:
            log(f"  Fetching detail: {title[:40]}...")
            detail = fetch_article_detail(client, item_id)
            sleep_random(2, 3)

        item = extract_article_info(raw, detail=detail)
        if not item:
            continue

        save_item(item, dry_run=dry_run)
        saved.append(item)
        log(f"  ✓ {item['title'][:50]}")

    client.close()
    return saved


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Crawl 36kr AI section for AI/LLM articles",
    )
    parser.add_argument(
        "--limit", type=int, default=30,
        help="Maximum number of items to save (default: 30)",
    )
    parser.add_argument(
        "--query", type=str, default=None,
        help="Filter articles by keyword in title/summary",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Don't write files, just show what would be saved",
    )
    parser.add_argument(
        "--no-detail", action="store_true",
        help="Skip fetching article detail pages (faster, summary only)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> list[dict]:
    args = parse_args(argv)

    log(f"Starting 36kr crawl (limit={args.limit}, dry_run={args.dry_run}, detail={not args.no_detail})")

    saved = crawl(
        limit=args.limit,
        dry_run=args.dry_run,
        fetch_detail=not args.no_detail,
        query=args.query,
    )
    log(f"Done. Saved {len(saved)} items.")

    # Summary to stdout
    print(f"\n## 36kr crawl summary — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"\nTotal items: {len(saved)}\n")
    for i, item in enumerate(saved, 1):
        tags = ", ".join(item.get("tags", [])[:3])
        print(
            f"{i}. **{item['title'][:60]}** "
            f"({item['date']}, {tags}) — {item['url']}"
        )

    return saved


if __name__ == "__main__":
    main()
