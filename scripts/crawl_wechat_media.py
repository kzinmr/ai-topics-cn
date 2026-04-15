#!/usr/bin/env python3
"""WeChat public account (微信公众号) crawler for AI media.

Crawls Chinese AI media WeChat articles via Sogou WeChat search.
Targets top AI media accounts: 机器之心, PaperWeekly, 新智元, 量子位, etc.

Usage:
    python scripts/crawl_wechat_media.py
    python scripts/crawl_wechat_media.py --account "机器之心"
    python scripts/crawl_wechat_media.py --limit 20 --dry-run
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
from urllib.parse import quote, urljoin

import httpx
from bs4 import BeautifulSoup

# ---------------------------------------------------------------------------
ROOT_DIR = Path(__file__).resolve().parent.parent
OUTBOX = ROOT_DIR / "inbox" / "wechat-media"

# Target WeChat public accounts — Chinese AI deep media
WECHAT_ACCOUNTS = {
    "机器之心": "Top Chinese AI media, fast accurate paper analysis",
    "PaperWeekly": "Paper-focused, LLM/Agent implementation insights",
    "新智元": "AI industry news, China model comparisons",
    "量子位": "Popular AI news and trend tracking",
    "夕小瑶科技说": "AI researcher perspective, technical deep-dives",
    "AI前线": "InfoQ China AI channel, enterprise AI",
    "大模型生态圈": "LLM ecosystem focused content",
}

AI_KEYWORDS = [
    "大语言模型", "LLM", "AI Agent", "智能体", "RAG", "大模型", "GPT",
    "Claude", "Gemini", "开源模型", "微调", "fine-tuning",
    "提示工程", "prompt", "推理", "inference", "Transformer", "注意力机制",
    "向量数据库", "embedding", "多模态", "RLHF", "对齐", "AI安全", "AGI",
    "Qwen", "通义千问", "DeepSeek", "百川", "文心一言", "Kimi", "豆包",
    "Anthropic", "OpenAI", "Mistral", "Llama", "混元", "MCP",
    "function calling", "tool use", "代码生成", "编程助手", "Copilot",
    "Cursor", "coding agent", "ChatGPT", "langchain", "llamaindex",
]

_KW_PATTERN = re.compile("|".join(re.escape(k) for k in AI_KEYWORDS), re.IGNORECASE)

USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
]


def log(msg: str) -> None:
    print(f"[wechat] {msg}", file=sys.stderr, flush=True)


def is_ai_related(text: str) -> bool:
    return bool(_KW_PATTERN.search(text))


def matched_keywords(text: str) -> list[str]:
    return list({m.group() for m in _KW_PATTERN.finditer(text)})


def slug(title: str) -> str:
    h = hashlib.md5(title.encode()).hexdigest()[:8]
    safe = re.sub(r"[^\w\u4e00-\u9fff]+", "-", title)[:60].strip("-")
    return f"{safe}-{h}"


def clean_html(html: str) -> str:
    text = re.sub(r"<br\s*/?>", "\n", html)
    text = re.sub(r"<[^>]+>", "", text)
    for ent, ch in [("&nbsp;", " "), ("&lt;", "<"), ("&gt;", ">"),
                     ("&amp;", "&"), ("&quot;", '"')]:
        text = text.replace(ent, ch)
    return text.strip()


def truncate(text: str, max_len: int = 1500) -> str:
    if len(text) <= max_len:
        return text
    return text[:max_len].rsplit("\n", 1)[0] + "\n\n…(内容已截断)"


def sleep_random(lo: float = 3.0, hi: float = 5.0) -> None:
    time.sleep(random.uniform(lo, hi))


def build_client() -> httpx.Client:
    return httpx.Client(
        headers={
            "User-Agent": random.choice(USER_AGENTS),
            "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "DNT": "1",
        },
        timeout=30,
        follow_redirects=True,
    )


# ---------------------------------------------------------------------------
# Sogou WeChat search
# ---------------------------------------------------------------------------

def search_sogou_wechat(
    client: httpx.Client,
    query: str,
    page: int = 1,
) -> list[dict]:
    """Search WeChat articles via Sogou."""
    url = "https://weixin.sogou.com/weixin"
    params = {
        "type": "2",  # article search
        "s_from": "input",
        "query": query,
        "page": str(page),
    }
    results: list[dict] = []
    try:
        # First visit main page for cookies
        if not hasattr(client, '_sogou_init'):
            client.get("https://weixin.sogou.com/", follow_redirects=True)
            client._sogou_init = True  # type: ignore
            sleep_random(1, 2)

        resp = client.get(url, params=params)
        resp.raise_for_status()
        html = resp.text
    except Exception as exc:
        log(f"  Sogou search error for '{query}': {exc}")
        return results

    # Check for anti-bot
    if "请输入验证码" in html or len(html) < 1000:
        log(f"  Sogou anti-bot triggered for '{query}'")
        return results

    soup = BeautifulSoup(html, "lxml")

    # Parse article listings
    for item in soup.select(".news-list li, .news-box li, ul.news-list > li"):
        try:
            link_el = item.select_one("h3 a, .txt-box h3 a, a[href*='weixin.qq.com']")
            if not link_el:
                # Try broader selector
                link_el = item.select_one("a[href]")
            if not link_el:
                continue

            title = link_el.get_text(strip=True)
            href = link_el.get("href", "")
            if href and not href.startswith("http"):
                href = urljoin("https://weixin.sogou.com/", href)

            # Extract summary
            summary_el = item.select_one(".txt-info, p.txt-info, .s-p")
            summary = summary_el.get_text(strip=True) if summary_el else ""

            # Extract account name
            account_el = item.select_one(".account, .s2, .all-time-y2")
            account = account_el.get_text(strip=True) if account_el else ""

            # Extract date
            date_el = item.select_one(".s2, .all-time-y2, script")
            date_str = datetime.now().strftime("%Y-%m-%d")
            if date_el:
                # Sogou often puts timestamps in script tags
                ts_match = re.search(r"timeConvert\('(\d+)'\)", str(item))
                if ts_match:
                    ts = int(ts_match.group(1))
                    date_str = datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d")

            if title:
                results.append({
                    "title": clean_html(title),
                    "url": href,
                    "author": account or query.split()[0],
                    "date": date_str,
                    "summary": clean_html(summary),
                })
        except Exception as exc:
            log(f"  Parse error: {exc}")
            continue

    # Fallback: try extracting from any link structure
    if not results:
        for a_tag in soup.find_all("a", href=True):
            href = a_tag.get("href", "")
            title = a_tag.get_text(strip=True)
            if ("weixin.qq.com" in href or "sogou.com/link" in href) and len(title) > 10:
                results.append({
                    "title": clean_html(title),
                    "url": href if href.startswith("http") else urljoin("https://weixin.sogou.com/", href),
                    "author": query.split()[0],
                    "date": datetime.now().strftime("%Y-%m-%d"),
                    "summary": "",
                })

    return results


def fetch_article_content(client: httpx.Client, url: str) -> str:
    """Fetch and extract text from a WeChat article page."""
    try:
        resp = client.get(url)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "lxml")
        # WeChat article content is in #js_content
        content_div = soup.select_one("#js_content, .rich_media_content")
        if content_div:
            return clean_html(content_div.get_text(separator="\n"))
        # Fallback: get main text
        body = soup.select_one("body")
        if body:
            return clean_html(body.get_text(separator="\n"))[:2000]
    except Exception as exc:
        log(f"  Content fetch error: {exc}")
    return ""


# ---------------------------------------------------------------------------
# Markdown output
# ---------------------------------------------------------------------------

def item_to_markdown(item: dict) -> str:
    tags_str = json.dumps(item.get("tags", []), ensure_ascii=False)
    lines = [
        "---",
        f'title: "{item["title"]}"',
        "source: wechat-media",
        f'url: "{item["url"]}"',
        f'author: "{item["author"]}"',
        f"date: {item['date']}",
        f"score: 0",
        f"tags: {tags_str}",
        "---",
        "",
        f"# {item['title']}",
        "",
        f"> 来源: {item['author']} (微信公众号)",
        "",
        item.get("excerpt", item.get("summary", "")),
        "",
    ]
    if item.get("tags"):
        lines.append("## 涉及话题")
        for t in item["tags"]:
            lines.append(f"- {t}")
        lines.append("")
    if item.get("url"):
        lines.append(f"[原文链接]({item['url']})")
        lines.append("")
    return "\n".join(lines)


def save_item(item: dict, dry_run: bool = False) -> Path | None:
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{today}-{slug(item['title'])}.md"
    path = OUTBOX / filename
    if dry_run:
        log(f"  [dry-run] would write {path.name}")
        return path
    OUTBOX.mkdir(parents=True, exist_ok=True)
    path.write_text(item_to_markdown(item), encoding="utf-8")
    return path


# ---------------------------------------------------------------------------
# Main crawl
# ---------------------------------------------------------------------------

def crawl(
    accounts: dict[str, str] | None = None,
    limit: int = 30,
    dry_run: bool = False,
    fetch_content: bool = False,
) -> list[dict]:
    if accounts is None:
        accounts = WECHAT_ACCOUNTS

    saved: list[dict] = []
    seen_titles: set[str] = set()
    client = build_client()

    for account_name, description in accounts.items():
        if len(saved) >= limit:
            break

        # Search for this account's AI content
        queries = [
            f"{account_name}",
            f"{account_name} LLM AI Agent 大模型",
        ]

        for query in queries:
            if len(saved) >= limit:
                break

            log(f"Searching: {query}")
            results = search_sogou_wechat(client, query)
            log(f"  Got {len(results)} results")

            for raw in results:
                if len(saved) >= limit:
                    break

                title = raw["title"]
                if title in seen_titles or len(title) < 5:
                    continue

                combined = f"{title} {raw.get('summary', '')}"
                if not is_ai_related(combined):
                    continue

                seen_titles.add(title)

                # Optionally fetch full content
                if fetch_content and raw.get("url"):
                    content = fetch_article_content(client, raw["url"])
                    if content:
                        raw["excerpt"] = truncate(content)
                    sleep_random(2, 4)
                else:
                    raw["excerpt"] = raw.get("summary", "(暂无摘要)")

                raw["tags"] = matched_keywords(combined)
                save_item(raw, dry_run=dry_run)
                saved.append(raw)
                log(f"  ✓ [{account_name}] {title[:50]}")

            sleep_random(3, 5)

    client.close()
    return saved


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> list[dict]:
    parser = argparse.ArgumentParser(description="Crawl WeChat AI media articles")
    parser.add_argument("--limit", type=int, default=30)
    parser.add_argument("--account", type=str, default=None,
                        help="Single account to search (e.g. '机器之心')")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--fetch-content", action="store_true",
                        help="Fetch full article content (slower)")
    args = parser.parse_args(argv)

    accounts = None
    if args.account:
        accounts = {args.account: WECHAT_ACCOUNTS.get(args.account, "custom")}

    log(f"Starting WeChat media crawl (limit={args.limit})")
    saved = crawl(
        accounts=accounts,
        limit=args.limit,
        dry_run=args.dry_run,
        fetch_content=args.fetch_content,
    )
    log(f"Done. Saved {len(saved)} items.")

    print(f"\n## WeChat media crawl — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"\nTotal items: {len(saved)}\n")
    for i, item in enumerate(saved, 1):
        print(f"{i}. **{item['title'][:60]}** ({item['author']}) — {item['url']}")

    return saved


if __name__ == "__main__":
    main()
