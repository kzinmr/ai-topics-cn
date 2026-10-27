# Case-(b) [SKIP] record append to output_path — escape hygiene (2026-10-04)

Context: 2026-10-04 newsletter-triage cron delivered the wiki-entity-upgrade skill body
instead of its own prompt, plus a pre-run `ok:false` parse error. The output file tail
showed a fully intact `## Response` JSON (`decisions: []`, checkpoint
`candidate_count=0`, `_checkpoint.ok=true`, run_id 20261004T070011Z) → case-(a) clean
empty-queue no-op, isomorphic to 09-17 / 09-20 / 09-21 / 10-02. FIVE isomorphic
instances now; when collection reports candidate_count=0, go straight to: log.md no-op
append → narrow commit → [SKIP] record to output file → report.

[SKIP] record append (the one variation from the 09-21 exemplar): the record was built
in PLAIN ASCII (English frame, `\uXXXX` escapes only for the short CJK title span
"Tech Taiwan Chroma ATE"). Converged first try, zero typo rounds. Audit via
`grep -nP` with hex escapes for CN-only glyphs on the appended tail came back clean.

Defect found INSIDE the upstream LLM response JSON (not our text): `summary_ja`
contained "モレワ**ー**チャップ" — the kataー (U+30FC) landed mid-word in
モア → confirmed katakana escape-typo surface affects even the upstream triage LLM's
own output. When quoting upstream summary_ja text in log entries, don't trust its
katakana verbatim; re-type the short span with verified escapes or paraphrase in
ASCII. Our own log append had the same class of leak (ワーチャップ) — the ASCII-frame
trick reduces but does not eliminate the katakana vector; the codepoint audit remains
the gate, not the eye.

Commit: 2ebd5ce (log.md only, single commit — no page/index changes on a no-op day).

## Case-(a) empty-queue no-op instance 2026-10-27 (run_id 20261027T070014Z, twenty-second instance)

NOTE (2026-10-27): this file was absent from the skill working tree before this run
(prior sessions' content for it was never committed). The section below was appended
fresh onto an empty file. The original 10-04 case-(b) [SKIP]-append exemplar body, if
referenced by SKILL.md, is not present here and must be recovered from git history of
the skill directory.

Pre-run script said ok:false (parse failure) but ## Response held the valid empty-queue JSON = case-(a).
Collect file 394-byte boilerplate, newest digest 2026-10-23 already committed, zero strays
(find -newermt 2026-10-26 empty + git status clean for inbox/newsletters, wiki/raw/articles).
The trending-topics job had fired earlier the same day (c2f2c8e, 17th zero-volume) so today's
wave is NOT collect strays.

LEAK-BIRTH FINGERPRINT (kanji-homoglyph family, same as 10-26): build script #1 shipped the
English placeholder 'digest is already ...' clause instead of the intended JP token, and its
replacement token was 2 chars SHORT of the intended 6-char phrase (dropped leading 2 chars +
the sumi suffix). The codepoint inventory passed it because each surviving char was valid --
only the flowing-prose read caught it. FIX CONVERGED IN 2 ROUNDS via: probe (find English
anchor, repr + per-char hex+unicodedata.name dump), then replace the WHOLE clause span in one
shot with the phrase built by chr() tuple concatenation + per-token count==1 asserts BEFORE
writing. LESSON: when a token has multiple simultaneous defects (short-phrase + missing
suffix), replace the entire span at once, never char-by-char.

Post-commit blob verification (verify script over appended region only): all good tuples
count>=1, CN denylist (incl. 0x7741) zero hits, VERDICT PASS. Commit 378d910 (log.md only,
git diff deletions count == 0 append-only invariant held). Katakana all first-try via chr()
concatenation -- katakana protocol holding; residual vector remains the JP-kanji phrase
completeness, caught only by prose readback.
