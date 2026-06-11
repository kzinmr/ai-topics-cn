# Digest Search Patterns — `search_files` for Cron-Mode Research

When web_search is unavailable and subagents fail, the fastest way to check local crawl data is `search_files` on the daily digest directory.

## Basic Pattern

```python
from hermes_tools import search_files

results = search_files(
    pattern="Trae|通义灵码|Qoder|CodeGeeX|编程助手",
    path="~/ai-topics-cn/inbox/daily_digests",
    output_mode="content",
    limit=50
)
```

The `|` OR syntax covers multiple subtopics in one call. Daily digest files are small (< 20KB each) and ripgrep-backed — this is faster than reading them sequentially.

## Keyword Strategy

When `search_files` with Chinese keywords returns thin results (the digest files use title text, not tagged content):

1. **Read the 3 most recent digest files directly** — each is 60-80 lines covering V2EX/Juejin/36kr/wechat-media. Scan for topic-adjacent articles the grep may have missed.
2. **Extract URLs from digest entries** matching the topic — each entry has a source URL. Use `web_extract` (if available) or `browser_navigate` to read full articles.
3. **Cross-reference with inbox source files** — `search_files(pattern="<topic>", path="~/ai-topics-cn/inbox/juejin")` etc. to find raw source files with full metadata.

## Date Filtering

The digests are named `daily-digest-YYYY-MM-DD.md`. To limit search to a date range:

```python
search_files(
    pattern="Kimi Work|月之暗面",
    path="~/ai-topics-cn/inbox/daily_digests",
    file_glob="daily-digest-2026-06-*.md",  # glob filters by filename
    output_mode="content",
    limit=30
)
```

## When to Use This vs Reading Files Directly

| Situation | Approach |
|-----------|----------|
| Known keywords (Chinese names, products) | `search_files` with OR pattern |
| Broad topic scan — not sure what keywords to use | Read the most recent 2-3 digest files with `read_file` |
| Need full article metadata | After finding digest match, search inbox source dir with the article hash or URL fragment |
| Source-specific analysis | `search_files` with `path="~/ai-topics-cn/inbox/juejin"` (or v2ex/36kr/wechat-media) |

## Pitfalls

- **Chinese-English gap**: A digest entry about "Agentic Engineering" may not match Chinese keywords like "编程助手". Use both language patterns in the OR.
- **Digest truncation**: The `daily-digest-*.md` files show only title stub + tags + URL, not full article text. Use the URL for deeper content.
- **`file_glob` syntax**: The glob matches against the filename only, not the full path. `daily-digest-2026-06-*.md` works because all files are in the same directory.
