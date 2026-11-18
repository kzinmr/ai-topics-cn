# Active-crawl run learnings — 2026-11-18 (Kimi K3.1 Pro / Doubao SuperCLUE-Office run)

New register file (per SKILL.md: if the main register append is risky, add a
dated file under references/). Newest facts at top.

## Selection

- kimi (high/deepdive, lc 8/31) + doubao (high/deepdive, lc 8/31) +
  mcp-chinese-tools (medium/laterals, lc 8/12). 3-day rule met for all.
- qwen (lc 9/4) deferred by the high-2 cap — flagged 次回候補 in log.md.
- monitor-policy topics (censorship-bypass, china-gpu-restrictions,
  cursor-china-adoption) excluded by policy, not by the date rule.

## Research channel (Tier 2B/3, no web_search)

- daily_digests 11/10-17 + inbox frontmatter `date:` verification was the
  whole evidence base. Two durable takes survived:
  (1) Kimi K3.1 Pro on DigitalOcean Serverless Inference (juejin 11/11,
      DigitalOcean official account, preview-only body) — single-source
      未検証, cross-consistent with entities/kimi-moonshot.md's 11/11 entry;
  (2) Doubao Work #1 on SuperCLUE-Office Oct run @85.33 (juejin 11/11,
      preview-only) — single-source 未検証.
- The 「轻量化复刻大模型 / KIMI K3」 series (罗西的思考, 8 posts 11/10-17)
  passed the date check = NEW content (not recollection) — recorded as a
  traction signal, not as facts.
- Satire三千万足矣 (hash 5c8e3320, dated 7/27) and Qoder-compare (40fc748f)
  recrawl daily — saturation-recollection skips, already tagged 09-27.

## Failures / fixes this run (both cost extra rounds)

1. **log.md double-prepend**: the "||" cleanup script recomputed the region
   END with `c.find(next_header, i)` where `i` was the PRE-fix index, so the
   slice boundary landed one entry early and the fix script DUPLICATED the
   new entry (HEAD count 2, caught by the `assert count==1` guard, which is
   why it never shipped). Rule: when a splice script both reads and writes
   the same buffer, recompute ALL anchor indices from the CURRENT `c` right
   before each find(), or do the whole fix in one pass. Also: the original
   prepend used `("|" + l if l else "|")` which, combined with an already
   pipe-prefixed source body, emitted "||" lines — the body string must be
   authored pipe-FREE, single prefix applied once.
2. **Slug-anchored YAML update silently no-op'd while printing "updated"**.
   The section bound `content.find("\n  - slug: ", idx+10)` matched a
   `  - slug:`-looking line INSIDE the same topic? No — the real culprit:
   `idx+10` was too short a skip for the pattern's leading 2 spaces,
   anchoring `nxt` before `lp`, and an earlier draft's bounds slicing
   returned the ORIGINAL section unchanged (replace with identical text),
   so the write was a byte-identical no-op — yet the script had no
   post-condition and printed success. Detected only because the
   blob-vs-base diff showed ZERO yaml changes in the tracking commit.
   Rule (extends SKILL.md "verify with content.count()"): the post-write
   asserts `c.count("last_crawled: TODAY")==N` and
   `c.count("YYYY.MM.DD更新")==N` MUST run over the FINAL buffer and be
   paired with a `diff /tmp/ht_presession.yaml config/hot-topics.yaml`
   showing exactly 2 changed lines per topic. Copy a presession snapshot
   first (`cp config/hot-topics.yaml /tmp/...`) — the working tree is
   always sibling-dirty, so a fresh snapshot is the only honest baseline.
   Recovery was cheap (re-run v2 with correct bounds, new commit 8fab129).

## Commits

- f13c742 pages (kimi.md 11/18 section, doubao.md 9g) — sibling's uncommitted
  9/16-9/27 sections rode along (disclosed here per SKILL.md section 0).
- c3f5df1 log.md + index.md (tracking commit shipped yaml UNCHANGED due to
  failure #2).
- 8fab129 hot-topics.yaml tracking retry (kimi/doubao/mcp-chinese-tools,
  notes prepend + last_crawled, closing-quote per-topic assert green).
- Push clean to main.

## Pre-existing (not touched)

- mcp-china topic `notes:` line lacks its closing quote (known
  pre-existing break; left alone per pre-existing-lint pitfall).
- index.md 最終更新 had drifted to 2026-10-05 (other pipelines don't touch
  it); bumped to 2026-11-18 with the new 本日更新 section.
