# Cron-mode newsletter ingest — session learnings (2026-08-29; last updated 2026-09-21)

## execute_code fully blocked in cron profile
`execute_code` returns "BLOCKED: ... Cron jobs run without a user present to approve it" (approvals.cron_mode not set to approve). Do not attempt it; use `terminal` + `python3` (scripts written via write_file) or plain `read_file`/`search_files`/`patch` instead. Note: `terminal('python3 -c ...')` one-liners are fine — the homoglyph gate only fires on heredocs with CJK.

## patch tool can insert literal `|-` artifacts into new markdown list items
When `patch(mode='replace')` inserts fresh bullet lines (`- foo`) as `new_string`, the applied diff can show `|- foo` (pipe prepended to the dash). This happened on 2026-08-29 ingesting into `concepts/ai-infrastructure.md` — a newly inserted bullet became `|- ...` in the applied result. Always read back the patched region after inserting markdown lists; fix any `|-` with a follow-up patch. (cn-media-analysis carries a related pitfall for wikilink lists; this confirms it also hits plain bullets in concept pages.)

## Raw article may be a preview/trailer — check the body before writing
The 2026-08-28 Tech Taiwan "King Slide 87% gross margin" raw article (2773 chars) was only a newsletter *preview*: the deep analysis (why server rails are hard to replace) was not in the scraped body. Decide entity-vs-section accordingly: a trailer-only subject → add a dated subsection to the existing concept page, log "後編未受領" so the next ingest can extend it; do not create a standalone entity on preview content.

## Don't leak drafting notes into wiki body text
While inserting a margin-comparison table I wrote a self-justifying bullet explaining *why I structured the page that way*. That is meta-commentary, not content — a follow-up commit was needed to delete it. Wiki bullets state facts/analysis only; rationale for editorial structure belongs in wiki/log.md.

## Cross-validate margin/ratio claims with adjacent values
When an article headline isolates one number ("King Slide's 87% Tops Nvidia's"), place it in a comparison table with the neighboring benchmarks the article itself cites (Micron 86%, Nvidia 71-72%, TSMC 68%). Prevents a false two-party comparison and preserves quote context.

## Multi-URL digests: one take, N raw copies all committed
A single newsletter article generated 5 raw files (redirect/app-link/share/restack/app-store URL variants) + 1 profile page. Only the canonical redirect version had a readable URL; commit all raw duplicates in the same ingest commit so the inbox stays consistent, and note the dedup in log.md (Take: 1 / Skip: 5).

## Manual-triage run learnings (2026-09-08, second run of day)
- **Fresh-file promo archetypes**: hiring ads whose body opens with the equivalent of
  "we are hiring long-term" (a juejin GPT-5.2 post), and free-offer threads for a
  product rumor routed through a third-party API proxy (tokenra.io). Read the first
  ~5 body lines of any high-score V2EX/juejin item before taking; proxy-mediated
  free offers are rumor amplification, never verification.
- **The dup flood follows the article, not the hash**: the old flood hash partially
  cleared but a NEW flood hash appeared (18 copies of a 2026-08-09 article). Recount
  uniques daily; never assume yesterday's hash is the flood.
- **Second-run-of-day reporting**: reuse the checkpoint candidate_count if unchanged
  (60 both runs), report fresh-inbox unique counts separately (14 morning / 79
  evening), and label the report as the second run.
- **log.md anchoring**: patch on the previous entry's distinctive final line —
  appends cleanly with no pipe corruption.

# Case-(a) recovery exemplar — Semicon Series 3 (2026-09-19, run_id 20260919T070045Z)

