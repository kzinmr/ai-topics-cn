# Strict-JSON newsletter-triage run learnings — 2026-11-14

Run: 20261114T070038Z (morning newsletter-triage, strict-JSON contract, zero wiki edits authorized).

## Situation
- Pre-run script `ok: true`, `candidate_count: 7` — NOT an empty day, NOT case (b).
- All 7 candidates = same Tech Taiwan 胡說科技 Substack issue dated 2026-11-13,
  digest `2026-11-13--Can-Nvidia-and-Its-Taiwanese-Suppliers-Keep-Soaring-Without---46a1efd6.md`,
  single message_id. Classic multi-URL Substack duplicate archetype (redirect / app-link /
  open.substack restack / read-in-app variants of ONE post + 2 header/promo stubs,
  length 157/139).
- Novel twist vs the 11-11 archetype: the claim is now ASSERTED as done —
  "Jensen Huang has indeed resigned", CFO interim CEO, board seat relinquished —
  whereas 11-11 was "Alleged Ties to a Suspected Chinese Spy" (commit da47c48 / triage 1bff9e8).
  Same newsletter, escalating single-source chain over 3 days.

## Decisions (labelled as my own triage — LLM stage did not run this job type; contract = I decide)
- take 1: 54da9459 canonical redirect copy — asserted resignation claim + CPO (co-packaged
  optics) supply-chain thesis. candidate_wiki_path: entities/nvidia (does NOT exist yet;
  nearest pages = concepts/semiconductor-packaging.md, concepts/ai-infrastructure.md;
  11-11 spy chain also unrecorded in wiki). Mark 単一ソース・未検証 downstream.
- reference 1: 2739c563 open.substack body copy — verify full text before any ingest.
- skip 5: header stub 265c6bde (157ch promo), profile stub 0674ce3b (139ch), and 3 more
  URL-variant dupes 7fd4c89b / 022f28d1 / ce934eef (identical 471ch excerpt).

## Leak / process notes
- `semantic-article-grouping` skill confirmed DELETED from working tree
  (git status shows ` D config/hermes/skills/research/semantic-article-grouping/SKILL.md`).
  The cron banner "skill not found and skipped" is now the PERMANENT expected state —
  do not hunt for it; sibling session is pruning skills (several other D entries).
- No CJK build script needed this run? Not true — summary_ja/reason_ja were composed via a
  /tmp ASCII script with \uXXXX escapes + put()-style asserts, flow-read before emit.
  Zero post-delivery fixes.
- No repo writes (strict-JSON job type). No [SILENT] — populated decisions contract.
