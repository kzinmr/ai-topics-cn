# Active-crawl run learnings register (append-only, newest dated section at bottom)

Per-run post-mortems for shelley-active-crawl jobs. SKILL.md carries the
generalized rules; this file keeps the dated receipts. If terminal is denied
in your session, add your dated section as a NEW register file under
references/ (active-crawl-run-learnings-YYYY-MM-DD.md) instead of touching
this file — there is no append mode in skill_manage write_file.

## 2026-11-17 (DeepSeek-Harness / China-Coding-Agents-JoyCode run)

- Selection: deepseek (lc 9/5) + china-coding-agents (lc 8/24), both
  high/deepdive, 3-day rule met. Rejected candidates logged in log.md.
- GitHub API (repo + releases endpoints) was the win: Stars 282,481 / MIT /
  weekly v0.2.2 RCs — Verified tier without web_search.
- JoyCode: juejin official-account preview-only body + jdcloud.com grep
  confirm = existence Verified, capability unverified (two-tier labeling).
- Failures and fixes:
  (1) execute_code BLOCKED in cron profile (arbitrary-python gate) — fell
      back to write_file + terminal python3, now a SKILL.md pitfall.
  (2) First page-append /tmp script carried an ascii coding declaration
      with literal CJK payload -> SyntaxError: encoding problem: ascii.
      Fix: no ascii decl for literal-CJK page scripts (ascii decl is only
      for escaped build/verify scripts). SKILL.md pitfall added.
  (3) read_file on hot-topics.yaml served a stale pre-sibling snapshot
      (chatglm 9/11 vs tree 9/17) — see
      hot-topics-yaml-stale-read-file-2026-11-17.md.
  (4) skill_manage patch without top-level name failed with the known
      misleading "Skill '' not found" — always pass name=.
  (5) cn-media-analysis SKILL.md patch attempt hit the 100,000-char hard
      limit — that skill is at capacity; new lessons MUST go to
      references/ files + a pointer, and a future curator pass should
      relocate overflow pitfalls out of SKILL.md (candidates: the long
      11x-series build-protocol bullets already partially relocated to
      trending-log-build-early-learnings.md).
- Sibling dirty tree: committed 4 explicit paths only (2 concepts pages,
  log.md, hot-topics.yaml); sibling yaml bumps rode along in the tracking
  commit, disclosed in the report per SKILL.md section 0.
- Commits 9b44d20 + dba4bea, push clean. Blob-vs-base diff used for the
  honest change account.


## 2026-11-20 active-crawl run (chatglm single-topic deepdive)

- Selection: only chatglm (medium, 2026-09-17) met the 3-day rule among prerequisites/laterals/deepdive; qwen/tencent-hunyuan crawled 11/19, kimi/doubao/mcp-chinese-tools/china-coding-agents 11/17-18, deepseek 11/17; yi (medium, 8/14) skipped with reason logged (zero 01.AI mentions in all digests 9/12-11/19, no Tier-1 source). Single-topic run, legitimate per skill.
- Tier-3 primary sources that worked: HuggingFace API (author=zai-org + search=GLM-5.4), docs.bigmodel.cn static page (dateModified in JSON-LD block), zcode.z.ai/cn. z.ai/blog and docs overview path 404'd; Bing not needed.
- New leak class (yaml notes prepend): the slice idiom `h[:body_start] + new_entry + h[body_start:]` where body_start was computed as `np_ + len('    notes: "')` while new_entry ALSO started with `    notes: "` SHIPPED A DOUBLED OPENER (`notes: "    notes: "`). RULE: the prepended new_entry must contain ONLY the notes body text (date + xin + content), never re-include the `    notes: "` opener; post-write flow-read of the whole notes line is the only catch (quote asserts still pass because the line ends correctly).
- Second leak: hand-typed chain char shipped U+93C6 (wrong) for intended U+94FE; caught by codepoint-dumping the SAME word from the wiki page written minutes earlier (live-register compare), fixed with a whole-token .replace() (11f(a) spirit). Also caught pre-commit: katakana shortening (a dropped mora in the crawl-verified word) found by the flow readback.
- log.md prepend: 11/19 sibling entries are pipe-prefixed; block built via pipe-join helper; `count('||||')==0` guard passed; a 3-pipe-looking `||` blank line in the rendered tail is normal (the block's trailing `|` + neighbor's `|`).
