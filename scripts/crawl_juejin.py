#!/usr/bin/env python3
"""Juejin crawler for LLM/AI Agent topics.

Crawls Juejin (掘金) recommended articles, category feeds, and search results
for AI-related developer content. Outputs structured markdown files.

Usage:
    python scripts/crawl_juejin.py
    python scripts/crawl_juejin.py --limit 20 --query "大语言模型"
    python scripts/crawl_juejin.py --dry-run
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

import httpx

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parent.parent
OUTBOX = ROOT_DIR / "inbox" / "juejin"

# Juejin API endpoints
API_RECOMMEND = "https://api.juejin.cn/recommend_api/v1/article/recommend_all_feed"
API_CATE_FEED = "https://api.juejin.cn/recommend_api/v1/article/recommend_cate_feed"
API_SEARCH = "https://api.juejin.cn/search_api/v1/search"
API_TAG_FEED = "https://api.juejin.cn/recommend_api/v1/article/recommend_cate_tag_feed"

# Known category IDs
CATEGORY_AI = "6809637773935378440"       # 人工智能
CATEGORY_BACKEND = "6809637769959178254"   # 后端
CATEGORY_FRONTEND = "6809637767543259144"  # 前端

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

USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def log(msg: str) -> None:
    print(f"[juejin] {msg}", file=sys.stderr, flush=True)


def is_ai_related(text: str) -> bool:
    return bool(_KW_PATTERN.search(text))


def matched_keywords(text: str) -> list[str]:
    return list({m.group() for m in _KW_PATTERN.finditer(text)})


def ts_to_date(ts: int | float | str) -> str:
    """Convert a timestamp to YYYY-MM-DD. Handles seconds and milliseconds."""
    try:
        v = int(ts)
        # Juejin sometimes uses millisecond timestamps
        if v > 1e12:
            v = v // 1000
        return datetime.fromtimestamp(v, tz=timezone.utc).strftime("%Y-%m-%d")
    except Exception:
        return datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")


def datestr_to_date(s: str) -> str:
    """Parse an ISO-ish date string to YYYY-MM-DD."""
    if not s:
        return datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")
    try:
        # "2024-06-15T08:30:00+0800" or similar
        dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d")
    except Exception:
        # Try extracting just the date portion
        m = re.match(r"(\d{4}-\d{2}-\d{2})", s)
        return m.group(1) if m else datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")


def slug(title: str) -> str:
    h = hashlib.md5(title.encode()).hexdigest()[:8]
    safe = re.sub(r"[^\w\u4e00-\u9fff]+", "-", title)[:60].strip("-")
    return f"{safe}-{h}"


def clean_html(html: str) -> str:
    text = re.sub(r"<br\s*/?>", "\n", html)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"&nbsp;", " ", text)
    text = re.sub(r"&lt;", "<", text)
    text = re.sub(r"&gt;", ">", text)
    text = re.sub(r"&amp;", "&", text)
    return text.strip()


def truncate(text: str, max_len: int = 1500) -> str:
    if len(text) <= max_len:
        return text
    return text[:max_len].rsplit("\n", 1)[0] + "\n\n…(内容已截断)"


def build_client() -> httpx.Client:
    return httpx.Client(
        headers={
            "User-Agent": random.choice(USER_AGENTS),
            "Content-Type": "application/json",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Origin": "https://juejin.cn",
            "Referer": "https://juejin.cn/",
        },
        timeout=30,
        follow_redirects=True,
    )


def sleep_random(lo: float = 1.0, hi: float = 2.5) -> None:
    time.sleep(random.uniform(lo, hi))


# ---------------------------------------------------------------------------
# Juejin API calls
# ---------------------------------------------------------------------------

def fetch_recommend_feed(client: httpx.Client, limit: int = 40) -> list[dict]:
    """Fetch the general recommended article feed."""
    payload = {
        "id_type": 2,
        "client_type": 2608,
        "sort_type": 200,  # 200 = recommended, 300 = latest, 3 = hot
        "cursor": "0",
        "limit": min(limit, 40),
    }
    try:
        resp = client.post(API_RECOMMEND, json=payload)
        resp.raise_for_status()
        data = resp.json()
        return data.get("data", [])
    except Exception as exc:
        log(f"  Error fetching recommend feed: {exc}")
        return []


def fetch_category_feed(
    client: httpx.Client,
    category_id: str,
    sort_type: int = 200,
    limit: int = 40,
    cursor: str = "0",
) -> list[dict]:
    """Fetch articles from a specific category."""
    payload = {
        "id_type": 2,
        "client_type": 2608,
        "sort_type": sort_type,
        "cursor": cursor,
        "limit": min(limit, 40),
        "cate_id": category_id,
    }
    try:
        resp = client.post(API_CATE_FEED, json=payload)
        resp.raise_for_status()
        data = resp.json()
        return data.get("data", [])
    except Exception as exc:
        log(f"  Error fetching category {category_id}: {exc}")
        return []


def search_articles(
    client: httpx.Client,
    query: str,
    limit: int = 20,
) -> list[dict]:
    """Search Juejin articles via their search API."""
    all_results: list[dict] = []
    cursor = "0"
    per_page = min(limit, 20)

    while len(all_results) < limit:
        params = {
            "query": query,
            "search_type": 0,  # 0 = all, 2 = articles
            "cursor": cursor,
            "limit": per_page,
            "id_type": 0,
            "version": 1,
        }
        try:
            resp = client.get(API_SEARCH, params=params)
            resp.raise_for_status()
            data = resp.json()
            items = data.get("data", [])
            if not items:
                break
            all_results.extend(items)
            cursor = str(data.get("cursor", int(cursor) + per_page))
            if not data.get("has_more", False):
                break
        except Exception as exc:
            log(f"  Search error for '{query}': {exc}")
            break
        sleep_random(1, 2)

    return all_results[:limit]


# ---------------------------------------------------------------------------
# Normalise Juejin data
# ---------------------------------------------------------------------------

def extract_article_info(raw: dict) -> dict | None:
    """Extract article info from a Juejin feed/search result item."""
    # Feed items wrap the article in an "article_info" key
    article_info = raw.get("article_info", raw)
    article_id = article_info.get("article_id", "")

    title = article_info.get("title", "")
    brief = article_info.get("brief_content", "")
    content = article_info.get("content", "") or brief

    # Search results may nest differently
    if not title and "result_model" in raw:
        rm = raw["result_model"]
        article_info = rm.get("article_info", rm)
        article_id = article_info.get("article_id", article_id)
        title = article_info.get("title", "")
        brief = article_info.get("brief_content", "")
        content = article_info.get("content", "") or brief

    if not title:
        return None

    # Clean up search-highlight tags
    title = re.sub(r"</?em>", "", title)
    content = re.sub(r"</?em>", "", content)
    brief = re.sub(r"</?em>", "", brief)

    combined = f"{title} {content} {brief}"
    if not is_ai_related(combined):
        return None

    # Author info
    author_info = raw.get("author_user_info", {})
    if not author_info and "result_model" in raw:
        author_info = raw["result_model"].get("author_user_info", {})
    author = author_info.get("user_name", "匿名用户") if isinstance(author_info, dict) else "匿名用户"

    # Counters
    article_counter = raw.get("article_counter", {})
    if not article_counter and "result_model" in raw:
        article_counter = raw["result_model"].get("article_counter", {})
    view_count = article_counter.get("view", 0) if isinstance(article_counter, dict) else 0
    digg_count = article_counter.get("digg", article_info.get("digg_count", 0))
    collect_count = article_counter.get("collect", article_info.get("collect_count", 0))

    # Tags
    raw_tags = raw.get("tags", [])
    if not raw_tags and "result_model" in raw:
        raw_tags = raw["result_model"].get("tags", [])
    tag_names = []
    for t in raw_tags:
        if isinstance(t, dict):
            tag_names.append(t.get("tag_name", ""))
        elif isinstance(t, str):
            tag_names.append(t)
    ai_tags = matched_keywords(combined)
    all_tags = list(dict.fromkeys(ai_tags + [t for t in tag_names if t]))

    # Date
    ctime = article_info.get("ctime", "0")
    mtime = article_info.get("mtime", ctime)
    date = ts_to_date(ctime)

    # URL
    url = f"https://juejin.cn/post/{article_id}" if article_id else ""

    # Build excerpt
    excerpt_text = clean_html(content or brief)
    stats_line = f"\n\n> 👍 {digg_count}   👁️ {view_count}   ⭐ {collect_count}"
    excerpt_text = truncate(excerpt_text, 1400) + stats_line

    return {
        "title": title,
        "url": url,
        "author": author,
        "date": date,
        "score": digg_count,
        "view_count": view_count,
        "collect_count": collect_count,
        "excerpt": excerpt_text,
        "tags": all_tags,
        "article_id": article_id,
    }


# ---------------------------------------------------------------------------
# Markdown output
# ---------------------------------------------------------------------------

def item_to_markdown(item: dict) -> str:
    tags_str = json.dumps(item["tags"], ensure_ascii=False)
    lines = [
        "---",
        f'title: "{item["title"]}"',
        "source: juejin",
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
    if queries is None:
        queries = DEFAULT_SEARCH_QUERIES

    saved: list[dict] = []
    seen_ids: set[str] = set()
    client = build_client()

    def try_save(raw: dict, source_label: str) -> bool:
        """Attempt to normalise and save an item. Returns True if saved."""
        if len(saved) >= limit:
            return False
        item = extract_article_info(raw)
        if not item:
            return False
        aid = item.get("article_id", "")
        if aid in seen_ids:
            return False
        seen_ids.add(aid)
        save_item(item, dry_run=dry_run)
        saved.append(item)
        log(f"  ✓ [{source_label}] {item['title'][:50]}")
        return True

    # --- 1. AI category feed (recommended) ---
    log("Fetching AI category feed (recommended)...")
    ai_rec = fetch_category_feed(client, CATEGORY_AI, sort_type=200, limit=40)
    log(f"  Got {len(ai_rec)} items from AI category (recommended)")
    for raw in ai_rec:
        try_save(raw, "ai-rec")
    sleep_random(1, 2)

    # --- 2. AI category feed (latest) ---
    if len(saved) < limit:
        log("Fetching AI category feed (latest)...")
        ai_latest = fetch_category_feed(client, CATEGORY_AI, sort_type=300, limit=40)
        log(f"  Got {len(ai_latest)} items from AI category (latest)")
        for raw in ai_latest:
            try_save(raw, "ai-latest")
        sleep_random(1, 2)

    # --- 3. AI category feed (hot / three_days_hottest) ---
    if len(saved) < limit:
        log("Fetching AI category feed (hot)...")
        ai_hot = fetch_category_feed(client, CATEGORY_AI, sort_type=3, limit=40)
        log(f"  Got {len(ai_hot)} items from AI category (hot)")
        for raw in ai_hot:
            try_save(raw, "ai-hot")
        sleep_random(1, 2)

    # --- 4. General recommended feed (filter for AI) ---
    if len(saved) < limit:
        log("Fetching general recommended feed...")
        gen_rec = fetch_recommend_feed(client, limit=40)
        log(f"  Got {len(gen_rec)} items from general feed")
        for raw in gen_rec:
            try_save(raw, "general")
        sleep_random(1, 2)

    # --- 5. Backend category (filter for AI) ---
    if len(saved) < limit:
        log("Fetching backend category feed...")
        be_rec = fetch_category_feed(client, CATEGORY_BACKEND, sort_type=200, limit=40)
        log(f"  Got {len(be_rec)} items from backend category")
        for raw in be_rec:
            try_save(raw, "backend")
        sleep_random(1, 2)

    # --- 6. Search queries ---
    for query in queries:
        if len(saved) >= limit:
            break
        log(f"Searching: {query}")
        try:
            results = search_articles(client, query, limit=20)
            log(f"  Got {len(results)} search results for '{query}'")
        except Exception as exc:
            log(f"  Search error for '{query}': {exc}")
            results = []
        for raw in results:
            try_save(raw, f"search:{query}")
        sleep_random(1, 2.5)

    client.close()
    return saved


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Crawl Juejin for AI/LLM articles",
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
    parser.add_argument(
        "--search-only", action="store_true",
        help="Only run search queries, skip category feeds",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> list[dict]:
    args = parse_args(argv)

    queries = None
    if args.query:
        queries = [args.query]

    log(f"Starting Juejin crawl (limit={args.limit}, dry_run={args.dry_run})")

    if args.search_only:
        if queries is None:
            queries = DEFAULT_SEARCH_QUERIES
        # Minimal crawl: search only
        client = build_client()
        saved: list[dict] = []
        seen_ids: set[str] = set()
        for query in queries:
            if len(saved) >= args.limit:
                break
            log(f"Searching: {query}")
            try:
                results = search_articles(client, query, limit=20)
                for raw in results:
                    item = extract_article_info(raw)
                    if item and item["article_id"] not in seen_ids:
                        seen_ids.add(item["article_id"])
                        save_item(item, dry_run=args.dry_run)
                        saved.append(item)
                        log(f"  ✓ {item['title'][:50]}")
                        if len(saved) >= args.limit:
                            break
            except Exception as exc:
                log(f"  Error: {exc}")
            sleep_random(1, 2)
        client.close()
    else:
        saved = crawl(
            queries=queries,
            limit=args.limit,
            dry_run=args.dry_run,
        )

    log(f"Done. Saved {len(saved)} items.")

    print(f"\n## Juejin crawl summary — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"\nTotal items: {len(saved)}\n")
    for i, item in enumerate(saved, 1):
        score = item.get('score', 0)
        views = item.get('view_count', 0)
        print(
            f"{i}. **{item['title'][:60]}** "
            f"(👍 {score}, 👁️ {views}) — {item['url']}"
        )

    return saved


if __name__ == "__main__":
    main()
