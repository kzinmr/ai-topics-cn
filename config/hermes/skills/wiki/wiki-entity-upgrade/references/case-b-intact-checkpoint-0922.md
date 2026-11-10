# Case-(b) intact-checkpoint fallback — worked instance 2026-09-22 (ChinAI #375)

## Variant 2026-09-26 — case (a) reference-only (candidates present, zero takes)

Pre-run `ok: false` was a parse-only error; `## Response` held intact decisions (case a). Checkpoint 20260926T070006Z (ok: true): 6 candidates = ONE Tech Taiwan (cwnewsroom) message — 5 Substack link variants of the same preview-only article (1041 chars, body paywalled; Jonah Cheng CIO interview: midterms black-swan thesis, TSMC-vs-Intel packaging "pseudo-proposition", Huang "feint") + 139-char profile page. Triage: reference 1 (semiconductor-packaging sentiment signal) + skip 5. Zero takes → no wiki edits. Outcome: collect-only commit 47bf850 (digest + 5 new raw; profile raw was an already-tracked dirty re-fetch → left unstaged) + no-op log a1fa93d. Isomorphic to the 09-17/09-20/09-21/09-25 no-ops; only difference: candidates existed but all resolved to reference/skip. Typo lesson (5th fix-cascade confirmation): hand-written `\uXXXX` Japanese in the /tmp append script leaked 5 defects in 2 bullets; converged in 2 rounds via extract-anchor protocol (anchor on unique ASCII substrings, rebuild whole lines from short latin+escape fragments, assert count==1, verify zero `-` lines in git diff).


Isomorphic template for a newsletter-triage cron run where the pre-run script reports
`"ok": false, "error": "failed to parse JSON response from newsletter-triage output"`.

## Diagnosis sequence (run in this order)

1. `wc -c` + `tail -c 6000` the cron `output_path` file (`~/.hermes/cron/output/<job>/<ts>.md`).
   The file is prompt + checkpoint + `## Response` + `## Error`; the triage JSON (if any) sits
   AFTER the long prompt, so read the TAIL.
2. Check the tail's `_checkpoint` block: `ok: true` + populated `candidates` = collection survived.
3. Check `## Response` / `## Error`:
   - Parseable fenced json with a `decisions` array -> case (a), recover the decisions and work the queue.
   - Empty `## Response` + `## Error: RuntimeError: HTTP 503: Local LLM server is busy` ->
     case (b), the LLM never answered; there is NOTHING to recover even though the checkpoint is intact.
4. `git ls-files --error-unmatch <digest> <raw>` to confirm the checkpoint's files are untracked
   new collection output (not already committed by a prior run).

## Actions in case (b) — collect-only, no self-made takes

The injected triage prompt says "Do NOT edit wiki files in this job"; the ingest prompt forbids
substituting your own take decisions for the failed LLM. So:

1. Commit ONLY the surviving collection files, narrow scope:
   `git add inbox/newsletters/ wiki/raw/articles/ && git commit -m "inbox: newsletter collect YYYY-MM-DD (case-b 503; ... checkpoint <id> intact, triage LLM failed — defer takes to next authorized run)" && git push`
   (Multi-URL digest dedup applies — one digest email scraped ~13 raw files here.)
2. Append a case-(b) no-op entry to `wiki/log.md` via the `/tmp` append-script pattern
   (ASCII-only, `|`-prefixed lines mirroring neighbor style, `|-\u3000` bullets).
   Gate: `git diff -- wiki/log.md | grep -c "^-[^-]"` must be 0.
3. Append a `[SKIP]` JSON record to the cron `output_path` file in APPEND mode. A
   `terminal` heredoc `python3 - <<'EOF'` passes the tirith homoglyph gate as long as ALL CJK
   inside is `\uXXXX`-escaped — no separate write_file'd script needed for this.
4. Commit log.md separately (`wiki: newsletter-triage case-b no-op log ...`).
   Two-commit discipline: collection commit first, then log commit.

## Typo-fix convergence log (why 3 rounds happened)

The log-append script's long Japanese lines built from `\uXXXX` escape runs produced garbage
glyphs the run couldn't see at write time: (wrong glyph) instead of 忘録, (wrong) for 予め,
(garbage) for 欗→延期-related word; then fix round 1 rebuilt line 1 OK but left another garbage
glyph in line 3, and a header replace left a stray fullwidth comma at the join.
Round 2/3 rebuilt each line from SHORT ASCII+single-escape fragments with extract-anchored
`s.find()`/slice replacement — converged. Prevention rule now in SKILL.md pitfall (cascading
repairs, items 5–6): short-fragment line construction + `repr()` the join boundaries.

## Report shape delivered

Standard output-format block, Take/Reference/Skip all 0 with "(triage LLM failed, no decisions
generated)" parenthetical, plus a case-(b) diagnosis paragraph, the two commit hashes, and top
topics from the digest's section headers (ChinAI #375 Pacing-the-Frontier critique, Trump AI
safety dismissal, Chip War #280 re-inclusion).
