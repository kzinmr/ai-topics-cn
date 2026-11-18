# Trending-log build register - 2026-11-18

Clean steady-state trending run (39th zero-volume, commit 79a48f8). Zero wiki
writes, log.md-only commit, blob verified clean via chr(0x) INT-tuple good/bad
checks (the shuusei check was a check-side false alarm - that word is not part
of this entry type; all entry-relevant tuples OK, all known-bad tuples clean).

## New leak site: CJK literals in an INLINE COMMENT next to a chr() anchor

The 11-17 pre-run gate caught it before execution: an ASCII-only build script
carried a trailing inline comment written with real CJK (the anchor-shape
comment after a c_anchor line) -> SyntaxError: encoding problem: ascii on the
FIRST run. Same family as the 11-10/11-17 comment rule, new mutation: the
comment documented the very CJK fragment being built, so the temptation to
paste it verbatim is highest exactly where the rule bites. Rule: in build
scripts, describe CJK in comments as U+XXXX or romaji (ken/no), never paste the
fragment; run the ord>127 whole-file scan as the FIRST gate, fix comments with
a single patch, zero log.md fix rounds (confirmed again this run).

## Reusable deltas (no new shape)

- counter replace anchored on ASCII-safe unique substring
  "11-16 + tsuzuki + 38 + me" built with escapes; date list APPENDED prevdate.
- candidate count replace ">=3-no-14-ken" -> ">=3-no-15-ken"; anchor built via
  chr(0x306E)/chr(0x4EF6) INT literals, not typed.
- 39th 36kr=0 AND zhihu=0; 23 trending topics all paged; zero new YAML;
  15 items sc>=3 (Anthropic re-entered the sc>=3 tier at 4 sources).
