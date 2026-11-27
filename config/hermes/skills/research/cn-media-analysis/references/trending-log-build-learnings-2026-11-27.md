# Trending-log build learnings - 2026-11-27 (11ac addendum)

Run: 2026-11-27 trending-topics timer, commit 89fc9b5 (log.md only, steady state).

## New leak/failure class: raw-string \uXXXX regex literals

Counter-line grab/match needed BOTH CJK literals and digit classes.
A raw string r"\u306b" is a LITERAL backslash-u sequence that matches
nothing. Six rounds burned on one counter-line regex.

Rules:
- Build patterns by CONCATENATION: chr(0x)-tuples for CJK + plain
  "[0-9]+" (or "[0-9/-]+") character classes as ordinary strings.
- Non-raw "\d" in a normal string is a valid regex \d (no corruption);
  the failure mode is exclusively raw-string \uXXXX.
- On FIRST grab/match failure: repr() the pattern and test it
  standalone against a chr()-built sample string before editing the
  script again. Do not iteratively re-patch the same line.

## What worked
- Live grab of period line, inner label, zero-volume word, monitor
  parenthetical, new-page prefix, topic->page map, candidate line
  (digit 19->17 via single .replace), verdict line from the committed
  11-26 entry: zero recall defects in the shipped entry.
- Counter line: date list copied from committed line + append 11-26,
  bump 47->48. Flow readback clean; blob verify via chr(0x) int tuples
  green (ni-tsuzuki, zero-volume, hantei present; U+6536/U+7D99/U+9F48
  absent).
- One anchor recall error (U+596C for U+5968 in the newpage anchor)
  caught by failed-grab assert, fixed via chr()-tuple rebuild per
  11ab LIVE-ANCHOR-FIRST.
