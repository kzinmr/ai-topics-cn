#!/usr/bin/env python3
"""Zhihu crawler for LLM/AI Agent topics.

Crawls Zhihu (知乎) search results and topic pages for AI-related discussions.
Outputs structured markdown files suitable for a knowledge wiki.

Usage:
    python scripts/crawl_zhihu.py
    python scripts/crawl_zhihu.py --limit 20 --query "AI Agent"
    python scripts/crawl_zhihu.py --dry-run
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
from urllib.parse import quote, urljoin

import httpx

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parent.parent
OUTBOX = ROOT_DIR / "inbox" / "zhihu"

DEFAULT_QUERIES = [
    "大语言模型",
    "AI Agent",
    "LLM应用",
    "智能体",
    "RAG 检索增强",
    "大模型推理",
    "微调 fine-tuning",
    "提示工程 prompt engineering",
    "MCP function calling",
    "coding agent 编程助手",
    "DeepSeek",
    "开源大模型",
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
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15",
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def log(msg: str) -> None:
    """Print progress message to stderr."""
    print(f"[zhihu] {msg}", file=sys.stderr, flush=True)


def is_ai_related(text: str) -> bool:
    """Check whether *text* contains any AI/LLM keyword."""
    return bool(_KW_PATTERN.search(text))


def matched_keywords(text: str) -> list[str]:
    """Return de-duplicated list of AI keywords found in *text*."""
    return list({m.group() for m in _KW_PATTERN.finditer(text)})


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


def ts_to_date(ts: int | float | str) -> str:
    """Unix timestamp → YYYY-MM-DD."""
    try:
        return datetime.fromtimestamp(int(ts), tz=timezone.utc).strftime("%Y-%m-%d")
    except Exception:
        return datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")


def slug(title: str) -> str:
    """Create a short filesystem-safe slug from a title."""
    h = hashlib.md5(title.encode()).hexdigest()[:8]
    safe = re.sub(r"[^\w\u4e00-\u9fff]+", "-", title)[:60].strip("-")
    return f"{safe}-{h}"


def build_client() -> httpx.Client:
    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "text/html,application/json,application/xhtml+xml,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Referer": "https://www.zhihu.com/",
        "DNT": "1",
    }
    return httpx.Client(
        headers=headers,
        timeout=30,
        follow_redirects=True,
        http2=False,
    )


def sleep_random(lo: float = 2.0, hi: float = 4.0) -> None:
    time.sleep(random.uniform(lo, hi))


# ---------------------------------------------------------------------------
# Zhihu API / scraping helpers
# ---------------------------------------------------------------------------

def search_zhihu(client: httpx.Client, query: str, limit: int = 20) -> list[dict]:
    """Search Zhihu via the web search API and return raw result dicts."""
    results: list[dict] = []
    offset = 0
    per_page = 20

    while len(results) < limit:
        url = "https://www.zhihu.com/api/v4/search_v3"
        params = {
            "t": "general",
            "q": query,
            "correction": 1,
            "offset": offset,
            "limit": per_page,
        }
        try:
            resp = client.get(url, params=params)
            if resp.status_code == 403:
                log(f"  403 on search API for '{query}', trying HTML fallback")
                return search_zhihu_html(client, query, limit)
            resp.raise_for_status()
            data = resp.json()
        except httpx.HTTPStatusError as exc:
            log(f"  HTTP {exc.response.status_code} searching '{query}', trying fallback")
            return search_zhihu_html(client, query, limit)
        except Exception as exc:
            log(f"  Error searching '{query}': {exc}")
            return search_zhihu_html(client, query, limit)

        items = data.get("data", [])
        if not items:
            break

        for item in items:
            obj = item.get("object", item)
            results.append(obj)
            if len(results) >= limit:
                break

        if not data.get("paging", {}).get("is_end", True) is False:
            break
        offset += per_page
        sleep_random(2, 3.5)

    return results


def search_zhihu_html(client: httpx.Client, query: str, limit: int = 20) -> list[dict]:
    """Fallback: scrape search results from the HTML search page."""
    url = f"https://www.zhihu.com/search?type=content&q={quote(query)}"
    results: list[dict] = []
    try:
        resp = client.get(url)
        resp.raise_for_status()
        html = resp.text
    except Exception as exc:
        log(f"  HTML search failed for '{query}': {exc}")
        return results

    # Try to extract the initial SSR data JSON embedded in the page
    m = re.search(r'<script\s+id="js-initialData"[^>]*>(\{.*?\})</script>', html, re.S)
    if not m:
        log(f"  Could not find initialData in search page for '{query}'")
        return results

    try:
        initial = json.loads(m.group(1))
        entities = initial.get("initialState", {}).get("entities", {})
    except json.JSONDecodeError:
        log(f"  Failed to parse initialData JSON for '{query}'")
        return results

    # Extract answers
    for aid, answer in entities.get("answers", {}).items():
        results.append({
            "type": "answer",
            "id": aid,
            "question": answer.get("question", {}),
            "excerpt": answer.get("excerpt", ""),
            "content": answer.get("content", ""),
            "author": answer.get("author", {}),
            "voteup_count": answer.get("voteupCount", 0),
            "created_time": answer.get("createdTime", 0),
            "updated_time": answer.get("updatedTime", 0),
        })
        if len(results) >= limit:
            break

    # Extract articles
    if len(results) < limit:
        for artid, art in entities.get("articles", {}).items():
            results.append({
                "type": "article",
                "id": artid,
                "title": art.get("title", ""),
                "excerpt": art.get("excerpt", ""),
                "content": art.get("content", ""),
                "author": art.get("author", {}),
                "voteup_count": art.get("voteupCount", 0),
                "created_time": art.get("created", 0),
            })
            if len(results) >= limit:
                break

    return results


def fetch_hot(client: httpx.Client, limit: int = 50) -> list[dict]:
    """Fetch Zhihu hot list via API."""
    url = "https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total"
    params = {"limit": min(limit, 50)}
    try:
        resp = client.get(url, params=params)
        resp.raise_for_status()
        data = resp.json()
        return data.get("data", [])
    except Exception as exc:
        log(f"  Error fetching hot list: {exc}")
        return []


# ---------------------------------------------------------------------------
# Normalise results into a common shape
# ---------------------------------------------------------------------------

def normalise_item(raw: dict) -> dict | None:
    """Turn a raw Zhihu result into a normalised dict, or None to skip."""
    item_type = raw.get("type", "")

    # --- hot list item ---
    if "target" in raw and "detail_text" in raw:
        target = raw["target"]
        title = target.get("title", "")
        excerpt = clean_html(target.get("excerpt", ""))
        combined = f"{title} {excerpt}"
        if not is_ai_related(combined):
            return None
        author_obj = target.get("author", {})
        author = author_obj.get("name", "匿名用户") if isinstance(author_obj, dict) else "匿名用户"
        qid = target.get("id", "")
        url = f"https://www.zhihu.com/question/{qid}" if qid else ""
        return {
            "title": title,
            "url": url,
            "author": author,
            "date": ts_to_date(target.get("created", 0)),
            "score": raw.get("detail_text", "0"),
            "excerpt": truncate(excerpt),
            "tags": matched_keywords(combined),
        }

    # --- search result: answer ---
    if item_type == "answer" or "question" in raw:
        question = raw.get("question", {})
        title = question.get("title", "") or raw.get("title", "")
        content = clean_html(raw.get("content", "") or raw.get("excerpt", ""))
        combined = f"{title} {content}"
        if not is_ai_related(combined):
            return None
        author_obj = raw.get("author", {})
        author = author_obj.get("name", "匿名用户") if isinstance(author_obj, dict) else "匿名用户"
        qid = question.get("id", "") or raw.get("id", "")
        url = f"https://www.zhihu.com/question/{qid}" if qid else ""
        return {
            "title": title or "(无标题)",
            "url": url,
            "author": author,
            "date": ts_to_date(raw.get("created_time", raw.get("updated_time", 0))),
            "score": raw.get("voteup_count", 0),
            "excerpt": truncate(content),
            "tags": matched_keywords(combined),
        }

    # --- search result: article ---
    if item_type == "article" or ("title" in raw and "content" in raw):
        title = raw.get("title", "")
        content = clean_html(raw.get("content", "") or raw.get("excerpt", ""))
        combined = f"{title} {content}"
        if not is_ai_related(combined):
            return None
        author_obj = raw.get("author", {})
        author = author_obj.get("name", "匿名用户") if isinstance(author_obj, dict) else "匿名用户"
        artid = raw.get("id", "")
        url = f"https://zhuanlan.zhihu.com/p/{artid}" if artid else ""
        return {
            "title": title or "(无标题)",
            "url": url,
            "author": author,
            "date": ts_to_date(raw.get("created_time", raw.get("created", 0))),
            "score": raw.get("voteup_count", 0),
            "excerpt": truncate(content),
            "tags": matched_keywords(combined),
        }

    # --- generic fallback: just look for title + content/excerpt ---
    title = raw.get("title", raw.get("name", ""))
    excerpt = clean_html(raw.get("excerpt", raw.get("content", raw.get("description", ""))))
    combined = f"{title} {excerpt}"
    if not title or not is_ai_related(combined):
        return None
    author_obj = raw.get("author", {})
    author = author_obj.get("name", "匿名用户") if isinstance(author_obj, dict) else "匿名用户"
    url = raw.get("url", "")
    if url and not url.startswith("http"):
        url = f"https://www.zhihu.com{url}"
    return {
        "title": title,
        "url": url,
        "author": author,
        "date": ts_to_date(raw.get("created_time", raw.get("created", 0))),
        "score": raw.get("voteup_count", 0),
        "excerpt": truncate(excerpt),
        "tags": matched_keywords(combined),
    }


# ---------------------------------------------------------------------------
# Markdown output
# ---------------------------------------------------------------------------

def item_to_markdown(item: dict) -> str:
    tags_str = json.dumps(item["tags"], ensure_ascii=False)
    score = item.get("score", 0)
    if isinstance(score, str):
        # e.g. "1234 万热度"
        score_display = score
    else:
        score_display = str(score)

    lines = [
        "---",
        f'title: "{item["title"]}"',
        "source: zhihu",
        f'url: "{item["url"]}"',
        f'author: "{item["author"]}"',
        f"date: {item['date']}",
        f"score: {score_display}",
        f"tags: {tags_str}",
        "---",
        "",
        f"# {item['title']}",
        "",
        item["excerpt"] if item["excerpt"] else "(暂无摘要)",
        "",
    ]

    # Key discussion points from tags
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
    include_hot: bool = True,
) -> list[dict]:
    """Run the full crawl. Returns list of saved items."""
    if queries is None:
        queries = DEFAULT_QUERIES

    saved: list[dict] = []
    seen_titles: set[str] = set()
    client = build_client()

    # --- Hot list ---
    if include_hot:
        log("Fetching hot list...")
        try:
            hot_items = fetch_hot(client, limit=50)
            log(f"  Got {len(hot_items)} hot items")
            for raw in hot_items:
                item = normalise_item(raw)
                if item and item["title"] not in seen_titles:
                    seen_titles.add(item["title"])
                    save_item(item, dry_run=dry_run)
                    saved.append(item)
                    log(f"  ✓ {item['title'][:50]}")
        except Exception as exc:
            log(f"  Hot list error: {exc}")
        sleep_random(2, 4)

    # --- Search queries ---
    for query in queries:
        if len(saved) >= limit:
            break
        log(f"Searching: {query}")
        remaining = limit - len(saved)
        try:
            results = search_zhihu(client, query, limit=min(remaining + 5, 20))
            log(f"  Got {len(results)} raw results")
        except Exception as exc:
            log(f"  Search error for '{query}': {exc}")
            results = []

        for raw in results:
            if len(saved) >= limit:
                break
            item = normalise_item(raw)
            if item and item["title"] not in seen_titles:
                seen_titles.add(item["title"])
                save_item(item, dry_run=dry_run)
                saved.append(item)
                log(f"  ✓ {item['title'][:50]}")

        sleep_random(2, 4)

    client.close()
    return saved


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Crawl Zhihu for AI/LLM topics",
    )
    parser.add_argument(
        "--limit", type=int, default=30,
        help="Maximum number of items to save (default: 30)",
    )
    parser.add_argument(
        "--query", type=str, default=None,
        help="Custom search query (overrides default list)",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Don't write files, just show what would be saved",
    )
    parser.add_argument(
        "--no-hot", action="store_true",
        help="Skip the hot-list fetch",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> list[dict]:
    args = parse_args(argv)
    queries = [args.query] if args.query else None

    log(f"Starting Zhihu crawl (limit={args.limit}, dry_run={args.dry_run})")
    saved = crawl(
        queries=queries,
        limit=args.limit,
        dry_run=args.dry_run,
        include_hot=not args.no_hot,
    )
    log(f"Done. Saved {len(saved)} items.")

    # Summary to stdout
    print(f"\n## Zhihu crawl summary — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"\nTotal items: {len(saved)}\n")
    for i, item in enumerate(saved, 1):
        score = item.get('score', 0)
        print(f"{i}. **{item['title'][:60]}** (score: {score}) — {item['url']}")

    return saved


if __name__ == "__main__":
    main()
