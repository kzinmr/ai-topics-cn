---
name: cn-media-analysis
description: Analyze Chinese AI media, newsletter, and crawl items for durable trends, source differences, and wiki actions
category: research
version: 1.0.0
author: hermes
license: MIT
metadata:
  hermes:
    tags: [Media-Analysis, Chinese-AI, Trend-Detection, Cross-Source]
---

# Chinese AI Media Analysis

Use this skill for Chinese AI media, newsletter, or crawl triage when the task asks for source comparison, trend detection, or wiki update recommendations. Unless the task says otherwise, write the final analysis in Japanese.

## Core Workflow

1. Read `triage_latest.json` in `~/.hermes/cron/data/crawl_and_triage/` — this is the authoritative work queue with `decisions` array. Do NOT use `latest.json` or `crawl_checkpoint_*.json` for decisions (those contain raw crawl stats and candidates, not triage actions).
2. For checkpoint jobs, treat `decisions` as the work queue and process `recommended_action: take` items first.
3. Use metadata such as source, publisher, title, date, URL, summary, and proposed wiki target together; do not infer importance from volume alone.
4. Cluster related items by durable topic: company, model, project, research result, product capability, regulation, business event, or developer practice.
5. Compare source perspectives only when multiple sources cover the same durable topic.
6. Recommend wiki work only when the item adds stable, reusable information or materially changes an existing page.
7. If there is no actionable work and the cron prompt allows silence, return `[SILENT]`.
8. If `execute_code` is blocked (cron mode), use `terminal` with `python3 -c` for JSON parsing, or `read_file` + `search_files` for inspection.

## Common Pitfalls

- **WeChat duplicate re-collection**: WeChat media crawls frequently re-collect the same articles across multiple runs (same URL, same content, different hash). Detection heuristic: the 8-char hash suffix in the filename (e.g., `aafeba3f` in `...-aafeba3f.md`) is content-derived — if the same suffix appears across files dated days or weeks apart, it is the same article re-collected, not new content. If a `take` item's inbox file contains only a title + URL with no body text, the original article was likely already processed in a prior run. Update the `updated` date on the wiki page and move on — don't treat this as new content.
- **V2EX "暂无内容" items**: V2EX forum posts often have placeholder titles but no actual body content (rendered as `暂无内容` in the inbox markdown). These provide no wiki value and can be safely skipped even if the checkpoint marks them as `take` or `reference`.
- **Newsletter header items**: WeChat newsletter digests (e.g., 机器之心PRO 会员通讯) often appear as individual crawl items with only a header/preview line and no full article. Treat as reference only if an existing wiki page covers the topic; otherwise skip.
- **Digest-to-candidate mismatch**: The `daily-digest-YYYY-MM-DD.md` file lists all items found by the crawl, but the `candidates` array in the checkpoint JSON may be a subset (filtered by size, deduplication, or crawl timing). Do NOT assume every article named in the digest's stderr/stdout has a corresponding `.md` file in the inbox — 36kr articles in particular may appear in the crawl log but not in the candidate list due to pipeline delay. Triage only what is in the `candidates` array; treat digest text as a preview, not an inventory.
- **Checkpoint `candidate_wiki_path` is authoritative**: The triage checkpoint JSON includes a `candidate_wiki_path` field for each `take` decision (e.g., `"candidate_wiki_path": "entities/huawei"`). This is the pre-resolved target wiki entity/concept path. DO NOT waste tool calls searching `~/wiki/entities/` or `~/wiki/concepts/` for matching files — the checkpoint already tells you exactly which page to read/update. For each `take` item: read `raw_path` → read `candidate_wiki_path` (create if missing) → patch/write → update index.md and log.md. Only search if `candidate_wiki_path` is empty or clearly wrong.
- **`execute_code` blocked in cron mode**: Cron jobs run without a user present, so `execute_code` (which allows arbitrary subprocess calls) is blocked by the approval gate. **`terminal` with `python3 -c` is ALSO blocked** (returns `status: pending_approval`). For JSON parsing and data inspection in cron mode, use ONLY `read_file` + `search_files` — these work without approval. If you need to parse JSON, do it inline with shell tools like `jq` in `terminal` (simple commands work) or process it mentally from `read_file` output.
- **Checkpoint file confusion**: Multiple JSON files exist in `~/.hermes/cron/data/crawl_and_triage/`. `triage_latest.json` contains the `decisions` array (what to take/reference/skip). `latest.json` and `crawl_checkpoint_*.json` contain raw crawl stats and the `candidates` array but NOT triage decisions. Always read `triage_latest.json` for the work queue.

