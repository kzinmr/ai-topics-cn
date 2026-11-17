# Newsletter Empty-Day No-Op — Build Register (append-only, newest dated section at bottom)

Companion register for the `cn-media-analysis` empty-day (case-a) no-op path. The
SKILL.md pitfall points here; the full dated post-mortems live in the repo copy at
`~/ai-topics-cn/config/hermes/skills/research/cn-media-analysis/references/newsletter-empty-day-learnings.md`.
**Copy-divergence hazard (confirmed 2026-11-04):** the live skill dir
`~/.hermes/skills/cn-media-analysis/references/` can be a SEPARATE working copy from
the git repo copy. If `skill_view` shows this register missing a date that the repo
copy has, read the repo copy as canonical (it is git-tracked in `~/ai-topics-cn` and
committed with narrow staging: `git add <explicit path> && git commit --no-verify -m`).

## Converged build shape (reuse verbatim, confirmed 2026-11-04 run_id 20261104T070031Z, clean first-build delivery, 0 post-delivery rounds)

Pre-run verification (two facts, then emit contracted JSON directly):
1. `wc -c ~/.hermes/cron/data/newsletter/newsletter_collect_<run_id>.json` == 394
   (the boilerplate variant).
2. `ls inbox/newsletters/ | tail` shows no digest for today's date.

Then: no `triage_latest.json` read, no wiki/repo writes, no commit, strict JSON only
(job contract forbids `[SILENT]`).

Builder (write ASCII /tmp script, run via terminal):
- Whole-sentence `put(key, val, expect)` entries s1..s4 ONLY — never fragment-compose
  the summary (fragment composition is where のの / copula-splice / particle-orphan
  leaks are born; whole sentences make every CJK char a copy event).
- Expects copy-derived, never recalled: canonical katakana tuples from the SKILL.md
  10-23 bullet — ニュースレター U+30CB U+30E5 U+30FC U+30B9 U+30EC U+30BF U+30FC,
  ボイラープレート U+30DC U+30A4 U+30E9 U+30FC U+30D7 U+30EC U+30FC U+30C8 (NOT
  ボイラプレート / no ム), ダイジェスト U+30C0 U+30A4 U+30B8 U+30A7 U+30B9 U+30C8,
  収集 = 収 U+53CE (JP form, NOT CN 收 U+6536).
- **RARE-KANJI EXPECT RULE (confirmed 2026-11-05 run_id 20261105T070012Z):** for any
  lexicon word NOT in the canonical katakana/kanji tuples above whose kanji is rare
  (the 新規/shinki 規 class — U+898F, not the lookalike U+8987/8982/8986 block), DO
  NOT hand-type its expect. Derive the expect from the val expression itself:
  `_v = (…U(...)+…); _e = " ".join("U+%04X" % ord(c) for c in _v); put(k,_v,_e)`.
  The expect literal is itself a recall event and the leak-birth site — on 11-05 the
  val was perfect every round but a hand-recalled U+8987 expect fired identically for
  THREE fix rounds (patch and /tmp replace both re-typed the same wrong cp from visual
  memory, 11e(i) rare-kanji mutation). Corollaries: (i) when the SAME assert fires
  identically 2+ times, STOP re-typing — live-probe a committed sample instead
  (`git show HEAD:wiki/log.md` blob, regex 新+one-CJK-char → U+65B0 U+898F x329
  settled it in one probe); (ii) `unicodedata.name()` on a suspect cp only returns
  `CJK UNIFIED IDEOGRAPH-XXXX` (no semantic hint) and CANNOT adjudicate rare kanji —
  only committed-text can; (iii) a regex strip-patch on the build script can also eat
  the adjacent `summary =` line — after any strip, re-grep dependent lines before
  rerunning. The cp-derived-expect shape also makes future rounds copy events, so the
  fix-script budget returns to 0–1.
- `# -*- coding: ascii -*-` on the build script is a FEATURE, not an obstacle: it
  force-dies with `SyntaxError: encoding problem: ascii` the moment any raw CJK
  separator (、。) is typed instead of routed through a put()/`\uXXXX` literal. That
  crash IS the 11m(5) guard firing. Fix = move every separator into the lexicon;
  NEVER delete the declaration. Applies equally to fix/patch scripts.
- Pre-run guards that caught everything on 2026-11-04: (a) the ascii SyntaxError
  above; (b) a malformed `put()` call (copy-paste leftover with a duplicated arg)
  fired its own expect assert before first execution. Budget 0–1 fix rounds.
- Deny asserts over the composed JSON: トライアトル, ノーオパ, ディジェスト,
  ボイラプレート, ネースレター, のの, でです, ででした, ととして, なかったでした
  (copula double), + surrogate pre-grep `\\ud[89a-f]` + octal pre-grep `\\[0-7]`.
- Flow-readback of the printed summary before delivering; the shape
  `run_id <ID> no-op でした。今日はニュースレターの収集がなかったものでした。
  ニュースレター一件も新着はありません。394バイトのボイラープレートバージョンでした。`
  validated (「ものでした」 explanatory-past copula reads acceptably).
- Summary-sentence ASCII slug `no-op` is fine inside JP (5 chars n-o-hyphen-o-p;
  an expect for it must be the 5-char uppercase tuple — a 4-char hand-typed expect
  is the known 11k(i) char-drop leak).
- Verify written file via `read_file` as proof before pasting as the cron response.

## Dated sections

(Repo copy holds the full dated post-mortems; this file carries the reusable
protocol. Append new dated leak-class sections to the REPO copy via the sanctioned
/tmp `io.open(...,'a')` ASCII script, then mirror a one-line pointer here.)

### 2026-11-17 (run_id 20261117T070039Z)

# Newsletter empty-day register addendum 2026-11-17 (run_id 20261117T070039Z)

Clean case-a no-op. Pre-run two facts green: collect file 394 bytes, no
2026-11-1x digest in inbox/newsletters (latest 2026-11-13). Zero candidates,
zero decisions, zero repo writes.

New leak-birth sites this run (all caught pre-delivery; 4 build-script rounds,
0 delivered-defect rounds):

1. PHANTOM-VERB CLASS EXTENSION: the 11-11/11-09 presence gate caught polite
   copulas ARIMASEN (0x3042...x0) and DESU (x0) in committed log.md — this
   register's committed shape is plain-form (xNashi x496, xDeshita appears
   only inside longer compounds). Rule: for empty-day summaries, prefer
   plain-form predicates (xNashi / xDeshita) and run the phantom gate on
   EVERY predicate token, not just content words — a 0-count verb ships green
   under val==expect just like a phantom noun.
2. NASHI KATAKANA-INTRUSION: xNashi was first hand-typed as U+306A U+30B7
   (shi katakana) — phantom probe count=0 caught it; committed register is
   hiragana U+306A U+3057. Hiragana particles are ALSO recall sites, not just
   kanji/katakana.
3. COUNTER-NEGATION CONTRADICTION (tuple-blind, flow-readback-only): the
   first passing build shipped x0-ken + xNashi on the same predicate
   ("0 items none" — contradictory). Flow readback is the primary gate for
   semantics; codepoint asserts cannot see it.

Korekara-wa was a phantom too (probe fired) — dropped, s5 became
xinjouhou-no-shuushuu-mo-hoji-nashi.
