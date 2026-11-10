#!/usr/bin/env python3
# ASCII-only no-op entry appender for wiki/log.md + codepoint audit.
# Usage: python3 ascii-log-append.py <lines-json-file> [marker]
# lines-json-file: JSON array of strings, each ALREADY carrying its intended
# line prefix ("|" blank rows are just "|", bullet rows "|-..."). Keep the
# narrative frame in ASCII and use \uXXXX escapes ONLY for short CJK spans.
# marker (optional but RECOMMENDED): a unique ASCII substring of the new entry
#   (e.g. the run_id). If already present in the file the script aborts
#   (double-append guard). ALWAYS grep the target file for the marker after
#   running this — count==0 means the append silently did not land (confirmed
#   2026-10-22: a /tmp script whose write_file returned a "modified by sibling
#   subagent" warning never executed its write despite exit 0). Recovery:
#   re-write_file the script under a NEW filename and re-run.
# NOTE: the deployed copy lives in the REPO at
#   ai-topics-cn/config/hermes/skills/wiki/wiki-entity-upgrade/scripts/ascii-log-append.py
# — skill_view serves the content but the file is NOT under ~/.hermes/skills/.
# Locate with: find /opt/data/ai-topics-cn/config/hermes/skills -name ascii-log-append.py
# GRAB/COPY-DERIVE CAVEAT (confirmed 2026-10-28): when a build script live-grabs
# reusable CJK tokens from a prior committed entry via re.search, write the
# pattern with SINGLE-backslash "\u30DC" escapes so Python parses them into the
# actual characters — a DOUBLE-backslash "\\u30DC" puts the literal six chars
# \u30DC into the regex and the grab assert fires even though the token is in
# the file. Guard: print the "U+%04X" codepoint tuple of every grabbed token
# before using it (a literal-regex bug dumps ASCII backslashes, not U+30xx).
import io, json, sys

path = "/opt/data/ai-topics-cn/wiki/log.md"
lines = json.load(io.open(sys.argv[1], encoding="utf-8"))
entry = "\n".join(lines) + "\n"

s = io.open(path, encoding="utf-8").read()
# Idempotency + landed-marker guard (confirmed 2026-10-22).
if len(sys.argv) > 2 and sys.argv[2]:
    if sys.argv[2] in s:
        print("MARKER_ALREADY_PRESENT, aborting"); sys.exit(1)
if not s.endswith("\n"):
    s += "\n"
before = len(s)
s += entry
io.open(path, "w", encoding="utf-8").write(s)
print("appended %d lines, +%d bytes" % (len(lines), len(s) - before))

# Post-append codepoint audit over the JUST-APPENDED region only (never the
# whole file -- auditing/replacing on shared append-only files can touch
# siblings' committed text).
region = s[before:]
bad = []
for ch in region:
    # CN simplified glyphs that never belong in Japanese prose:
    # 节 U+8282, 实 U+5B9E, 监 U+76D1, 查 U+67E5, 侧 U+4FA7 (confirmed 2026-10-16 leak)
    # 応 U+5FDC also flagged: leaks where 前 U+524D intended (confirmed 2026-10-21 log append: 応先 for 前日, caught by tail prose read, invisible to codepoint scan)
    # 睁 U+7741: CN-simplified homoglyph of JP 着 U+7740 (confirmed 2026-10-26: 未着信 shipped 未睁信; renders near-identically, invisible to a prose read — only this scan catches it)
    if ch in "\u8282\u5b9e\u76d1\u67e5\u4fa7\u5fdc\u7741":
        bad.append("U+%04X %s" % (ord(ch), ch))
print("CN-leak scan:", bad if bad else "clean")
print("--- CJK inventory (proofread these against intended prose) ---")
for ch in sorted(set(c for c in region if ord(c) > 0x2000)):
    print("U+%04X %s" % (ord(ch), ch))