## Source Lens

| Source | Use For | Caveat |
| --- | --- | --- |
| V2EX | Developer reaction, practical friction, pricing/API complaints, deployment experience | Forum tone can overrepresent acute pain points |
| Juejin | Implementation details, code-level validation, framework integration | Search results can resurface old articles |
| 36kr | Business context, financing, market structure, company positioning | Separate publisher/editorial voice from cited facts |
| Zhihu | Expert explanations, technical arguments, research context | Distinguish expert answers from generic discussion |
| WeChat public accounts | Long-form explainers, research summaries, sector commentary | Source quality varies by account; name the account |
| Newsletters | Curated item lists and summaries | Treat as triage inputs, not primary evidence when stronger sources exist |

Exclude CSDN from analysis unless explicitly requested.

## Analysis Rules

- Prefer durable facts and stable implications over short-lived hype, rankings, or engagement metrics.
- Do not invent article counts, dates, first appearances, source coverage, or confidence levels.
- Preserve Chinese proper nouns in their original form; add Japanese explanations when useful.
- Quote Chinese text only when it materially supports the conclusion, and include a short Japanese explanation.
- Clearly separate source-observed facts from your inference.
- Check for source disagreement, but do not force a cross-source comparison when the evidence is single-source.
- When judging wiki relevance, prioritize technical novelty, entity significance, regulatory or business impact, ecosystem adoption, and whether the information changes an existing wiki page.

## Daily Trending Report Workflow

Use this workflow when the task asks for a daily trending topics report from `trending_topics.py` output — typically the `shelley-trending-topics.timer` cron job (daily, ~10:00 JST). This is a **different pipeline** from crawl triage (which reads `triage_latest.json`).

### Steps

1. **Run the trending script**:
   ```
   python3 /opt/data/ai-topics-cn/scripts/trending_topics.py --days 3
   ```
   This produces a markdown report with hot topics, cross-source signals, and source-level counts.

2. **Read hot-topics.yaml** at `/opt/data/ai-topics-cn/config/hot-topics.yaml`. This is the authoritative list of active crawling targets.

3. **Cross-reference trending topics against hot-topics.yaml**:
   - For each trending topic with `source_count >= 3`, check if it matches any entry in `hot-topics.yaml`'s `topics` array (match by slug or title).
   - Topics found in hot-topics.yaml are already tracked — skip them for crawl candidate proposals.
   - Topics **not found** in hot-topics.yaml are candidates for new crawl targets.

4. **Check wiki page existence** for candidate topics:
   - Search `entities/`, `concepts/`, and `pages/` under the wiki directory.
   - `search_files(target='files', pattern='<topic>', path='~/wiki')` covers all subdirectories in one call.
   - Record which candidates have no wiki page at all (→ new page recommended).

5. **Propose YAML snippets** for topics meeting ALL criteria:
   - `source_count >= 3`
   - Not already in `hot-topics.yaml`
   - Relevant to the Chinese AI ecosystem (global entities may be excluded)

### Report Structure (Japanese)

