# 2026-11-19 active-crawl run post-mortem (Qwen / Tencent-Hunyuan)

Run: qwen + tencent-hunyuan selected (both high/deepdive, 75d/65d stale). Sibling
sessions were active (11/17 deepseek run, 11/18 kimi/doubao run had already claimed
those) — topic selection had to skip 11/17-18-crawled topics in the log rejection list.

## New/confirmed lessons
1. **Pitfall recurrence (ascii-decl)**: the hot-topics + log.md tracking script was
   first written with `# -*- coding: ascii -*-` while carrying CJK `u"..."` payloads
   -> `SyntaxError: encoding problem: ascii`. Tracking scripts (YAML notes + log
   blocks) contain CJK just like page-append scripts, so the "no ascii decl when
   payload is literal CJK" rule applies to BOTH file classes, not only wiki page
   appends. Fix = drop the decl, keep `io.open(..., encoding='utf-8')`.
2. **Frontmatter `updated:` from a compacted session summary was STALE** (qwen listed
   2026-09-17, actual file 2026-10-02 — a sibling had bumped it). Always grep the
   live `^updated:` line before writing the replace anchor; the assert caught it
   pre-run (zero cost).
3. **touch() slug-anchored helper worked clean** for notes-prepend + last_crawled
   (both topics, first try): find `  - slug: X\n`, replace last_crawled line within
   bounds, splice `'    notes: "'` + new_prefix before old opener, then per-section
   regex assert `notes:` closes with `"`. New prefix must end with the dotted date +
   kanji-colon opener + trailing space so the old date opener flows in cleanly.
4. **Pre-existing UNCLOSED notes**: mcp-china `notes:` lacks its closing quote AT HEAD
   (pre-existing, far from this edit) — reported but NOT touched per
   pre-existing-lint pitfall. Only the 2 touched topics were quote-verified.
5. **Primary-source dead ends this run**: openlm.ai old static pages (e.g.
   /qwen3-8-max/) now 404 (site SPA-ified) — the "curl the vendor static page" Tier-3
   trick fails for OpenLM.ai as of 11/19; hunyuan.tencent.com is a JS shell (Hy4
   string 0 hits). Both topics shipped with single-source unverified labels from
   juejin/digest frontmatter-verified dates. Bing Hunyuan query = spam pollution
   (known pattern, no retry).
6. **Cross-linking pair**: Qwen4-Max and Hy4 were announced in the same daily digest
   (11/17) — recorded mirrored on both entity pages with cross-references.
7. Two-step commit clean (pages, then log+yaml, explicit paths). Working tree had
   heavy sibling dirt (~30 modified wiki pages + skill deletions) — never staged.
   Push OK: 8430cd7..ea92be8.
