# Strict-JSON crawl-triage learnings - 2026-11-11 MORNING run (run_id 20261111T090222Z)

Pre-run ok:false "failed to parse JSON response from crawl-triage output". `## Response`
EMPTY; `## Error` = "RuntimeError: Response truncated due to output length limit".
=> NEW case-(b) error subclass: OUTPUT-LENGTH TRUNCATION (distinct family from HTTP 5xx
and context-length-exceeded). Fast discriminator unchanged: empty `## Response` = case (b).
Injected tail checkpoint INTACT (ok:true, 60 candidates) - but job contract is strict-JSON
triage-execution (no wiki edits, no self-made takes), so decisions: [] returned, zero repo
writes, no log append.

Checkpoint fingerprint identical to the permanent norm: 60 -> 8 unique (53x aafeba3f
2017-12-06 sogou recollection + 7x V2EX "(暂无内容)" placeholder bodies, stale dates
2026-04-19..07-28). Zero durable takes possible.

Fresh-day inbox scan (find -newermt 2026-11-10): today's juejin files are ALL ~500-700
byte preview-only shells (EditVid, Doubao office-agent ranking, LLM conformer, plus known
recollections: Codex/Jev promo 2026-09-23 score 87, Pi 2026-08-15 score 289, Superpowers
uninstall 2026-07-16 = saturation recollection). Preview-only with no bodies => clean skip
wholesale per the no-scraped-bodies hype-cluster rule.

No new CJK leak classes (decision-side only; returned JSON ASCII-escaped, flow-read once).