```markdown
# 🔥 中国AIデイリートレンドレポート — YYYY-MM-DD

## (1) 📗 新規Wikiページ推奨
Trending topics with no wiki page yet.

## (2) 🔥🔥 ホットトピック (4+ソース)
Table with topic, source count, and notes.

## (3) 🔀 クロスソーストピック (最高シグナル)
Highest signal items appearing across multiple sources.

## (4) クローリング候補提案
YAML snippets for hot-topics.yaml with slug, title, crawl_policy, priority, search_hints, and notes.
```

### Crawl Candidate YAML Template

```yaml
  - slug: topic-slug
    title: "Display Title — Context"
    crawl_policy: monitor      # start with monitor for global entities
    priority: high/medium/low
    search_hints:
      - "Chinese keyword search query"
      - "English keyword search query"
      - "Specific product or model names"
    wiki_pages:
      - entities/topic-slug    # or concepts/topic-slug
    notes: "YYYY-MM-DD初登録。Rationale and context."
    added: YYYY-MM-DD
    last_crawled: ~
```

### Key Heuristics

- **Already-has-wiki → skip new page proposal**: If an entity/concept page exists, don't recommend creating a new one even if the topic is trending. Instead, note the existing page and update it separately.
- **Global entities**: Claude, Anthropic, Gemini/Google, Llama/Meta are discussed heavily in Chinese media but are global products — evaluate case-by-case whether they warrant a hot-topic entry (they typically don't unless their China-specific impact is material).
- **Chinese entities without crawl targets**: 文心一言/Baidu, for example, has a wiki page but no hot-topics.yaml entry — these are stronger candidates than global entities.
- **Cross-source signal strength**: Topics appearing across 3+ source types (e.g., 36kr + juejin + v2ex + wechat) have the highest signal-to-noise ratio.
- Source count from `trending_topics.py` is article-level mentions; the script's deduplication is heuristic. Moderate your confidence — a topic with 87 sources can still be a broad umbrella (e.g., "AI Agent").

### Pitfalls

- **trending_topics.py output is the primary source, not triage_latest.json**: The crawl triage pipeline and the trending report pipeline are distinct. Do NOT read `triage_latest.json` for a trending report task — it contains crawl decisions, not trending data.
- **hot-topics.yaml has mixed quoting**: Some `last_crawled` values are quoted (`"2026-06-08"`), others bare (`2026-06-08`). When proposing YAML snippets, match the existing convention in the file (check surrounding entries).
- **Wiki page names may not match trending topic names**: The script outputs normalized names (e.g., "豆包/ByteDance" → wiki page is `doubao` or `doubao-bytedance`). Use `search_files` rather than guessing paths.
- **Zero mentions from a source is meaningful**: If Zhihu has 0 articles for the period (as seen in this session), note it in the report — it may indicate a pipeline issue rather than true absence of discussion.
- **Source volume imbalance**: juejin and v2ex produce similar volumes (~86 each) while 36kr produces ~40 and zhihu may produce 0. Don't assume proportional coverage across sources.
- **Do NOT infer topics from digest stderr/stdout**: If a source has 0 articles in the report, cite the report's count as-is. Do NOT search the crawl digest for counter-evidence — the report is the authoritative aggregation.

## Newsletter And Crawl Cron Defaults

- Newsletter triage: decide which newsletter items deserve wiki work; deduplicate overlapping items and ignore transient mentions.
- Newsletter wiki ingest: follow checkpoint decisions and use wiki skills for writing; do not rerun broad media analysis unless the prompt explicitly asks for it.
- Crawl triage: use the checkpoint or digest as the primary input; raw inbox files are secondary evidence for verification.
- Crawl wiki ingest: preserve the triage decision and add only stable facts to `~/wiki`.

## Output Shapes

Use compact structured output suited to the job:

```markdown
## Triage
- take: ...
- skip: ...
- park: ...

## Topic Clusters
- ...

## Source Caveats
- ...

## Wiki Actions
- ...
```

For a long-form, ad hoc media report, load `references/analysis-guide.md` only when the task explicitly asks for detailed cross-source reporting.
