---
name: active-crawl-workflow
description: Active crawl workflow — reads hot-topics.yaml, selects high-priority un-crawled topics, deep-dives via web search, creates wiki concept pages, and updates tracking
category: research
version: 1.0.0
---

# Active Crawl Workflow

Topic-driven deep-diving based on `config/hot-topics.yaml` configuration. Distinct from `crawl-and-triage-workflow` which focuses on multi-source article collection and semantic triage.

## Cron Job Configuration
- **Schedule**: 11:00 JST daily
- **Purpose**: Deep-dive into hot topics that haven't been crawled recently
- **Related**: `trending-topics` (10:00 JST) identifies hot topics, `active-crawl` (11:00 JST) deep-dives them

## Execution Steps

### 1. Read and Filter Topics
```bash
cat ~/ai-topics-cn/config/hot-topics.yaml
```
Select topics matching:
- `crawl_policy`: prerequisites | laterals | deepdive
- `last_crawled`: null OR 3+ days ago
- Priority order: `high` (max 2) → `medium` (max 1)

### 2. Deep-Dive Each Topic
For each selected topic, use its `search_hints` for web research:
- Search Chinese AI sources (V2EX, Juejin, 36kr, Zhihu, WeChat media)
- Find recent developments, technical details, community reactions
- Cross-reference with existing wiki pages to avoid duplication

### 3. Create/Update Wiki Pages
- Check if page exists first: look in `wiki/concepts/`, `wiki/entities/`, and `wiki/pages/` (varies by topic type)
- Always `read_file` the existing page first to see current content
- Compare search results with existing content: identify what's stale vs new
- For updates: use `write_file` (not patch) — wiki pages are complex markdown with tables and YAML frontmatter
- New concept pages: `wiki/concepts/[topic-slug].md`
- Entity/model pages: `wiki/entities/[topic-slug].md`
- Product/tool pages: `wiki/pages/[topic-slug].md`
- Follow SCHEMA.md format
- Include: overview, key findings, Chinese sources, Japanese analysis
- Update `updated:` date in frontmatter

### 4. Update Tracking
- Edit `hot-topics.yaml`: set `last_crawled: YYYY-MM-DD` for processed topics
- Update `wiki/log.md` with crawl results
- Update `wiki/index.md` statistics

### 5. Commit and Push
```bash
cd ~/ai-topics-cn
git add -A
git commit -m "active-crawl: add [topic] concept pages + update hot-topics"
git push
```

## Output Format
Generate Japanese report with:
```
📊 Active Crawl Report — YYYY-MM-DD
対象トピック: [topic1], [topic2], [topic3]
新規ページ: N件
更新ページ: N件
主要発見: [bullet points]
hot-topics.yaml 更新: [list of updated topics]
```

## Key Differences from crawl-and-triage
| Aspect | crawl-and-triage | active-crawl |
|--------|------------------|--------------|
| Trigger | Scheduled (06:00, 18:00 JST) | Topic-driven (11:00 JST) |
| Input | Multi-source article inbox | hot-topics.yaml config |
| Method | Semantic triage of collected articles | Deep-dive web research |
| Output | Triage report, wiki updates | Concept pages, config updates |
| Scope | Broad coverage | Focused depth |

## Known Patterns
- DeepSeek-V4: 1T MoE, Engram memory, mHC, Ascend 910C, Cambricon MLU, $0.30/MTok
- Vibe Coding → Agentic Engineering: Karpathy paradigm shift, Cursor $293B valuation
- MCP China ecosystem: Linux Foundation AAIF, Dify/Coze integration, A2A protocol
- 国产AI编程助手: 通义灵码, CodeGeeX, MarsCode, 文心快码, 腾讯云AI代码助手

## Pitfalls

- **Canonical paths**: Use `~/ai-topics-cn` for the repository and `~/wiki` for wiki paths. Do not introduce environment-specific absolute paths.
- **Wiki page location varies by topic type**: Concept topics go in `wiki/concepts/[slug].md`, model/entity topics go in `wiki/entities/[slug].md`, and product/tool topics go in `wiki/pages/[slug].md`. Check all three directories before deciding to create new.
- **Always read existing wiki page before updating**: Use `read_file` to see current content. Compare with search results to identify what's stale vs new.
  - **Use `patch` for targeted updates** (adding sections, updating table rows, appending paragraphs): fuzzy matching handles indentation differences, avoids full rewrite risk, and is faster. Ensure `old_string` is unique within the file.
  - **Use `write_file` only when restructuring** (changing frontmatter schema, reorganizing sections, or the page is very short).
  - **Never use `sed`/`awk`** for wiki pages — they break table formatting.
- **hot-topics.yaml patch requires exact indentation matching**: The `patch` tool's replace mode is extremely sensitive to whitespace. The YAML entries have multi-line structures (search_hints arrays, wiki_pages arrays) with specific indentation. Always `read_file` the exact section first, then patch with the exact text including indentation.
- **Enrich notes field after crawling**: When updating hot-topics.yaml, also update the `notes` field with key recent findings. This provides context for future crawls so you know what's been covered.
- **Enrich search_hints with latest terms**: Update `search_hints` to include newly discovered terms (model names, product names, Chinese keywords) found during the crawl.
- **Git push may fail without credentials**: Cron environments often lack GitHub credentials. The commit will succeed but push may fail. Always check push status and report if commit succeeded but push failed. Use `git log --oneline origin/main..main` to see unpushed commits.
- **web_search returns raw text blocks**: The `web_search` tool returns a large text block with metadata (e.g., "(16,093 chars result)"). Content is in the result body, not structured JSON.
- **read_file pagination on large files**: When reading hot-topics.yaml or other large files, use offset/limit to read specific sections. Re-read the full file before major edits if you've only seen a partial view.
- **Update both last_crawled AND log.md**: For traceability, always update hot-topics.yaml's last_crawled date AND write to wiki/log.md. Don't skip either.
