# Trending-log build learnings (append-only, newest at bottom)

NOTE: created 2026-10-30 — the canonical path was missing from the skill dir that session
(SKILL.md prose referenced it, file absent). If a terminal session recovers the old git-tracked
copy under ~/ai-topics-cn/config/hermes/skills/research/cn-media-analysis/references/, merge.
Append NEW dated sections via the sanctioned /tmp ASCII io.open(...,'a') script ONLY — never
write_file/skill_manage write_file on an append-only register (overwrite incidents 10-16, 10-21).

## 2026-10-30 — trending log.md append (commit 53625db, steady state, zero-volume 20th)

20 topics, all paged, zero new YAML. Three NEW leak-birth sites, ALL in the grab()-live-token
path, ALL caught pre-commit by the mandated flow readback, zero post-commit archaeology:

(i) GREEDY DATE-RANGE GRAB TRUNCATION — grab of the period label with a digit class stopped at
the tilde U+301C (not in the class), matching only yesterday's first date, then the template
appended the fresh range and shipped a glued "10-2610-27" string. Tuple check blind (all chars
legal). Fix: grab the LABEL token only and build the date range as a fresh escaped literal, or
widen the class to include U+301C. Rule: a live-token grab must stop at the label — never let
the grab regex eat per-run VARIABLE data you intend to regenerate.

(ii) CLAUSE-HEAD PARTICLE FRAGMENT DUPLICATION — reusing the committed multi-char token for
"ni-tsuzuki" plus a separate template particle fragment shipped a doubled leading particle
before the counter. Same family as 11k particle-role overload: a grabbed multi-char particle
phrase already contains its leading particle; composition sites must not prepend a matching
fragment. Guard kept: structural assert that the doubled particle digraph is absent.

(iii) WHOLE-CLAUSE VERBATIM-COPY RE-INCLUSION — to avoid re-typing the indirect-cover segment,
the previous entry's segment was copied starting at its clause HEAD, but the own line template
already composed that same direct-registration clause -> the shipped line carried it TWICE, once
fresh with today's counts and once verbatim carrying yesterday's stale counts. Caught only by
flow readback; guard added: count==1 assert on the distinctive verb of any clause that must
appear exactly once. Rule: when copy-deriving a long segment, slice the grab to begin AFTER the
clause your own template composes (start at the indirect-cover marker, not the clause head).

Protocol wins to keep: scoped blob verify over git show HEAD with chr(0x....) hex-literal tuples
passed clean on first run; range audit and octal pre-grep both clean. Reminder that cost a near
miss: the counts in the "all N topics paged" and "source_count>=3 no N items" lines must be
RECOUNTED from today's script output, never carried over from yesterday's committed entry — the
verbatim-copy habit in (iii) nearly smuggled yesterday's numbers in too.

## 2026-11-13 trending log.md append (commit 2a8500b) - three leak-birth sites, ALL caught by flow readback, zero log.md fix rounds

1. *blob-anchor cross-reference (11-11 register rule reconfirmed)*: `blob.rfind('[2026-11-12] trending-topics')` hit a
   LATER newsletter entry quoting the trending commit, so the first ref region was the wrong entry and two grabs failed.
   Anchor with the FULL pipe string `## [date] trending-topics | shelley-trending-topics.timer` (assert i>0).
2. *grab-pattern char-class from recall*: `kan` class for the indirect-cover word was typed without the kanji form
   (U+6E08 mis-read as hiragana sumi); grab assert fired. Per the failed-grab rule, codepoint-probed the committed
   region (dump U+9593 U+63A5 U+30AB U+30D0 U+30FC U+6E08 U+307F) and added U+6E08 to the class - never re-type blind.
   Same run: the zero-volume word needed a cp-literal grabword() (U+30BC U+30ED U+30DC U+30EA U+30E5 U+30FC U+30E0)
   after the hand-typed katakana grab pattern failed.
3. *period/naibun composition seams (tuple-blind, flow-readback-only, 3 rebuilds)*:
   (a) split-grab-rejoin of the period line shipped a doubled date (11-09 + 11-10 + 11-13) - grab the head
       `NN-NN` ONLY (regex `\u671f\u9593\uff1a\d\d-\d\d`) and append exactly one TILDE + end date;
   (b) the naibun line's ken_slash separator token has NO trailing space before the next source, while the last item
       ends with the ken2 token (counter+fullstop) - appending TOK[sep] after ken2 shipped the double-punct
       fullstop-then-slash; rule: build the whole counter line from ONE repeated ken_slash token for all
       non-final sources and use ken2 ONLY at the tail.
   Each defect killed the pre-append flow readback; recovery was truncate-file-at-heading + full rebuild from the
   escape/grab table (11f(a) holds - never line-patch a CJK line).
4. *verify-script check-side concatenation*: a good-tuple check word glued the zenbu prefix onto the zero-volume word
   (MISSING false alarm, commit clean). Build each check word as its OWN full cp tuple; never splice two tuples.
Counter increment: 33rd -> 34th consecutive 36kr+zhihu zero-volume (date list copied from committed entry + append
11-12). 25 topics, all paged; zero new pages, zero new YAML; log.md-only commit.


