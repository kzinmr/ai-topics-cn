# Verify-Script / Build-Script Expect Leaks — Dated Register (append-only, newest at bottom)

Per pitfall (11i)(vi) and (11l). Each dated section records leak-birth sites caught in strict-JSON
build scripts or post-commit verify scripts, with the committed-register tuples to COPY FROM.
For empty-day newsletter no-op runs, the summary is built from this register's verified tuples —
never from recall.

---

## 2026-10-26 — crawl-triage run 20261026T210212Z (verify-script expect side)

Committed register (copy from here, do not re-derive):
- 再収集 = U+518D U+53CE U+96C6 (committed register is 収 U+53CE, NOT CN 收 U+6536; 収集 x156 in history)
- 榜単: 単 = U+5358 (NOT 榜单 U+699C U+5355 — the CN simplified 单 leaks if typed from recall)
Recipe on any verify FAIL: dump the WRITTEN file's codepoints FIRST (`python3 -c` over the file via
io.open) — the FAIL is usually the CHECK side (expect tuple), not the shipped data.

---

## 2026-10-27 — newsletter-triage empty-day no-op, run_id 20261027T070014Z

Case-a no-op (zero-mail day): collect file at
`~/.hermes/cron/data/newsletter/newsletter_collect_20261027T070014Z.json` = the 394-byte boilerplate
variant; `ls inbox/newsletters/` latest = 2026-10-23 (no new digest). Checkpoint intact
(`_checkpoint.ok: true`), `candidate_count: 0`. Emitted contracted JSON directly
(`decisions: []`, `processed_count: 0`), no repo writes (strict-JSON job).

### New leak class: copula/particle FRAGMENT STACKING in the composition lines

All four defects were in the s1/s2/s3 composition lines, NOT in the put() vals — every tuple check
passed while the composed sentence was broken. Tuple checks are blind to this whole class; only the
flow readback caught them. Mutations observed in one session:

1. *Double topic-particle* — sentence composed `date + wa + nl + tri + wa + ...` shipped
   「2026-10-27はニュースレタートリアージ**は**394バイト…」 (two は markers, second should be が).
   Rule: a clause has exactly ONE topic-particle slot (wa) after the subject; the subject-marker slot
   needs が — give it its own key, never reuse the wa fragment.
2. *Overloaded も deleted mid-fix* — s2 shipped 「ダイジェストファイルは**も**ありません」
   (fragment grabbed where none was needed). Same 11k(ii) overload class: a fragment must have a
   designated composition site; if a sentence doesn't need it, its key must not appear in that line.
3. *Glued copula connective* — `atta + kute` composed 「ボイラープレート形であっ**たて**一日」
   (あった + て glued). Japanese te-connectives must be single verified tokens, never
   past-tense-fragment + て-fragment concatenations.
4. *Double copula stack* — fixing (3) by swapping in a datta fragment while keeping the earlier
   no2(で) fragment shipped 「形**でだったて**一日」 — two copulas adjacent. Lesson: when a fix swaps
   one fragment in a copula chain, REWRITE the whole clause to a flat committed shape instead of
   swapping pieces — this session's cascade cost 4 sequential rounds on one sentence.

### Correct protocol for the empty-day summary (validated shape, copy the whole sentence templates)

Three flat sentences, each one clause, committed clean shape (2026-10-27 run, delivered):
- S1: `<date>はニュースレタートリアージが394バイトのボイラープレートでした。`
- S2: `最新のダイジェストファイルはありません。`
- S3: `カンデデートは0件でした。no-opと終わります。`

Verified tuples (put() expects, uppercase):
- ニュースレター U+30CB U+30E5 U+30FC U+30B9 U+30EC U+30BF U+30FC
- トリアージ U+30C8 U+30EA U+30A2 U+30FC U+30B8
- バイト U+30D0 U+30A4 U+30C8
- ボイラープレート U+30DC U+30A4 U+30E9 U+30FC U+30D7 U+30EC U+30FC U+30C8 (long vowels intact — 11k(iii))
- 最新 U+6700 U+65B0 / ダイジェスト U+30C0 U+30A4 U+30B8 U+30A7 U+30B9 U+30C8 / ファイル U+30D5 U+30A1 U+30A4 U+30EB
- カンデデート U+30AB U+30F3 U+30C7 U+30C7 U+30FC U+30C8 / 件 U+4EF6 / でした U+3067 U+3057 U+305F
- ありません U+3042 U+308A U+307E U+305B U+3093 / 終わります U+7D42 U+308F U+308A U+307E U+3059
- no-op (ASCII) U+006E U+006F U+002D U+006F U+0070 (5 chars — 11k(i))

Expect-side typos caught pre-run this session (val perfect, expect wrong — fix the expect per 11e(i)):
- り U+308A mistyped as U+30EA in a となりました expect
- こ U+3053 mistyped as katakana コ U+30B3 in a この expect
Also: a `.replace()`-built expect (11i(ii) class) was removed and rewritten as a plain uppercase tuple.

Bottom line for the next empty-day run: paste the three S1/S2/S3 templates above into the composition
lines verbatim (keys already traceable to the tuple table), skip any 「形」/「一日でした」 sub-clause
embellishment (the source of all four pileups), and budget ZERO fix rounds — the clean run is one pass
once the templates are copied rather than fragment-composed.

## 2026-11-25 trending log.md append (commit 1356dbc) - CHECK-SIDE leak only, build clean

- Build: full-line grab from prev entry (digit/date edits only) + chr()-tuple literals with `assert LIT in ref` gates.
  Two literal tuples died on their own in-ref asserts BEFORE running (build-side, caught by the mandated gate):
  ZEROWORD recalled as zero+bu+ra+i+mu family vs committed zero+bo+ru+u+mu; KANMON tail dropped ki.
- VERIFY-SIDE leak (this family's recurring shape): good-tuple for the katakana word was hand-typed starting
  U+3048 (HA) instead of U+30A8 (E) - assert MISSING fired while the blob was clean. Converged per standing rule:
  dump the region's codepoints via ASCII-anchor regex (here: find on the two-kanji prefix, print hex window),
  copy the ints into the check literal. Cost: 1 round, zero damage.
- Rule reconfirmed: the verify script's expect side is a leak-birth site; a MISSING report means dump-first,
  never re-type the check word.
