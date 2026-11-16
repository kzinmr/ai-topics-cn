# Trending log build register — 2026-11-16

Run: shelley-trending-topics 2026-11-16, steady state (18 topics, all paged,
zero new YAML, 36kr+zhihu zero 37th). Commit fa517f5 (log.md only).

## New leak-birth sites this run (all caught pre-commit)

1. GRAB PATTERN WRONG-CODEPOINT RECALL (val-side, not expect-side): the
   wakei-label grab regex was typed from recall as U+5185 U+8B21 (内訳 with
   the CN-form 訳 U+8B21) while the committed register is 内訳 = U+5185
   U+8A33 (JP shinjitai 訳). The grab FAILED (assert-style exit) instead of
   shipping the wrong char — good failure mode — but the fix still required
   a live codepoint dump of the committed line to pick the right form.
   RULE: when a grab fails, do NOT re-type the pattern from recall; dump
   the committed line's codepoints around the token and rebuild the pattern
   class from the dump (extends the 10-31 grab-pattern rule to the
   JP-vs-CN shinjitai variant pairs 訳/訳,図/図 etc.).

2. DOUBLE TERMINATOR AT COMPOSITION SEAM: the pagelist grab `[^\n]+`
   swallowed the committed line-final fullwidth period, then the template
   appended another -> 「vector-db。。」. Tuple-blind, caught by flow
   readback only. RULE: after any `[^\n]+` whole-line grab that gets
   re-terminated by the template, `.rstrip('\u3002')` first (generalizes
   the 11h(ii) trailing-space rstrip rule to the terminator case; same
   family as the 11-03 「。」 swallow rule but for grabs ending at EOL
   rather than at an explicit terminator class).

3. ASCII-DECL GATE ON REGEX CLASS LITERALS CONFIRMED AGAIN (11-10 rule):
   `[^）]*` inside a raw-string grab pattern killed the build with
   SyntaxError: encoding problem: ascii. Write every class char as
   `\uff09`. Also a CJK char in a trailing COMMENT (`# e.g. "36目"`) trips
   the same gate — scan the whole file with an ord>127 line probe as the
   first-run gate.

## Shape notes

- Counter line (10-25/.../11-15に続き37目（監視アイテム、据え置き）。) is
  built by grabbing the date list via `10-25(/[0-9\-]+)+`, appending
  `/11-15`, and grabbing the committed 「に続き」 + asserting `36目` then
  emitting `37目` — never re-type the counter phrase.
- The クローリング候補 line is grabbed WHOLE from the ref (`>=3の14件は…`
  to EOL) and only `.replace('の14件','の15件')` — count swap only, zero
  re-typing.
- Kur-line count today = 15 (14 yesterday + 規制/コンプライアンス, which
  newly crossed source_count>=3 and is direct-registered via
  china-ai-regulation / china-ai-model-filing).
