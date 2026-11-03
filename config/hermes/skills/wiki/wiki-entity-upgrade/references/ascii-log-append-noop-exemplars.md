# Newsletter-triage no-op run exemplars

## Fingerprint checklist (case-(a) empty-queue no-op — run these BEFORE writing anything)

1. `## Response` in the output_path file holds a parseable ```json block with
   `decisions: []` and `checkpoint_run_id` -> case-(a), honor as work queue.
   (If `## Response` is empty / HTTP 5xx body -> case-(b): collect-only or
   [SILENT] per job type, NEVER invent decisions.)
2. Collect file `~/.hermes/cron/data/newsletter/newsletter_collect_<run_id>.json`
   is the 394-byte boilerplate (ok:true, processed/skipped empty).
3. `ls -t inbox/newsletters/ | head` — newest digest predates today AND is
   already committed (`git log -- <digest-path>`).
4. `find inbox/newsletters wiki/raw/articles -newermt <today> -type f` -> empty.
5. `git status --short -- inbox/newsletters wiki/raw/articles` — no `??` strays
   (if strays exist and no `inbox: newsletter collect` commit covers them,
   do the catch-up collect commit FIRST — see counter-example 2026-10-07).
6. `git log --oneline -5` — no today's newsletter ingest commit yet; a same-day
   trending commit is NOT a collect stray (different timer, fires ~1h apart).

All six pass -> the entire run is: log.md no-op entry + [SKIP] record + single
narrow log.md-only commit. Do not read triage_latest.json, do not crawl inbox.

## Worked instance: 2026-10-29, run_id 20261029T070059Z (24th isomorphic)

- Pre-run script: `ok:false, "failed to parse JSON response"` — red herring;
  `## Response` held clean empty-queue JSON (case-a).
- Checklist: collect 394-byte OK, latest digest 2026-10-23 (f2253083, committed)
  OK, -newermt empty OK, git status zero strays OK, today's trending commits
  (6ba4c66, f7b92c1) from earlier wave — not strays OK.
- log.md append: ASCII-frame script, `|`-prefixed lines, `|-\u3000` bullets,
  run_id header `|## [2026-10-29] newsletter-triage | shelley-newsletter-triage.timer`.
- Defect round 1 (3 defects, one fix script): stray U+6D2A tail after the
  COMMITZUMI token, `commit.` stray period, missing space before particle DE.
- Defect round 2: U+6B20+U+7559 (a valid-looking but nonexistent word) ->
  U+6EDE U+7559 (churyu/tairyu) — caught only by the flow read.
- Commit afe5bf2 (log.md only, 0 deletion lines) + [SKIP] record appended to
  the output file with its own 2-round fix.

## Failure modes that cost rounds THIS run (memorize)

| Mode | Symptom | Prevention |
|------|---------|------------|
| `r"...\u30d0..."` raw-string grab pattern | `AssertionError: grab failed` though token present | single-backslash `\uXXXX`, NO r-prefix, in regex patterns |
| CJK char in script IDENTIFIER | `SyntaxError: encoding problem: ascii` at launch | pre-run scan every line for ord>127 incl. identifiers |
| `git checkout -- wiki/log.md` before fix script | fix dies on `rfind(HEAD)` — own uncommitted entry wiped | re-run append.py && fix.py; checkout only for sibling damage |
| Double-defect token (dup char + homoglyph) | partial fix leaves the homoglyph, passes 2nd tail read | fix the WHOLE token in one extracted-string replace, re-probe per-char hex |

## Isomorphic-instance lineage (latest)

10-22 b0cd299, 10-23 008b438, 10-24 27ef876 (case-b 503 variant),
10-25 32703b8, 10-27, 10-28 aed54bd (23rd), 10-29 afe5bf2 (24th).
The 394-byte collect file + latest-digest-2026-10-23 + zero-strays triple is
the standing zero-mail-day fingerprint.

## 2026-11-03 (run_id 20261103T070056Z) - 29th isomorphic empty-queue no-op

Case-(a): pre-run ok:false parse-only, ## Response JSON intact with decisions: []. Collect file 394-byte boilerplate, no new digest since 2026-10-23, -newermt 2026-11-03 and git status both zero strays, trending job fired earlier same day (520b7a1). ASCII-frame log append with chr()-tuple katakana + denylist + good-tuple asserts + flow read.

NEW leak fingerprint - valid-but-wrong HIRAGANA word via wrong tuple: the tsuzuku counter/particle word shipped in a wrong 3-char hiragana form (tsu+gi instead of i+go+to) - all valid hiragana, invisible to the CN denylist, caught by the tail prose read. This extends the 10-25 katakana-shortening family to hiragana: build hiragana counter/particle words via full chr() tuples with a per-char unicodedata.name() dump. Also leaked: a copula splice (extra copula tail appended after a nashi phrase) and the completed/sumi kanji U+6E08 mis-shipped as the rare water-name kanji U+6E1F - all three fixed in one probe+fix round (within the 2-round budget), then the flow read flagged awkward spacing, cleaned by one final full-line patch quote. Grab-of-committed-form failed because the previous (11-02) entry carried no such token - probe grab targets for existence before relying on copy-derivation. Converged: log-only narrow commit 28b11fd, [SKIP] record appended to output_path file. Sibling dirty working tree carried 09-04-era v2ex files unrelated to this run - left alone.
