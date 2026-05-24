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

**Preferred approach — parallel subagent delegation:**
For 2-3 topics, delegate each to a `delegate_task` subagent in parallel. Each subagent receives the topic's `search_hints` and existing wiki page path. This is 2-3x faster than sequential web searches.

```python
# Pseudocode pattern for parallel research delegation
tasks = []
for topic in selected_topics:
    tasks.append({
        "goal": f"Research {topic['name']} using search_hints: {topic['search_hints']}",
        "context": f"Existing wiki page: wiki/concepts/{topic['slug']}.md\n"
                   f"Target: find developments from {last_crawled} to present\n"
                   f"Language: respond in Japanese\n"
                   f"Output: structured findings with source URLs",
        "toolsets": ["web", "file"]
    })
# Then delegate_task(tasks=tasks) and consolidate results
```

**Fallback — sequential web search:**
For each selected topic, use its `search_hints` for web research:
- Search Chinese AI sources (V2EX, Juejin, 36kr, Zhihu, WeChat media)
- Find recent developments, technical details, community reactions
- Cross-reference with existing wiki pages to avoid duplication

### 3. Create/Update Wiki Pages
- Check if page exists first: look in `wiki/concepts/`, `wiki/entities/`, and `wiki/pages/` (varies by topic type). **hot-topics.yaml `wiki_pages:` field provides the exact path** — use it directly rather than re-searching directories.
- Always `read_file` the existing page first to see current content AND verify the `updated:` date
- Compare search results with existing content: identify what's stale vs new
- **For updates: use `patch` (preferred)** — fuzzy matching handles indentation and table formatting. `patch` succeeds where full rewrites risk corruption. Use targeted `old_string` with enough surrounding context for uniqueness.
  - **Use `write_file` only when restructuring** (changing frontmatter schema, reorganizing sections, or the page is very short).
  - **Never use `sed`/`awk`** for wiki pages — they break table formatting.
- **Verify subagent updates** by reading the first 10 lines of the wiki page after subagents complete their work: check `updated:` date in frontmatter equals today's date. This catches silent failures where a subagent's `patch` or `write_file` didn't actually apply.
- New concept pages: `wiki/concepts/[topic-slug].md`
- Entity/model pages: `wiki/entities/[topic-slug].md`
- Product/tool pages: `wiki/pages/[topic-slug].md`
- Follow SCHEMA.md format
- Include: overview, key findings, Chinese sources, Japanese analysis
- Update `updated:` date in frontmatter

### 4. Update Tracking
- Edit `hot-topics.yaml`: set `last_crawled: YYYY-MM-DD` for processed topics
  - **For YAML edits — direct `patch` (preferred)**: Read the exact section with `read_file` at the right line offset, then call `patch()` directly (no need to wrap in execute_code). The fuzzy matching handles multi-line `notes:` strings and `search_hints:` arrays. Example:
    ```python
    # Or equivalently, call patch() directly from the agent tool
    patch(path=".../hot-topics.yaml", old_string="...exact text from read_file...", new_string="...replacement...")
    ```
    **Important**: Include sufficient surrounding context lines to ensure uniqueness. Read both the target section and ~3 lines above/below.
  - **`write_file` the entire file (fallback)**: Read it all, modify in Python (string replace or yaml lib), then write_file back. Safer when the section is very large or indentation is ambiguous, but risks accidental corruption on large files.
  - **Enrich `notes:` field with key recent findings**: Always prepend the new date-stamped entry before the old content. But also **manage notes field size** — when notes exceed ~500 chars or contain 4+ previous crawl cycles, trim the oldest entries and move that historical context to the wiki page's main body or a History section. Keep only the most recent 2-3 cycles in the YAML notes field.
  - **Update `search_hints:` with newly discovered terms**: Add model names, product names, Chinese keywords, and CVE IDs discovered during the crawl. New terms go at the end of the list (before `wiki_pages:`).
- Update `wiki/log.md` with crawl results
- Update `wiki/index.md` statistics:
  - **Summary table at top**: increment the concept/entity/page counts for newly created pages. The `コンセプト (概念):` row tracks `wiki/concepts/` files.
  - **本日更新 section**: add a `- ### [topic-name]` entry under the "本日更新" heading with a brief description of what changed (new page vs content update). Keep entries concise — one line per topic unless a major restructure happened.
  - **Check that the spacing and `|` alignment** in the summary table is preserved. Subagent patches to index.md frequently break pipe alignment or add stray `|` characters in headings.

### 5. Commit and Push

**Scope of files to stage:**
- Active-crawl touches: wiki/ pages, config/hot-topics.yaml
- Do NOT stage inbox/ files (those belong to crawl-and-triage pipeline)
- Minimum set: `git add wiki/ config/hot-topics.yaml`
- Full set if log/index also changed: `git add -A` (but verify with `git diff --cached --stat` first)

```bash
cd ~/ai-topics-cn
git add wiki/ config/hot-topics.yaml
git commit -m "active-crawl: topic1/topic2/topic3 YYYY-MM-DD update"
git push
# Verify: use unpushed commits if push fails
```

