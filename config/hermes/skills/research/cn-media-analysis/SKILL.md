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
- **`execute_code` blocked in cron mode**: Cron jobs run without a user present, so `execute_code` (which allows arbitrary subprocess calls) is blocked by the approval gate. Use `terminal` with `python3 -c` for JSON parsing, or `read_file` + `search_files` to inspect checkpoint data. The `execute_code` tool will return `status: pending_approval` and never complete in a cron context.
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