## 2026-11-15 trending log.md append (commit fd684fd) - one real leak, caught pre-commit

Run: shelley-trending-topics.timer, 22 topics, 36kr+zhihu zero 36th consecutive,
steady state (zero new pages, zero new YAML), single log.md-only commit.

NEW LEAK CLASS (per-char live probe needed even for a 2-char word you "know"):
the intent word shipped as U+610F U+56FE (CN form) instead of the committed
register U+610F U+5716 (JP form). Two mistakes compounded:
(1) the build script typed the escape from recall (never copied from register);
(2) the first verification probe searched HEAD with the SAME wrong pair, and a
second probe also built its pair from re-typed escapes - both returned NOT
FOUND and I nearly read that as "no committed sample exists" (11j(i)
recurrence). Converged only by locating the clause positionally in the HEAD
blob (find on a chr()-built landmark) and dumping codepoints from the FILE.
RULE: codepoint probes must be built with chr(0x....) INT literals or
positional extraction from the blob - never re-typed escape pairs; when a probe
returns 0 hits, suspect the probe before concluding "no sample".
DEFENSE ADDED: deny-list now includes CN form U+610F U+56FE (entry-region
scoped), same family as the collect/collect-homoglyph guard.

Other notes: the inward-token grab pattern needed the right kanji (U+8A33;
first attempt used U+8A73 and the grab assert fired - the assert caught it,
zero fix rounds: failed grab = codepoint-probe region, never re-type, 10-31
rule held). Counter line copied from committed register + appended 11-14,
35->36. Flow readback green on first rebuild after the intent-kanji fix; zero
post-commit log.md fix rounds; blob verify via chr(0x) INT tuples clean.


## 2026-11-19 trending log.md append (commit 6fd6dc7) - counter-grab and grab-boundary classes

Three new leak/gotcha sites, all caught pre-commit, zero log.md fix rounds after append:

1. COUNTER-GRAB STRADDLE: the zero-volume counter token is one contiguous string
   'ZEROWORD <dates>CONT40ME' (no space between the date list and the connector).
   A grab pattern anchored on the connector alone (connector + dates + n + ME) FAILS
   silently because the connector sits AFTER the date list, not before it. Converge
   by grabbing the whole counter clause first (zero-word class through ME) then
   splitting with dates-then-connector-then-digits. Also: raw-string r".." patterns
   with backslash-u escapes are NOT decoded by re - use non-raw strings (or chr-built
   literals) for CJK classes inside re.search, otherwise the class matches the literal
   backslash-u text and returns None.
2. GRAB-BOUNDARY DOUBLE-KEN CLASS (11b family, new mutation): grabbing 'source_count>=3nXXken'
   INCLUDING the counter char then appending a template ken ships 'kenken'. Fix = grab
   WITHOUT the counter char and let the template supply it exactly once. Same root as
   the 11-01 13ken+ken line: counter char must live on ONE side of the composition seam.
3. GRAB-TOKEN SHAPE: the committed inner source list has ken only after the 36kr 0 /
   zhihu 0 / wechat tail numbers, NOT after v2ex/juejin numbers. Composing the new
   day's inner list by hand must match that shape exactly - adding ken after every
   source is a plausible-looking but wrong rewrite; flow-readback caught it.
Also: the verify script's own em-dash in a print() string tripped the ascii-decl gate
(ord>127 scan of the WHOLE script incl. print strings, per the 11-17 recipe, is the
first-run gate). Blob verify passed on first try via chr(0x) int-tuple good/bad checks.

## 2026-11-22 trending log.md append (steady state, 43rd zero-volume, counter 43)

Clean-ish run: 2 grab rounds failed before converging, 1 corrupt-escape shipped
in the FIRST build and was caught pre-commit by the char-diff audit.

Real defect classes hit:
- (a) raw-CJK-in-r-string grab patterns: r"\u30bb..." inside a raw string is NOT
  a unicode escape -- it stays literal backslash-u and matches nothing (also fires
  SyntaxWarning invalid-escape). Converged by building ALL anchors as
  C(0xXXXX,...) chr()-int tuples + re.escape() (11-11 rule, reconfirmed).
- (b) wrong hex digit in a chr() anchor: NEWPAGE anchor typed 0x8846 (visually
  plausible) while the committed token is 0x884C -> anchor not found. Rule: on
  any failed grab, hex-dump the committed line (probe script, " ".join("%04X"))
  and copy the ints -- never repair the anchor by re-typing another guess.
- (c) corrupt-escape-on-disk in a CONSTRUCTED fragment (not just grab side):
  the hand-composed candidate line shipped U+9F48 for intended 0x9F50, caught
  only by diffing the composed line char-by-char against the committed neighbor
  line (zip diff printing pos + both codepoints). This char-diff-vs-neighbor is
  now a mandatory gate for any line copied-but-edited from the previous entry.
- (d) flow readback caught 0 further defects this run (good).

New gate adopted: for lines that are "copy previous entry + bump counter", the
audit script must do a positional zip char-diff vs the committed reference line
and only the intended diffs (counter digits) may appear. Zero-cost, caught (c).

