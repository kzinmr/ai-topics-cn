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


## 2026-09-17 crawl-triage run (case b, context-length fail 34,533 tok)

run_id 20260917T090201Z. Checkpoint 60 candidates -> 8 unique by content hash
(53x aafeba3f flood, established baseline; 7 stale old v2ex threads from Apr-Jul
kept as-is). Straight to manual inbox triage after the `## Response` check per
the settled operating norm.

Fresh-day take that qualified: juejin 米小虾「拆给 8 个子智能体，只拿回 2-3 倍信息：多智能体分解的产出守恒律」
(body 09-16, score 0) — a quantitative claim (8 sub-agents yield only ~2.3x info
vs single agent, "output conservation law"). Went to concepts/agent-team-swarm/
index.md as a falsification-flavored counterpart to the page's Apr 2026 optimistic
4-agent exemplar. Lesson: fresh-day SCORE-0 research-style posts can be the real
durable take — do not let the score-sort hide them; judge by durable-facts test.

Reference: SkillOpt auto-evolution proposal (first 06-11) re-crawled + JavaGuide
Superpowers piece third re-crawl -> one dated reference bullet on agent-skills.md.

Skips confirmed: Amodei items (09-15 recorded), Kimi K3 satire, Cursor转Codex 05-10
resurface, promo/daichong/invite threads, RSI/别卷了 within anthropic.md 09-15 scope.

Commit hygiene: pages committed immediately after patching (sibling warning seen on
agent-skills.md + index.md + log.md, same-day), then index+log as second commit
(9495731 pages, 2e05b98 index+log). Two-step narrow staging worked clean again.


## 2026-09-17 run 2 (crawl-triage, 21:02 UTC) — case (b) ninth+ consecutive, same-day rerun

LLM-triage stage failed again: pre-run reported ok:false "failed to parse JSON
response from crawl-triage output"; output file tail showed RuntimeError: Context
length exceeded (32,873 tokens). Case (b) confirmed via the `## Response` check
(empty). triage_latest.json stale (08-27, decisions:[]). Checkpoint run_id
20260917T090201Z, 60 candidates -> 8 unique after hash-dedupe (53x aafeba3f
flood, 12x 52691b70 Amodei re-crawl, 8x 6b8434d4 Codex-guide dupes) — the
established fixed baseline, not re-investigated.

Same-day rerun context: morning run had already committed 9495731 (pages:
agent-team-swarm + agent-skills) + 2e05b98 (index+log). Dedup baseline = that
pair.

Fresh-day scan (juejin+v2ex 09-17 files, ~30 unique bodies): the durable takes
were BOTH OpenAI-side items structurally invisible to the morning commit's scope:
1. WeChat 09-16 re-crawl "OpenAI 上线模型乘离事件开框架" (model
   misalignment disclosure framework, 3 categories, initial 6 cases) -> take as
   dated preview-only/unverified section on entities/openai.md. First preview hit
   was 09-16 file (title-only), body arrived today = legit evening take per the
   preview-body-later rule.
2. juejin "OpenAI 发了一篇 Astra 时代 Codex 提示词清洁指南" — official
   4-direction prompt-cleanup guidance = the official-side redefinition of the
   morning's recorded "skill = 负優化" thesis -> take on agent-skills.md as
   続報その2 (body not scraped, external link dead -> preview-only).

Skip list: 花生 video ad (score 16, highest-scored fresh item — promo-overrides-score
again), DeepSeek V4 Flash release-reaction posts (09-06/09-09 aggregated), 09-14/09-16
re-crawls (KubeWatch, "即将垄断", Harness 200k-star, 微软 token), Kimi3/小米集团 chat
noise, 别卷了 Anthropic thread (09-15 anthropic.md scope), 安全沙箱 quantization
tutorials.

Sibling-conflict incident (new archetype): openai.md had a working-tree edit from
sibling 26f81dc7 that MERGED the sibling's own bullet and my morning preview line
into one line ("- 发布/翻译节点可能...- 09-16...") — likely the same
trailing-newline patch merge the 09-12 pitfall describes, happening in the
sibling's own commit window. Recovery: verified via `git show HEAD~1` that HEAD's
committed openai.md does NOT contain the merged Chinese line (sibling only
committed 3 lines), so the corruption was working-tree-only; rebuilt the merged
line + my new section in ONE patch (old_string = the corrupted merged line,
new_string = two clean lines + new section). Lesson: when a page shows BOTH
sibling-bullet text AND your own recorded text on a single merged line, check
`git show HEAD:<page>` first — if committed is clean, a single reconstruct-patch
fixes both the merge and the insertion.

Typo note: post-patch `+`-line proofread caught a halfwidth-digit leak in a patched bullet (rendered like "2026" with fullwidth digits) and fixed it; CN-glyph intrusion into Japanese prose remains the standing risk — always re-read `+` lines as prose.

Commits: 15674ad pages-only (openai + agent-skills), then index+log second
commit. Two-step narrow staging again (siblings dirty: kimi, huawei, rag,
openclaw, mediatek, qwen, mcp-security, china-ai-agent-ecosystem — left alone).


## 2026-09-19 crawl-triage run (case b, context-length fail 35,302 tok)

run_id 20260919T090149Z (latest.json, morning run). Pre-run ok:false; `## Response` empty;
`## Error` = context-length 35,302 tokens. Checkpoint 60 candidates → 8 unique by content
hash (53x aafeba3f flood, fixed baseline, not re-investigated). Same-day morning
newsletter-triage (Tech Taiwan, commits 0d23de8/ab637e3) was the dedup baseline - subjects
did not overlap with the crawl run.

Fresh-day takes (manual triage, both went to concept pages, committed immediately per the
sibling-wipe rule):
1. concepts/harness-engineering.md - V2EX t/1243146 personal quantitative LSP-vs-grep
   retrieval-backend measurement (LSP voluntary-selection 0-6%, forcing lowers success rate
   100→89%, recall unchanged, biggest win from output-format change pass@1 0.67→0.83).
   Recorded single-source/unverified as an empirical counterpart to the page's
   Externalization (cognitive artifact) framing.
2. concepts/in-context-learning.md - juejin commentary on arXiv:2609.15990
   "Few-Shot Degradation Is Not What It Seems" (thesis: few-shot gains confounded by
   prompt-length effect) as a conditional falsification signal against the page's
   example-quality claim; preview-only/unverified. Author is the same 09-17 output-
   conservation-law poster - low-score research posts keep being the durable take.

New skip archetype: V2EX "TypeSafe Jev" (structured-decision model, 250K tok/s claim)
reference-only - no existing page, single source, primary info unknown; entity-ization
deferred. Its derivative posts (Jev catalog 433 / plugin) skipped as a same-source chain.
Skills-series flood (Claude Code 9大神/32亲测/27外挂/商汤 skills/boss-call-skills) =
agent-skills.md already-aggregated archetype recurrence, skipped wholesale.

Hygiene: two-step narrow staging (e39a62 pages, 365953d index+log) worked clean; log.md
appended via ASCII /tmp script; post-commit CN-codepoint scan on `git show` + lines was
clean. Sibling warnings on index.md present but diffs were clean.
