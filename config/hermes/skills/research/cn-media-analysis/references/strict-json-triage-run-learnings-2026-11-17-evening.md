# Strict-JSON crawl-triage run learnings — 2026-11-17 evening

run_id 20261117T210140Z, output 2026-11-17_21-12-13.md, 29th isomorphic skip-only run.

## Fingerprint (unchanged, no investigation needed)
- Pre-run `ok:false` parse error; `## Response` tail = ONLY the missing-skill banner
  (`semantic-article-grouping` — DELETED skill, banner is permanent, do not hunt it).
  No ```json block => case (b) for the response side, BUT the injected tail `_checkpoint`
  is INTACT (ok=true) => strict-JSON contract job: emit decisions from own triage,
  ZERO repo writes.
- Checkpoint: 60 candidates -> 8 unique via hash-dedupe one-liner.
  53x wechat aafeba3f (2017-12 saturation recollection) + 7x v2ex.
- All 7 v2ex unique files = `(暂无内容)` body, date 1970-01-01, score 0/None,
  filenames dated 2026-04-19..2026-07-28 (stale re-queue, not fresh-day).
  Titles: Openai forum abuse report, deep research quality, GPT-6 release-wait,
  Codex reset promo, Codex App SSH remote, cheap-GPT ban, plus status.
  Zero durable facts => take 0 / ref 0 / skip 8 (7 unique v2ex + 1 aafeba3f cluster).
- Today's durable topics already committed by earlier waves
  (active-crawl dba4bea/9b44d20, trending 4c9f7cf, newsletter 623b4b1) => no overlap risk.

## Verdict
Clean skip-only no-op. No log.md append (triage-execution job, JSON-only contract —
per 11d rule). No commit. Report raw candidate_count=60, judge on deduped 8.

## New leak sites this run
None — report built via write_file to /tmp + read_file proof; flow-read clean first try.
