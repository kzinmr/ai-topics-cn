# Trending log grab-side learnings 2026-11-07

Run: 2026-11-07 trending daily report, 28th consecutive 36kr+zhihu zero-volume, steady state, log.md-only commit.

## New leak/bite sites (all caught pre-commit)

1. Grab-region boundary class: the ref window cur[rfind(PREV_HEAD):][:3500] clipped the reusable counter phrase out of reach because the immediately-preceding entry used the CN-form keizoku variant while only the entry before it has the correct U+7D9A form. The grab() assert fired cleanly. The fix that worked: a second grab region from the older entry (ref1105 + grab5()), never relaxing the assert or escaping the phrase from recall. Rule: before grabbing a per-run-incrementing phrase, probe BOTH the preceding entry and the one before it and grab from whichever actually contains it. A single-entry window is one CN-variant leak away from a failed build.

2. Grab-token double-punctuation class: grabbing a token that ENDS in fullwidth punctuation (colon U+FF1A) while the line template also supplies that punctuation shipped a doubled colon. Range/deny audits are blind (both chars legit). Caught ONLY by the mandated flowing-prose readback before appending. Rule: when a grabbed token ends in punctuation your template also supplies, drop it from one side only. Same family as 11h(ii) trailing-space double, punctuation instead of whitespace.

3. Judge-line pipe-wrapper loss: grabbing the whole verdict line dropped its leading pipe wrapper (log.md pipe-prefix style). Flow-readback caught it. Rule: grabbed whole lines from pipe-wrapped entries must be re-verified for the leading pipe (lstrip then restore, or exclude the wrapper in the grab regex and re-add in the template).

## What worked

- Live-token grab plus esc() audit trail; deny-list extended with U+7D56 and U+7E7C for the keizoku family; range audit; whole-entry rebuild over line-patching (two defects fixed in one scripted pass via minimal wrong-token replace pairs with pre-asserts that the defects exist).
- Post-commit scoped blob verification with chr(0x....) hex literals, clean on first try.

## Tool note

- skill_manage(action='write_file') dropped file_content on every attempt for this register (4 retries, ASCII-only payloads) - per the >2-retries rule, the dated section was NOT committed to references/. TODO for next terminal-equipped session: append this file's content via the sanctioned /tmp io.open(...,'a') route.
