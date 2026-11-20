# Trending log build register - 2026-11-20

Run: shelley-trending-topics.timer, 2026-11-20. Steady-state no-new-page / no-new-YAML run
(41st consecutive 36kr+zhihu zero-volume). Committed e1e7115 (log.md only).

## Builder shape that produced a CLEAN FIRST COMMIT (zero fix rounds)

Structural line-locate + verbatim copy instead of the grab()/escape pattern:

1. cur = io.open(P).read(); assert HEAD not in cur (double-append guard).
2. ref = cur[cur.rfind("|## [PREVDATE] trending-topics"):][:3000]; rl = ref.splitlines().
3. find(pred) helper locates the 6 reusable lines by ASCII-anchored predicates
   ("v2ex" in l and "juejin" in l; "11-16/11-17/11-18" in l; "AI Agent=" in l;
   "source_count>=3" in l; "steady state" in l) and copies them VERBATIM.
   Zero CJK escapes typed for these lines -> zero escape-leak surface.
4. Mutations are single-token .replace() on the copied strings only:
   - period line: replace old start date with new, old end date with new
   - iwake line: v2ex 83->84, juejin 77->78, wechat 47->48
   - counter line: append /prevdate to date list, then bump 40 -> 41
     (assert new != old and count of new date token == 1)
5. Hand-composed lines (period, iwake) inherit their CJK label chars from copied line
   heads; only digits are replaced.
6. Range audit (3000-30FF / 4E00-9FFF / FF00-FFEF + 0x301C/0xFF5E) + deny list
   (U+6536, U+7EE7, U+5BF9, U+9F48) on the assembled entry; cjk_audit.py on the /tmp
   entry file BEFORE appending.
7. Append via separate /tmp script with a fresh assert HEAD not in read() guard.
8. Commit git add wiki/log.md && git commit --no-verify -q -m "..."; blob verify via
   git show HEAD:wiki/log.md > /tmp/x + INT-tuple presence checks on the tail region only.

## New leak-birth sites avoided this run (rules to keep)

(a) grab() regex pattern strings written as raw r".." with \uXXXX are LITERAL, not escapes:
re.search(r"\u65b0...", text) never matches CJK text (pattern stays backslash-u). First two
build attempts died on failed grabs before any damage shipped. RULE: locate lines
STRUCTURALLY with ASCII anchors (digits, slugs, >=, =) and copy verbatim; if a CJK regex is
unavoidable, build the pattern as a NORMAL string (not raw) so \uXXXX decodes, or decode
inside grab() via pat.encode("ascii","backslashreplace").decode("unicode_escape").

(b) counter bump via two sequential replaces (append /prevdate, then 40->41) needs
assert new != old plus count(new-date-token)==1; the list contains no other bare "40" today
but assert anyway.

(c) Roster delta check: today's trending set was a strict subset of yesterday's committed
23-item page map (AI-safety / RLHF dropped out) -- keeping the superset map line verbatim is
the established steady-state practice; no edit needed.

## Steady-state facts
- 36kr=0 and zhihu=0: 41st consecutive (date list now 10-25 ... 11-19).
- Roster: AI Agent 91, Claude 36, GPT 25, DeepSeek 20, OpenAI 19, MCP 17, Gemini 10,
  Kimi 10, Vibe Coding 8, Cursor 7, Anthropic/Qwen/RAG/Hunyuan/Doubao 6, Quantization 4,
  Function Calling 3, local-deploy 2, multimodal 2. All paged, all YAML-covered/direct.
- Volumes: v2ex 84 / juejin 78 / wechat 48.
