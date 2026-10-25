# CJK Append Verification Protocol (condensed from retired `cjk-append-verify` skill)

Use after ANY append of Japanese/Chinese text to a shared file (`wiki/log.md`,
`references/case-b-run-learnings.md`, output files) — the moment between
"script printed ok" and "git commit". The ASCII-frame append tools and
CN-denylist scans do NOT catch valid-glyph wrong words; this protocol does.
This is the distilled companion to the `ascii-log-append.py` pattern in
`wiki-entity-upgrade` and the pitfall-(11x) families above.

## The invariant: two independent gates, neither alone sufficient

1. **Codepoint audit** — `scripts/cjk_audit.py` (catches CN-script intrusions
   like 收/侧/图 in JP prose).
2. **Human-style prose read of the tail** — catches valid-but-wrong glyphs the
   denylist is structurally blind to: 応先 for 前日, reduplications like 管管外,
   extra-kana katakana like トライアジョル, missing kana like 委ぬ.

A clean CN-denylist scan means NOTHING about gate 2. Confirmed 2026-10-21: an
entry that passed the denylist shipped 4 gate-2 defects.

## Protocol (budget: ≤2 probe+fix rounds, then commit residual)

1. **Append** via the ASCII-frame `/tmp` script pattern (see
   `wiki-entity-upgrade` → "Cleanest no-op log.md append", or
   `templates/cjk-log-entry-build.py`).
2. **Gate 1**: run `cjk_audit.py` (or the audit built into `ascii-log-append.py`)
   on the appended region ONLY. Fix CN intrusions.
3. **Gate 2**: `tail` the file and read the new entry as a human sentence,
   character by character on every CJK word you care about. List every suspect.
4. **Never hand-type fix literals in either direction.** For each suspect:
   a. **Probe**: `scripts/cjk_fix_probe.py <file> <ascii-anchor>` — per-char
      `U+%04X` + `unicodedata.name` dump of the live suspect span (rfind
      semantics). The dump decides what's actually in the file — your belief
      does not.
   b. **Fix**: `patch` tool with `old_string`/`new_string` COPIED VERBATIM from
      tail/probe output (fuzzy matcher handles CJK fine when copied, fails when
      retyped from recall — 2026-10-21: a hand-typed fix script asserted
      count==1, got 0 on 応先 because the recalled codepoint was wrong again).
   c. Minimum span only — one word, never a sentence rewrite (re-typed
      replacement = new leak birth site).
5. **Final verify script** over ONLY the appended region
   (`idx = s.rfind(<unique ascii header>)`): assert every bad form absent, every
   good form present, CN-denylist re-scan clean, deletion-line check
   `git diff -- <file> | grep -c "^-[^-]"` == 0.
6. Commit. If a suspect is unresolved after ~2 rounds, leave the residual, note
   it in the log entry, and commit — persistence beats polish.

## Known valid-glyph leak families (invisible to CN denylists)

- 応 U+5FDC leaked for 前 U+524D (応先/前日) — in ascii-log-append.py denylist
  (77c9d6c) but expect more families
- Reduplication: 管管外 for 対象外
- Katakana vowel/extra-char slips: トライアジョル/トリアージ, ヴ/ブ/プ, レ/ル,
  ズ/ツ families
- Missing kana tails: 委ぬ/委ねる
- CN homoglyphs of JP chars: 收集/収集, 图/図 — hit the denylist only if listed;
  run the full codepoint inventory (not just the denylist) and eyeball the table