- Commit message format: `active-crawl: [topic1]/[topic2]/[topic3] YYYY-MM-DD update`
- Verify push success; report unpushed commits if push fails (`git log --oneline origin/main..main`)

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
- **Same `last_crawled` value across multiple topics → patch uniqueness failure**: When multiple topics were last crawled on the same day (common after a batch crawl), patching just `last_crawled: 2026-05-15` will fail with "Found N matches" even with ^3 lines of context if the surrounding YAML structure (added:/notes: layout) is identical. **Fix**: include a snippet of each topic's unique `notes:` content (which contains the topic slug) as part of the patch context. Easiest pattern: patch `notes:` AND `last_crawled:` together in one shot, using the notes text (unique per topic) as the unambiguous anchor.
  - **Also watch for mixed quoting**: The YAML file may have inconsistent quoting — some topics use `last_crawled: "2026-05-15"` (quoted) while others use `last_crawled: 2026-05-15` (bare). Always match the exact format by `read_file`-ing the section first. A quoted vs bare value counts as two different strings for uniqueness purposes but may still collide if the quotes are identical.
*(Notes & search_hints enrichment guidance now lives compactly in Step 4 above — refer there.)*
- **Git push may fail without credentials**: Cron environments often lack GitHub credentials. The commit will succeed but push may fail. Always check push status and report if commit succeeded but push failed. Use `git log --oneline origin/main..main` to see unpushed commits.
- **web_search returns raw text blocks**: The `web_search` tool returns a large text block with metadata (e.g., "(16,093 chars result)"). Content is in the result body, not structured JSON.
- **read_file pagination on large files**: When reading hot-topics.yaml or other large files, use offset/limit to read specific sections. Re-read the full file before major edits if you've only seen a partial view.
- **Update both last_crawled AND log.md**: For traceability, always update hot-topics.yaml's last_crawled date AND write to wiki/log.md. Don't skip either.
- **log.md prepend pitfall**: wiki/log.md uses `|` rows as entry separators, and the blank line at line 1 is identical across all entries. When using `patch` to prepend a new entry, matching just the header + blank line (e.g. `"|## [2026-05-21]...\n|"`) often finds 2+ matches because each entry starts with the same `|` separator pattern. **Reliable solution**: match the ENTIRE previous entry block — from its `##` header through ALL bullet points down to the start of its successor entry — as the `old_string`. This guarantees the match is unique regardless of entry count. Example: `old_string="|## [2026-05-21] active-crawl | Qwen/Doubao/ChatGLM deepdive\n|\n|### Wiki更新\n|- bullet 1\n|- bullet 2\n|- bullet 3\n|\n|### hot-topics.yaml更新..."` — the full previous entry's unique content anchors the match unambiguously. Then the `new_string` prepends the new entry + restores the old entry in one shot.
- **Subagent verification — two-part check**: Subagents self-report "updated wiki page" and "updated tracking" but silently fail on both. After subagents finish, verify TWO things:
  1. **Wiki page frontmatter**: Read the first 10 lines of each wiki page subagents claimed to update. Check `updated:` date equals today's date. A stale date means the patch didn't land.
  2. **hot-topics.yaml tracking**: Read the `last_crawled:` and `notes:` fields for each topic the subagent was supposed to update. Subagents frequently fail to update these even when wiki pages were updated correctly. You MUST perform this YAML update yourself — do not assume the subagent did it.
- **Subagent YAML frontmatter corruption**: Subagent `patch` calls to wiki pages can introduce stray characters (`|`, backticks, extra spaces) that break YAML frontmatter parsing. After verifying the `updated:` date (step 1 above), also check that lines 1-6 (between `---` markers) parse as valid YAML — notably that no line starts with `|` or contains unbalanced quotes. Repair with `patch` using the known-good structure from a sibling wiki page.
- **Subagent duplicate YAML keys**: When adding `search_hints:` or new frontmatter fields, subagents may write a SECOND `search_hints:` block instead of updating the existing one. This produces two YAML key definitions with different values, and the Hugo wiki renderer silently uses only one. If a patch on a YAML field doesn't seem to take effect, `read_file` the page and grep for duplicate keys. Remove duplicates with patch using surrounding context for uniqueness.
- **Context compaction**: Long sessions may trigger context compaction. The `todo` list is preserved across compactions — use it to track multi-step progress. The handoff summary reconstructs what happened, but file paths and exact text for patches may be stale (especially if the original `read_file` was paginated). After compaction, re-read the relevant YAML/wiki sections fresh before patching.
- **Pre-commit diff review for corruption**: Before committing, run `git diff --cached` and scan for common subagent-introduced corruption: (1) stray `|` characters in wiki page YAML frontmatter, (2) duplicate YAML keys like two `search_hints:` blocks, (3) broken pipe-aligned table rows in `index.md` where a subagent's patch misaligned columns or added/removed pipes, (4) `log.md` entries with `||` (double-pipe) from incorrect patch matching. Fix these before `git commit` — committed corruption is harder to unwind.
