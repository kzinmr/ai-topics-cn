# Strict-JSON crawl-triage run learnings — 2026-11-09

Run: run_id 20261109T090134Z, ~30th isomorphic skip-only crawl-triage (strict-JSON
contract, no repo writes). Checkpoint 60 candidates -> 8 unique by
(source, path-hash): 53x aafeba3f (2017-12 saturation recollection, archived
2026-04-26) + 7x body-less V2EX placeholders. Zero takes. Clean delivery.

## New leak classes this run (both caught by the mandated flow readback / pre-run gate)

1. **Phantom lexicon words shipped green through put()** — two hand-composed
   R_V2EX fragments were nonsense JP that put() cannot catch because val==expect
   by construction when both sides are typed from the same faulty recall:
   「st紙ディスコバート」 (intended "forum/discussion", ASCII "st" glued + CN 紙
   intrusion + katakana garbage) and 「ワイキなし」. RULE: every content-word in
   the recurring skip-reason skeleton must trace to a register tuple
   (スレッド = U+30B9 U+30EC U+30C3 U+30C9 was already in the register and was
   reused cleanly; フォーラム per-mora from the ボイラープレート-family lesson);
   never coin katakana words from recall. The flow readback is the ONLY check
   that fires on this class — budget it, do not skip it when asserts are green.

2. **Range-audit whitelist must pre-include the emoji block for verbatim
   checkpoint titles** — an 😎 (U+1F60E) echoed verbatim from a v2ex title
   crashed the whole-entry non-ASCII range audit (`AssertionError: 0x1f60e`).
   The 0x1F300-0x1FAFF astral whitelist (11-04 register) belongs in the range
   audit gate itself, not just in the surrogate pre-grep; astral chars are legal
   when SLICED verbatim from the checkpoint (only HAND-escaped surrogate pairs
   crash the UTF-8 write, per 11g(i)). Fix the whitelist before the first run,
   not as a fix round.

3. **Expect-side comma mutation when fixing a val** — patching the R_V2EX val
   from ASCII U+002C to fullwidth U+FF0C left the expect string carrying U+002C;
   the put() assert fired on the EXPECT while the val was perfect (11e(i)
   family, new mutation: the fix that edits val must re-derive expect from the
   SAME edit, or normalize expects with the one-pass uppercase/derivation pass
   AFTER all val edits). Also: a missing comma after a hex literal inside a
   U(...) call is a Python SyntaxError the write_file lint catches — treat the
   lint error as the pre-run gate it is.

## Composition-side confirmations (no change needed, keep the pattern)

- Whole-sentence put() per summary/reason sentence from U() chains + copy-derived
  uppercase expects: zero val-side leaks across 5 sentences.
- Verbatim title/path slices from the on-disk latest.json (`payload.candidates`)
  + dedupe by `([0-9a-f]{8})\.md$` with a seen-set on (source, hash): 60 -> 8 as
  per the permanent baseline.
- candidate_wiki_path derived via endswith(hash) equality assert against the
  archive string, not re-typed (11m-ext holds).
- Today's fresh inbox (Hy4 実測 score 0, Superpowers卸载潮 recollections, LiteLLM
  digest 2026-03-26 preview) carried no durable takes — release-reaction day-1
  noise + saturation recollections; a case-(b)-style fresh scan legitimately
  ends zero-take when the fresh items are promo/recrawl archetypes.


---

## Evening run (run_id 20261109T210137Z) - 31st isomorphic skip-only crawl-triage

Checkpoint 60 -> 8 unique by (source, path-hash): 53x aafeba3f (2017-12 saturation
recollection, archived 2026-04-26) + 7x body-less V2EX (score 0, date 1970-01-01,
stale backlog titles spanning 2026-04-19..2026-07-28). Zero takes, clean delivery,
no repo writes.

### New leak class this run

1. **Half-translated raw kana inside a put() val + synonym-fragment duplication in
   skip reasons** - two distinct defects, both invisible to put() asserts:
   (a) the s2 val shipped with one raw hiragana char (the kana 'zu' hand-typed
       instead of its \uXXXX escape), which the `# -*- coding: ascii -*-`
       declaration killed as SyntaxError (11-04 rule reconfirmed: the decl dies on
       ANY non-ASCII char including a single raw kana, comments AND literals).
       Fix by escaping the char; NEVER strip the ascii decl to silence it.
   (b) the first-pass R_WECHAT/R_V2EX reasons passed every put() assert (val==expect
       by construction, 11-09 morning class) but the flow readback flagged:
       a duplicated near-synonym head ('saturation-resaishuu(...)-fragment +
       saturation-saisei fragment' = same word twice in one sentence, 11d
       duplication family / katakana-assist variant), and the CN-marker fragment
       (zan-nai-naiyou, pitfall 11g(ii)) echoed into reason_ja prose AGAIN despite
       11g(iii) mandating the 'mitoukatsu-honbun' (unretrieved-body) phrasing.
       RULE: for skip-reason sentences prefer a SHORTER whole sentence that names
       the fact once (dated-old-doc + archived-date + no-new-fact) over composing
       independently-recalled synonym fragments; the raw no-content marker must
       never appear inside reason_ja (deny the 4-char sequence outside a
       verbatim-title context, per the 11-08 register). On skip-only runs the flow
       readback is the PRIMARY gate - put() asserts are structurally blind when
       val and expect share one recall event.

### Composition-side confirmations (keep the pattern)
- Whole-sentence put() per summary/reason sentence, uppercase-hex copy-derived
  expects: zero val-side asserts fired; surrogate pre-grep clean (emoji only in
  the verbatim-sliced title, legal per 11g(i)).
- Verbatim title/path slices from on-disk latest.json payload.candidates; dedupe
  via ([0-9a-f]{8})\.md$ seen-set on (source, hash): 60 -> 8 (permanent baseline).
- Range audit with astral 0x1F300-0x1FAFF whitelist pre-included: clean first run.
- Fresh-day scan: no durable takes (2026-11-09 juejin KIMI K3 Gated-MLA explainer
  + wechat event-promo item = release-reaction day-1 / promo archetypes).
