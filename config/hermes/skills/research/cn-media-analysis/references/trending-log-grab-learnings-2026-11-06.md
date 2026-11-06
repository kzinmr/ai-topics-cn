# 2026-11-06 trending log.md append -- two NEW leak-birth sites (continuation of the
# trending-log-grab learnings family; register file kept separate because this session
# had no sanctioned append path verified for the sibling file).

## Run context
Daily trending report cron, 2026-11-06. Builder = /tmp ASCII script, grab() live-token
pattern per the builder recipe. Steady state: 22 topics all paged, zero new YAML,
36kr+zhihu zero-volume 27th consecutive (22nd unbroken occurrence family).
Commit aa201e3 (log.md only, --no-verify, amend after fix).

## New leak class 1: DEAD put() lexicon entry silently overrides the live grab
The script carried BOTH a hand-typed put("kizoku", ni+U+7D99+ki, expect) entry AND a
newly added live grab of the same token (ni-X-ki before the digit-kaimoku). The grab
result was assigned via `LEX["kizoku"] = kizoku[1:]` AFTER the put block, but the
hand-typed put entry's val shipped U+7D9A (CN form) because the assignment line was
written against the grab var while an earlier `put` had already registered the wrong
val under the same key -- the composition then picked the lexicon value, and the
per-word asserts were BLIND (the put's own val-vs-expect assert passed on the wrong
val because BOTH val and expect were mis-recalled as U+7D9A -- the jointly-mistyped
(val,expect) pair class, pitfall 11n, now confirmed for a GRAB-overridden key).
Post-commit scoped blob check caught it: working tree showed U+306B U+7D9A U+304D
where U+7D99 was intended. Fix = scoped single-char replace in the region, amend.
RULE: when replacing a lexicon word with a live grab, DELETE the put() line entirely
(don't shadow it) and add the grab result to the denylist of its known-bad forms
(here U+7D9A U+304D and the CN form of the zhipu pair -- the committed register is
U+667A U+8C31; deny the wrong rare-kanji variant caught this run).

## New leak class 2: zhipu second char mis-escaped (U+8C31 shipped as U+8B31)
"ChatGLM/zhipu" in the 22-topic page list shipped U+8B31 (a rare unrelated kanji,
dead-giveaway of a one-block-off escape). Tuple check on the page list is blind (both
valid kanji); flow readback missed it in the long comma-separated list. Caught by
post-commit scoped bad-codepoint deny check (U+8B31 not-in region). RULE: proper-noun
kanji inside long ASCII-mixed lists (page rosters) are the highest-risk recall sites;
derive them via grab over the previous entry (re.search for the ASCII anchor around
the token) and put() them with a val-copied expect, never hand-escape.

## What worked
- grab-based live tokens (kikan, iwake, zero, kansa, shinky, handan) all clean.
- Pre-run gates caught: lowercase-hex expects (fixed by normalization INSIDE put() --
  the 11-04 rule; a separate pre-pass was skipped), octal/surrogate greps green.
- ASCII coding decl died on a CJK comment (pitfall 11(5), known) -- switched to utf-8
  decl after verifying zero non-ASCII in string literals.
- Denylist + scoped blob verify (region = blob[rfind(HEAD):]) caught both defects;
  whole-blob checks would have false-positived on old CN forms (10-13 rule).
