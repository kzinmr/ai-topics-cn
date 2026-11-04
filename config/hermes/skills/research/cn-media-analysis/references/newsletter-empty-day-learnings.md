# Strict-JSON Newsletter Empty-Day No-Op — Per-Run Learnings Register

Append-only. Newest dated section at the bottom. Append via ASCII /tmp script with
`io.open(path,'a')` + double-append guard ONLY — never write_file/skill_manage write_file
on append-only files (whole-file overwrite incident class, 2026-10-16 / 2026-10-21).

## 2026-11-01 — run_id 20261101T070037Z (empty-day no-op, clean delivery)

Facts verified pre-run (the contracted two-point check):
- `wc -c ~/.hermes/cron/data/newsletter/newsletter_collect_20261101T070037Z.json` == 394 (boilerplate variant).
- `ls -t ~/ai-topics-cn/inbox/newsletters/ | head` latest = 2026-10-23 — no new digest.
Outcome: case-a no-op, decisions=[], processed_count=0, no repo writes, no commit.

New leak classes this run (all in the EXPECT side or fix-script hygiene, vals clean):

1. SERIAL hiragana-expect-typed-as-katakana (the dominant class for this run type).
   All four whole-sentence put() asserts fired because hiragana copula tails were
   hand-typed from recall in katakana codepoints:
   - でした = U+3067 U+3057 U+305F — I typed U+30C7 U+30B7 U+30BF (t-ta confusion:
     した U+3057 U+305F shipped as U+30B7 U+30BF, a valid katakana シタ string).
   - です = U+3067 U+3059 — same class.
   - ノーオペレーション: U+30DA Pe — typed U+30D4 Pi (valid-katakana, tuple-blind).
   The vals were PERFECT every time (pitfall 11e(i), serial mutation). The run burned
   4 rounds fixing expects one-per-sentence before changing strategy.
   RULE: on the SECOND serial expect assert, stop the one-by-one whack-a-mole. Apply
   the 11i(i) one-pass `re.sub(r'U\+[0-9a-fA-F]{4}', lambda m: m.group(0).upper())`
   normalization over the whole script text, and re-derive every recurring hiragana
   copula expect (でした/です/の/は) from a committed whole-SENTENCE sample, never
   single-char recall.

2. FIX scripts are also ascii-coded. The /tmp fix scripts themselves declared
   `# -*- coding: ascii -*-` and died with `SyntaxError: encoding problem: ascii`
   when I put raw CJK in their comments and comparison literals. The template caveat
   (build script must be 100% ASCII) applies EQUALLY to every fix/patch/rebuild script
   touching it. Keep fix scripts ASCII-only: all CJK as \uXXXX, comments in ASCII.

3. execute_code is BLOCKED outright in cron mode (approvals gate, "Cron jobs run
   without a user present to approve"). Plan terminal-only from the start.

4. ASCII-slug swap worked: candidate (U+0063.. literal) + は + 0件でした dodged the
   カンデデート katakana leak family entirely (pitfall 11i slug rule), and flow
   readback accepted it inside the JP sentence.

Build shape that converged (reuse for next empty-day): whole-sentence put() entries
s1..s4 ONLY (no fragment composition), DUMP-first optional, uppercase-normalize
expects once pre-run, one flowing-prose read, then write JSON with
json.dumps(..., ensure_ascii=False) + surrogate pre-grep. Fix rounds budget: 1.

## 2026-11-04 run_id 20261104T070031Z (empty-day no-op, clean first-build delivery)

Facts: script JSON ok:true, candidate_count 0; collect file 394-byte boilerplate
confirmed via wc -c; last inbox/newsletters/ entry 2026-10-23 (Nvidia/Samsung) --
no new digest. Case-a no-op: emitted contracted JSON directly (decisions [],
processed_count 0), no read of triage_latest.json, no repo writes, no commit.

Build shape: reused the converged s1..s4 whole-sentence put() pattern from the
2026-11-03 section. Defects: (1) first build attempt died with SyntaxError:
encoding problem: ascii because raw CJK separators were typed directly instead
of via put() keys -- the ascii declaration is a FEATURE that force-catches raw
CJK (11m(5) rule, new instance). (2) A malformed put() call (copy-paste leftover
with a duplicated arg) fired its own assert before first execution -- fixed,
second build delivered clean. Zero post-delivery rounds.

Register additions confirmed this run:
- Whole-sentence put() entries + expects copy-derived from the canonical
  katakana tuples in the SKILL.md 10-23 bullet caught everything pre-run.
  Budget 0-1 fix rounds held (0 needed after the two pre-run guards fired).
- Summary copula shape 'run_id ... no-op ' + copula-deshta + full-stop reads
  acceptably in flow (validated by readback, no particle gap observed).
- Deny asserts (toraiaru / no-o-pa / dejisuto variant / boirapureeto variant /
  no-no / de-desu / de-deshita / to-to-shite / nakatta-deshita) + surrogate
  pre-grep + octal pre-grep all green on the written JSON.

Delivered JSON verbatim from /tmp/newsletter_report_20261104T070031Z.json.
