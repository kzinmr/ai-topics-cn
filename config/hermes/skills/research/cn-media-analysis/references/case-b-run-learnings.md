# 2026-09-15 run 2 (case-b, context-length failure at 33,251 tokens) — SIBLING-WIPE INCIDENT LESSON

Run_id 20260915T121023Z. LLM-triage stage failed (context-length 33,251 tokens). Injected
checkpoint 14 candidates → 8 unique, ALL stale (already processed by morning commit 8655608).
Fresh inbox (v2ex 49 + juejin 21) manual-triaged against 8655608 as dedup baseline.
Two takes: anthropic.md (Amodei『我们必须给前沿踩刹车』9/12 statement confirmed published +
Huang×Trump All-In Summit phone call, preview-only/単一ソース) and deepseek.md (V2EX t/1242083
V4.1 Flash POSITIVE field report score 69 — first reverse-direction reaction vs the 09-12
complaint accumulation → usage-layer split signal). Fresh-day fingerprint changed: no aafeba3f;
new dominant hash 49437192 (×17) = the V4.1 Flash reaction flood. Dedup baseline 60→8 collapse
held (14→8 this volume).

## THE INCIDENT (the lesson worth more than the takes)

**A sibling commit can wipe your uncommitted working-tree edits. Commit YOUR pages FIRST.**

- This session patched anthropic.md / deepseek.md / index.md / log.md; then a sibling
  active-crawl session (d113e465, commit 2949045, "fix: restore wiki files wiped by 29d9f6e")
  committed `git checkout`-restored versions of those same files, silently reverting ALL FOUR
  of this session's uncommitted edits (they vanished from the working tree; `patch` later
  reported "modified since you last read it" as the only visible symptom).
- Recovery: 2949045's parent was 8130cc4 (not this session's pages commit — no merge, pure
  overwrite). Re-applied everything from this session's own transcript tool-call arguments
  (patch/write_file old_string/new_string verbatim). The transcript is the ONLY backup for
  uncommitted wiki edits — the repo and stash had nothing.
- Also found: the sibling's re-added 09-15 iris block in log.md and its index 本日更新 section
  had themselves wiped earlier in the day and were absent — re-added them (noted in the
  index/log commit message).

## Rules extracted

1. **Sequence under sibling concurrency**: pages edits → IMMEDIATE commit+push → only then
   touch shared index.md/log.md. Never leave pages uncommitted across long analysis phases
   (raw-file writing, re-reads) — the wipe window is minutes.
2. **A "restore" commit by a sibling is a red flag that a wipe already happened**: check
   `git show <sha> --stat` for files YOU have dirty. If your dirty file appears in someone
   else's commit as a change you didn't stage, assume your edits are gone and recover from
   your own transcript, not by re-patching the (already-clean-looking) file — patch anchors
   will silently mismatch after a wipe.
3. **Sibling commits can also steal a planned take**: 'LLM评测的失效' was skip-logged here
   ("=朝 commit 既出の批判 chain") but was actually taken by the sibling as NEW concept page
   concepts/ai-math-limits-debate.md — verify skip claims against `git show <sibling-sha>`
   before finalizing the log; correct the log explicitly rather than leaving a false skip.
4. **Commit-scope verification post-push**: after `git show HEAD --stat`, confirm each expected
   file appears (this session expected raw ×2, only 1 existed — the deepseek raw had never
   actually been written despite the earlier plan; logged the discrepancy in log.md
   commit-hygiene line rather than scrambling a late addition).
5. /tmp script name collision is real: `/tmp/append_log.py` had been overwritten by a sibling
   session (write_file warned). Copy to a unique name (`/tmp/append_log_run2.py`) before
   executing; never run a /tmp helper immediately after write_file without checking the
   modified-by warning.
6. log.md append after a wipe must re-anchor: the wipe removed the previous run's whole entry;
   `git show HEAD:wiki/log.md | tail` + `grep 2026-09-15` confirmed which dated entries
   survived before appending. Recovery = rebuild the missing prior blocks AND the new one in
   one pass, verify with grep -c per heading.

# 2026-09-16 run 2 (case-b, context-length failure at 33,666 tokens) — fresh-fingerprint day, no aafeba3f

Run_id 2026-09-16T12:00:00Z (latest.json). Checkpoint 150 raw candidates → 44 unique (hash-dedupe).
Dominant hash 49437192 (×33) = Codex "近乎无限上下文" reaction flood — ALREADY taken by the morning
run (openai.md 続報 2026-09-16, index entry present). Morning run was committed, so dedup baseline =
read morning index entry + log, not git-show.

Takes (manual triage, no LLM decisions existed):
- entities/deepseek.md 続報(2026-09-16): Harness "GitHub 200k+ stars in weeks" claim — IMPORTANT
  nuance: this time the BODY was received (古茗前端团队, article-date 09-14), so the claim is recorded
  as "本文受領部によれば" not "プレビューのみ". Still 単一ソース・未検証 (no independent star check).
  Plus ch.08 multi-agent explainer (reference) and the 8/13 launch explainer re-crawl (reference,
  post/7673390412729614390). Observation logged: explainer ecosystem going three-layer
  (実務記事→章立て解説→再解説).
- concepts/agent-skills.md 続報(2026-09-16): 滴滴面试官 Skill-監査 article (juejin
  post/7646674857891266606, original recorded 09-06) re-crawled WITH full body — new facts: none;
  logged as topic-consolidation evidence only (interview-question status). Skip-list rule extended:
  "朝 take で記録済みの本文受領版だが新事実なし" also covers PRIOR-DAY-recorded articles whose full
  body arrives days later via re-crawl.

Hygiene failures worth remembering:
- index.md run-2 entry shipped with CN glyph leaks (节/监査/查) that the 本|実 grep scan does NOT
  catch — needed 3 commits to converge. Scan `+` lines for the CN-only set [节实监查] and
  proofread the index bullet BEFORE first commit.
- Two-step commit (pages first, index+log second) went cleanly; sibling-modified skills/ and other
  wiki pages left unstaged and untouched.

# 2026-09-17 run (case-a, parse-failure red herring, empty checkpoint) — no-op

Job: newsletter-triage ingest cron. Pre-run reported `ok:false, "failed to parse JSON response
from newsletter-triage output"`, but the output file's `## Response` held a fully intact JSON
(`checkpoint_run_id 20260917T070004Z`, `decisions:[]`). Fast discriminator confirmed again:
parse-only failure (case a) whenever `## Response` has a parseable json block — the parser's
complaint is a red herring. Checkpoint `_checkpoint.ok:true`, `candidate_count:0` — legitimate
empty queue (no new NL emails since ChinAI #374 on 09-14, already committed 09-15).

Verified `git status` on `inbox/newsletters/` and `wiki/raw/articles/` was clean (no new
untracked files since 09-15) -> nothing to collect-only commit. Outcome: appended a case-(a)
no-op entry to `wiki/log.md` via an ASCII `/tmp` Python script (pipe-table `|` blank prefix +
`|- ` bullet style matching neighbors), delivered the structured report, committed log only
(sha 0a82b12).

LESSON: run the post-commit CN-codepoint typo-scan as
`git show <sha> -- file | grep '^+' | grep -nE '<CN codepoints>'` — grepping raw `git diff`
output matches context lines too and gave a false-positive count of 3 on this run.
