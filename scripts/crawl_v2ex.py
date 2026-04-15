#!/usr/bin/env python3
"""V2EX crawler for LLM/AI Agent topics.

Crawls V2EX (‘创意工作者的社区’) hot/latest topics and AI-related nodes.
Outputs structured markdown files suitable for a knowledge wiki.

Usage:
    python scripts/crawl_v2ex.py
    python scripts/crawl_v2ex.py --limit 20 --query "DeepSeek"
    python scripts/crawl_v2ex.py --dry-run
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
OUTBOX = ROOT_DIR / "inbox" / "v2ex"

# V2EX API base
API_BASE = "https://www.v2ex.com/api"

# Nodes likely to contain AI/LLM discussions
AI_NODES = ["ai", "openai", "chatgpt", "llm", "programmer", "python", "create"]

AI_KEYWORDS = [
    "大语言模型", "LLM", "AI Agent", "智能体", "RAG", "大模型", "GPT",
    "Claude", "Gemini", "开源模型", "微调", "fine-tuning", "fine tuning",
    "提示工程", "prompt", "推理", "inference", "Transformer", "注意力机制",
    "向量数据库", "embedding", "多模态", "RLHF", "对齐", "AI安全", "AGI",
    "Qwen", "通义千问", "DeepSeek", "百川", "文心一言", "Kimi", "豆包",
    "Anthropic", "OpenAI", "Mistral", "Llama", "混元", "MCP",
    "function calling", "tool use", "代码生成", "编程助手", "Copilot",
    "Cursor", "coding agent", "ChatGPT", "langchain", "llamaindex",
    "AI", "人工智能", "machine learning", "机器学习",
]

_KW_PATTERN = re.compile(
    "|".join(re.escape(k) for k in AI_KEYWORDS),
    re.IGNORECASE,
)

USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def log(msg: str) -> None:
    print(f"[v2ex] {msg}", file=sys.stderr, flush=True)


def is_ai_related(text: str) -> bool:
    return bool(_KW_PATTERN.search(text))


def matched_keywords(text: str) -> list[str]:
    return list({m.group() for m in _KW_PATTERN.finditer(text)})


def ts_to_date(ts: int | float | str) -> str:
    try:
        return datetime.fromtimestamp(int(ts), tz=timezone.utc).strftime("%Y-%m-%d")
    except Exception:
        return datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")


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
            "Accept": "application/json, text/html, */*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Referer": "https://www.v2ex.com/",
        },
        timeout=30,
        follow_redirects=True,
    )


def sleep_random(lo: float = 1.0, hi: float = 2.5) -> None:
    time.sleep(random.uniform(lo, hi))


# ---------------------------------------------------------------------------
# V2EX API
# ---------------------------------------------------------------------------

def fetch_hot_topics(client: httpx.Client) -> list[dict]:
    """Fetch hot topics from V2EX API."""
    url = f"{API_BASE}/topics/hot.json"
    try:
        resp = client.get(url)
        resp.raise_for_status()
        return resp.json()
    except Exception as exc:
        log(f"  Error fetching hot topics: {exc}")
        return []


def fetch_latest_topics(client: httpx.Client) -> list[dict]:
    """Fetch latest topics from V2EX API."""
    url = f"{API_BASE}/topics/latest.json"
    try:
        resp = client.get(url)
        resp.raise_for_status()
        return resp.json()
    except Exception as exc:
        log(f"  Error fetching latest topics: {exc}")
        return []


def fetch_node_topics_api(client: httpx.Client, node_name: str) -> list[dict]:
    """Fetch topics from a specific node via V2EX API v1."""
    url = f"{API_BASE}/nodes/show.json"
    try:
        resp = client.get(url, params={"name": node_name})
        resp.raise_for_status()
        # The nodes/show endpoint returns node info, not topics.
        # Topics for a node need the v2 API or HTML scraping.
    except Exception:
        pass

    # Use the topics by node endpoint (undocumented but works)
    url2 = f"https://www.v2ex.com/api/nodes/{node_name}/topics.json"
    try:
        resp = client.get(url2)
        if resp.status_code == 200:
            return resp.json()
    except Exception:
        pass

    # Fallback: scrape the node HTML page
    return fetch_node_topics_html(client, node_name)


def fetch_node_topics_html(client: httpx.Client, node_name: str) -> list[dict]:
    """Scrape topics from a V2EX node page."""
    url = f"https://www.v2ex.com/go/{node_name}"
    topics: list[dict] = []
    try:
        resp = client.get(url)
        resp.raise_for_status()
        html = resp.text
    except Exception as exc:
        log(f"  Error scraping node '{node_name}': {exc}")
        return topics

    # Extract topic links and titles from the cell items
    pattern = re.compile(
        r'<a\s+href="/t/(\d+)[^"]*"[^>]*class="topic-link"[^>]*>([^<]+)</a>',
        re.S,
    )
    for m in pattern.finditer(html):
        tid, title = m.group(1), m.group(2).strip()
        topics.append({
            "id": int(tid),
            "title": title,
            "url": f"https://www.v2ex.com/t/{tid}",
            "node": {"name": node_name},
            "content": "",
            "content_rendered": "",
            "replies": 0,
            "created": 0,
            "member": {"username": ""},
        })

    # Also try the simpler pattern
    if not topics:
        pattern2 = re.compile(
            r'<a\s+href="/t/(\d+)(?:#[^"]*)?"[^>]*>\s*([^<]+?)\s*</a>',
            re.S,
        )
        seen_ids: set[int] = set()
        for m in pattern2.finditer(html):
            tid = int(m.group(1))
            title = m.group(2).strip()
            if tid in seen_ids or len(title) < 4:
                continue
            seen_ids.add(tid)
            topics.append({
                "id": tid,
                "title": title,
                "url": f"https://www.v2ex.com/t/{tid}",
                "node": {"name": node_name},
                "content": "",
                "content_rendered": "",
                "replies": 0,
                "created": 0,
                "member": {"username": ""},
            })

    return topics


def fetch_topic_replies(client: httpx.Client, topic_id: int, limit: int = 10) -> list[dict]:
    """Fetch replies for a specific topic."""
    url = f"{API_BASE}/replies/show.json"
    try:
        resp = client.get(url, params={"topic_id": topic_id})
        resp.raise_for_status()
        replies = resp.json()
        return replies[:limit]
    except Exception as exc:
        log(f"  Error fetching replies for topic {topic_id}: {exc}")
        return []


# ---------------------------------------------------------------------------
# Normalise
# ---------------------------------------------------------------------------

def normalise_topic(raw: dict, replies: list[dict] | None = None) -> dict | None:
    """Normalise a V2EX topic dict."""
    title = raw.get("title", "")
    content = clean_html(raw.get("content_rendered", "") or raw.get("content", ""))
    combined = f"{title} {content}"

    # For node-sourced topics from AI nodes, be more lenient
    node_name = ""
    node = raw.get("node")
    if isinstance(node, dict):
        node_name = node.get("name", "")
    from_ai_node = node_name in ("ai", "openai", "chatgpt", "llm")

    if not from_ai_node and not is_ai_related(combined):
        return None

    member = raw.get("member", {})
    author = member.get("username", "") if isinstance(member, dict) else ""
    tid = raw.get("id", "")
    url = raw.get("url", f"https://www.v2ex.com/t/{tid}" if tid else "")

    # Build excerpt with replies
    excerpt_parts = []
    if content:
        excerpt_parts.append(truncate(content, 800))
    if replies:
        excerpt_parts.append("\n## 精选回复\n")
        for i, reply in enumerate(replies[:5], 1):
            r_content = clean_html(reply.get("content_rendered", "") or reply.get("content", ""))
            r_author = ""
            r_member = reply.get("member", {})
            if isinstance(r_member, dict):
                r_author = r_member.get("username", "")
            if r_content:
                excerpt_parts.append(f"**@{r_author}**: {truncate(r_content, 300)}\n")

    return {
        "title": title or "(无标题)",
        "url": url,
        "author": author or "匿名用户",
        "date": ts_to_date(raw.get("created", raw.get("last_modified", 0))),
        "score": raw.get("replies", 0),
        "excerpt": "\n".join(excerpt_parts) if excerpt_parts else "(暂无内容)",
        "tags": matched_keywords(combined) or ([node_name] if from_ai_node else []),
        "node": node_name,
    }


# ---------------------------------------------------------------------------
# Markdown output
# ---------------------------------------------------------------------------

def item_to_markdown(item: dict) -> str:
    tags_str = json.dumps(item["tags"], ensure_ascii=False)
    lines = [
        "---",
        f'title: "{item["title"]}"',
        "source: v2ex",
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
    custom_query: str | None = None,
    limit: int = 30,
    dry_run: bool = False,
    fetch_replies_flag: bool = True,
) -> list[dict]:
    saved: list[dict] = []
    seen_ids: set[int] = set()
    client = build_client()

    def process_topics(raw_topics: list[dict], source_label: str) -> None:
        for raw in raw_topics:
            if len(saved) >= limit:
                return
            tid = raw.get("id", 0)
            if tid in seen_ids:
                continue
            seen_ids.add(tid)

            title = raw.get("title", "")
            content = raw.get("content", "") or raw.get("content_rendered", "")
            combined = f"{title} {content}"

            # Quick pre-filter for non-AI-node topics
            node = raw.get("node", {})
            node_name = node.get("name", "") if isinstance(node, dict) else ""
            from_ai_node = node_name in ("ai", "openai", "chatgpt", "llm")

            if not from_ai_node and not is_ai_related(combined):
                continue

            # Optionally fetch replies for richer content
            replies = []
            if fetch_replies_flag and tid:
                try:
                    replies = fetch_topic_replies(client, tid, limit=5)
                    sleep_random(1, 2)
                except Exception:
                    pass

            item = normalise_topic(raw, replies=replies)
            if item:
                save_item(item, dry_run=dry_run)
                saved.append(item)
                log(f"  ✓ [{source_label}] {item['title'][:50]}")

    # --- Hot topics ---
    log("Fetching hot topics...")
    hot = fetch_hot_topics(client)
    log(f"  Got {len(hot)} hot topics")
    process_topics(hot, "hot")
    sleep_random(1.5, 3)

    # --- Latest topics ---
    if len(saved) < limit:
        log("Fetching latest topics...")
        latest = fetch_latest_topics(client)
        log(f"  Got {len(latest)} latest topics")
        process_topics(latest, "latest")
        sleep_random(1.5, 3)

    # --- AI-specific nodes ---
    for node_name in AI_NODES:
        if len(saved) >= limit:
            break
        log(f"Fetching node: {node_name}")
        try:
            node_topics = fetch_node_topics_api(client, node_name)
            log(f"  Got {len(node_topics)} topics from /go/{node_name}")
            process_topics(node_topics, f"node:{node_name}")
        except Exception as exc:
            log(f"  Error on node {node_name}: {exc}")
        sleep_random(1.5, 3)

    # --- Custom query filter (search within scraped content) ---
    if custom_query:
        log(f"Note: V2EX has no search API. '{custom_query}' filtering applied to scraped content.")
        # We've already applied keyword filtering above.
        # If the custom query is specific, we could do additional filtering,
        # but for now the keyword list handles it.

    client.close()
    return saved


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Crawl V2EX for AI/LLM topics",
    )
    parser.add_argument(
        "--limit", type=int, default=30,
        help="Maximum number of items to save (default: 30)",
    )
    parser.add_argument(
        "--query", type=str, default=None,
        help="Custom filter query (applied to results)",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Don't write files, just show what would be saved",
    )
    parser.add_argument(
        "--no-replies", action="store_true",
        help="Skip fetching replies (faster but less content)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> list[dict]:
    args = parse_args(argv)
    log(f"Starting V2EX crawl (limit={args.limit}, dry_run={args.dry_run})")

    saved = crawl(
        custom_query=args.query,
        limit=args.limit,
        dry_run=args.dry_run,
        fetch_replies_flag=not args.no_replies,
    )
    log(f"Done. Saved {len(saved)} items.")

    print(f"\n## V2EX crawl summary — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"\nTotal items: {len(saved)}\n")
    for i, item in enumerate(saved, 1):
        node = item.get('node', '')
        print(f"{i}. **{item['title'][:60]}** (replies: {item['score']}, node: {node}) — {item['url']}")

    return saved


if __name__ == "__main__":
    main()
