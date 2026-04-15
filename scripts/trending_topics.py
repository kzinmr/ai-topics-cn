#!/usr/bin/env python3
"""Trending Topics Detection for Chinese AI media.

Scans recent inbox data from V2EX, Juejin, 36kr, Zhihu, and WeChat media
to detect topics mentioned by 2+ independent sources.

Usage:  python scripts/trending_topics.py              # last 3 days
        python scripts/trending_topics.py --days 7
"""
import argparse
import datetime
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import NamedTuple

REPO_ROOT = Path(__file__).resolve().parent.parent
INBOX_V2EX = REPO_ROOT / "inbox" / "v2ex"
INBOX_JUEJIN = REPO_ROOT / "inbox" / "juejin"
INBOX_36KR = REPO_ROOT / "inbox" / "36kr"
INBOX_ZHIHU = REPO_ROOT / "inbox" / "zhihu"
INBOX_WECHAT = REPO_ROOT / "inbox" / "wechat-media"
WIKI_ROOT = REPO_ROOT / "wiki"

TODAY = datetime.date.today()

# --- Topic patterns ---

ENTITY_PATTERNS = [
    # Chinese-origin models
    (r'\bQwen\b|通义千问', 'Qwen/通义千问'),
    (r'\bDeepSeek\b|深度求索', 'DeepSeek'),
    (r'ChatGLM|智谱', 'ChatGLM/智谱'),
    (r'\bKimi\b|Moonshot', 'Kimi/Moonshot'),
    (r'文心一言|百度', '文心一言/Baidu'),
    (r'豆包|字节跳动', '豆包/ByteDance'),
    (r'百川\b|Baichuan', '百川'),
    (r'MiniMax', 'MiniMax'),
    (r'混元|腾讯', '混元/Tencent'),
    (r'\bYi\b|零一万物', 'Yi/01.AI'),
    # International
    (r'\bOpenAI\b', 'OpenAI'),
    (r'\bAnthropic\b', 'Anthropic'),
    (r'\bClaude\b', 'Claude'),
    (r'\bGPT\b', 'GPT'),
    (r'\bGemini\b|Google', 'Gemini/Google'),
    (r'\bLlama\b|\bMeta\b', 'Llama/Meta'),
    (r'\bMistral\b', 'Mistral'),
    (r'\bCursor\b', 'Cursor'),
    (r'Manus\b', 'Manus'),
    (r'OpenClaw', 'OpenClaw'),
]

CONCEPT_PATTERNS = [
    (r'\bAgent|智能体|代理', 'AI Agent/智能体'),
    (r'\bMCP\b|Model Context Protocol', 'MCP'),
    (r'\bRAG\b|检索增强', 'RAG'),
    (r'微调|fine.?tun', '微调/Fine-tuning'),
    (r'推理优化|inference optim', '推理优化'),
    (r'量化|quantiz|GGUF', '量化/Quantization'),
    (r'多模态|multimodal|vision', '多模态'),
    (r'vibe.?cod|编程助手|coding agent', 'Vibe Coding'),
    (r'prompt.?engineer|提示工程', 'Prompt Engineering'),
    (r'向量数据库|vector.?db|embedding', 'Vector DB'),
    (r'RLHF|对齐|人类反馈', 'RLHF/对齐'),
    (r'开源模型|开源大模型|open.?source.?model', 'オープンソースモデル'),
    (r'function.?call|tool.?use|工具调用', 'Function Calling'),
    (r'本地部署|local.?deploy|私有化部署', 'ローカルデプロイ'),
    (r'内容审查|censor|合规', '規制/コンプライアンス'),
    (r'AI安全|ai.?safety|对齐', 'AI安全'),
    (r'训练框架|training.?frame', '訓練フレームワーク'),
]


class Mention(NamedTuple):
    topic: str
    category: str
    source_type: str
    source_file: str
    source_date: datetime.date | None


def parse_date(fname: str) -> datetime.date | None:
    m = re.search(r'(\d{4})-(\d{2})-(\d{2})', fname)
    if m:
        try:
            return datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        except ValueError:
            pass
    return None