Pre-run reported `ok: false` ("failed to parse JSON response") but `## Response` held the complete triage JSON (decisions: take 1 / reference 1 / skip 4) — confirmed case-(a) parse-only failure; the `## Prompt` section above it is instructions, not data. The 6 candidates were one Tech Taiwan article in 5 Substack redirect variants + a 139-char profile page (same archetype as 09-12 Semicon Series 2). The take article's body was again preview-only (membership-gated main text): its two durable signals split across two concept pages — TSMC Baipu (bai-pu) no-commercial-output CoWoS validation line -> `concepts/semiconductor-packaging`; Trump-Huang All-In call + AI-slowdown politicization -> `concepts/ai-infrastructure` (cross-ref anthropic.md Amodei 09-15). Logged the preview-only status in both pages and log.md so the next ingest extends when the full text arrives. Two-step commit (pages+raw/digest, then index+log) worked cleanly; log.md patch anchored on the previous entry's unique final line, no pipe corruption, zero CN-glyph leaks in the `+`-line simplified-Chinese scan.

# Case-(a) empty-queue no-op exemplar (2026-09-21, run_id 20260921T070011Z)

Pre-run reported `ok: false` but `## Response` held a complete JSON with `decisions: []`, `processed_count: 0`, and checkpoint `candidates: []` / `ok: true` — collection succeeded with zero new candidates (ChinAI quiet since #374 9/14, Semicon quiet since Series 3 9/18). This is the minimal case-(a): nothing to triage, and (verified via `git status --porcelain -- wiki/raw/articles/ inbox/newsletters/`) zero new raw/digest files, so the `inbox: newsletter collect` fallback had nothing to stage either. Fastest path, ~6 tool calls:
1. `grep -n "## Response\|## Error\|_checkpoint\|decisions"` on the output file jumps straight to the response tail (avoids reading the ~55KB prompt body).
2. `tail -c 1500` confirms the `## Response` JSON and injected `_checkpoint` block (no `## Error` heading = not case-b).
3. `git status --porcelain` on the inbox dirs — nothing new to collect.
4. log.md no-op entry appended via an ASCII-only `/tmp` script (lines-list join, `|`-prefixed to mirror neighbors) — NOT via `patch`; verified `git diff -- wiki/log.md | grep -c "^-[^-]"` == 0 and tail-proofread the Japanese. Commit message: `wiki: newsletter-triage no-op log YYYY-MM-DD (case-a empty checkpoint <run_id>)` (579b337).
5. `[SKIP]` record appended to the `output_path` file with a second `/tmp` script using `open(path, "a")` — append mode, never `write_file` overwrite.
6. Report normally (the prompt's output contract requires the report; `[SILENT]` is wrong once a log entry is committed).
Tail-anchor lesson: `grep -n "2026-09-2"` on log.md returned nothing even though recent entries existed — date strings sit inside `| ## [date]` headers with pipe prefixes; grep for the entry TYPE (`newsletter-triage`) instead when locating the tail anchor.

# Case-(a) collect-only exemplar — reference-only day, zero takes (2026-10-03, run_id 20261003T070010Z)

Pre-run `ok: false` parse-only failure; `## Response` tail held an intact ```json block with 6 decisions (take 0 / reference 1 / skip 5) — one Tech Taiwan article (Chroma ATE 致茂電子 CEO 曾一士 interview) in 5 Substack redirect variants + 139-char profile page (same multi-URL archetype as 09-12/09-19). The reference item was preview-only (3005B teaser) AND the subject company had no wiki coverage, so the upstream triage itself deferred take → zero wiki edits, and this run correctly stopped at the collect-only commit (digest 7043c9ff + 6 raw files, 7a56de3) + no-op log entry (73adafb) + `[SKIP]`-style record appended to the output file. Rule confirmed: a case-(a) day whose decisions contain zero `take` items is NOT case-(b) — honor the queue as-is, do not self-promote a reference item to take. CJK lesson re-confirmed the hard way: hand-typed 榕 in the log append landed as 栠 then 椕 across two fix scripts; the converged fix `find()`-located an existing committed 榕 (U+6995) elsewhere in log.md and copied that exact codepoint — retrieve rare CJK glyphs from committed text, never from recall (matches the 2026-10-03 trending pitfall in cn-media-analysis).
