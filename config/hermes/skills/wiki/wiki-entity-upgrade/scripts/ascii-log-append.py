#!/usr/bin/env python3
# ASCII-only no-op entry appender for wiki/log.md + codepoint audit.
# Usage: python3 ascii-log-append.py <lines-json-file>
# lines-json-file: JSON array of strings, each ALREADY carrying its intended
# line prefix ("|" blank rows are just "|", bullet rows "|-..."). Keep the
# narrative frame in ASCII and use \uXXXX escapes ONLY for short CJK spans.
# NOTE: the deployed copy lives in the REPO at
#   ai-topics-cn/config/hermes/skills/wiki/wiki-entity-upgrade/scripts/ascii-log-append.py
# — skill_view serves the content but the file is NOT under ~/.hermes/skills/.
# Locate with: find /opt/data/ai-topics-cn/config/hermes/skills -name ascii-log-append.py
import io, json, sys

path = "/opt/data/ai-topics-cn/wiki/log.md"
lines = json.load(io.open(sys.argv[1], encoding="utf-8"))
entry = "\n".join(lines) + "\n"

s = io.open(path, encoding="utf-8").read()
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
    if ch in "\u8282\u5b9e\u76d1\u67e5\u4fa7":
        bad.append("U+%04X %s" % (ord(ch), ch))
print("CN-leak scan:", bad if bad else "clean")
print("--- CJK inventory (proofread these against intended prose) ---")
for ch in sorted(set(c for c in region if ord(c) > 0x2000)):
    print("U+%04X %s" % (ord(ch), ch))