def extract_mentions(text: str, source_type: str, source_file: str,
                     source_date: datetime.date | None) -> list[Mention]:
    mentions = []
    seen = set()
    for patterns, cat in [(ENTITY_PATTERNS, 'entity'), (CONCEPT_PATTERNS, 'concept')]:
        for regex, name in patterns:
            if name in seen:
                continue
            if re.search(regex, text, re.IGNORECASE):
                seen.add(name)
                mentions.append(Mention(name, cat, source_type, source_file, source_date))
    return mentions


def collect_recent(directory: Path, days: int) -> list[Path]:
    if not directory.is_dir():
        return []
    cutoff = TODAY - datetime.timedelta(days=days)
    result = []
    for f in sorted(directory.glob('*.md')):
        d = parse_date(f.name)
        if d and d >= cutoff:
            result.append(f)
        elif d is None:
            try:
                mtime = datetime.date.fromtimestamp(f.stat().st_mtime)
                if mtime >= cutoff:
                    result.append(f)
            except OSError:
                pass
    return result


def analyze(days: int) -> str:
    all_mentions: list[Mention] = []

    sources = [
        (INBOX_V2EX, 'v2ex'),
        (INBOX_JUEJIN, 'juejin'),
        (INBOX_36KR, '36kr'),
        (INBOX_ZHIHU, 'zhihu'),
        (INBOX_WECHAT, 'wechat'),
    ]

    for inbox_dir, source_type in sources:
        for f in collect_recent(inbox_dir, days):
            text = f.read_text(encoding='utf-8', errors='replace')
            d = parse_date(f.name)
            all_mentions.extend(extract_mentions(text, source_type, f.name, d))

    # Group and score
    topic_mentions: dict[str, list[Mention]] = defaultdict(list)
    for m in all_mentions:
        topic_mentions[m.topic].append(m)

    scored = []
    for topic, mentions in topic_mentions.items():
        unique_sources = set(m.source_file for m in mentions)
        source_types = set(m.source_type for m in mentions)
        if len(unique_sources) >= 2:
            scored.append({
                'topic': topic,
                'category': mentions[0].category,
                'count': len(unique_sources),
                'types': source_types,
                'files': sorted(unique_sources),
            })

    scored.sort(key=lambda x: (-x['count'], x['topic']))

    cutoff = TODAY - datetime.timedelta(days=days)
    lines = [
        f"# 🔥 トレンディングトピック — {TODAY}",
        "",
        f"分析期間: {cutoff} → {TODAY} ({days}日間)",
        f"2件以上の独立ソースで言及されたトピック: **{len(scored)}件**",
        "",
    ]

    # Summary
    for src_dir, label in sources:
        count = len(collect_recent(src_dir, days))
        lines.append(f"- {label}: {count}件")
    lines.append("")

    if not scored:
        lines.append("_トレンディングトピックなし_")
        return "\n".join(lines)

    # Hot topics (4+)
    hot = [s for s in scored if s['count'] >= 4]
    if hot:
        lines.append("## 🔥🔥 ホットトピック (4+ソース)")
        lines.append("")
        lines.append("| トピック | 種別 | ソース数 | ソース種別 |")
        lines.append("|---------|------|---------|------------|")
        for s in hot:
            types_str = ', '.join(sorted(s['types']))
            lines.append(f"| **{s['topic']}** | {s['category']} | {s['count']} | {types_str} |")
        lines.append("")

    # All trending
    lines.append("## 📈 全トレンディング")
    lines.append("")
    lines.append("| トピック | 種別 | ソース数 | ソース種別 |")
    lines.append("|---------|------|---------|------------|")
    for s in scored:
        types_str = ', '.join(sorted(s['types']))
        lines.append(f"| **{s['topic']}** | {s['category']} | {s['count']} | {types_str} |")
    lines.append("")

    # Cross-source
    cross = [s for s in scored if len(s['types']) >= 2]
    if cross:
        lines.append("## 🔀 クロスソース (高シグナル)")
        lines.append("")
        for s in cross:
            types_str = ' + '.join(sorted(s['types']))
            lines.append(f"- **{s['topic']}** ({s['count']}ソース: {types_str})")
        lines.append("")

    lines.append("---")
    lines.append("_Generated by trending_topics.py_")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Detect trending topics in Chinese AI sources")
    parser.add_argument('--days', type=int, default=3)
    args = parser.parse_args()
    print(analyze(args.days))


if __name__ == '__main__':
    main()
