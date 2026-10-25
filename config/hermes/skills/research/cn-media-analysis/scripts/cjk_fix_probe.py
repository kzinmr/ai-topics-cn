#!/usr/bin/env python3
# Hex-dump probe for CJK fix rounds. ALWAYS run this before writing any fix
# script -- the dump decides what the file actually contains, not your belief.
# Usage: python3 cjk_fix_probe.py <file> <ascii-anchor> [window_before] [window_after]
# Prints per-char U+%04X + unicodedata.name for the live region around the
# LAST occurrence of the anchor (use rfind semantics for append-only files).
# NOTE: same path resolution caveats as cjk_audit.py — in cron sessions `~`
# resolves oddly; invoke via the repo-absolute path under
# config/hermes/skills/research/cn-media-analysis/scripts/.
import io, sys, unicodedata

path, anchor = sys.argv[1], sys.argv[2]
before = int(sys.argv[3]) if len(sys.argv) > 3 else 8
after = int(sys.argv[4]) if len(sys.argv) > 4 else 8

s = io.open(path, encoding="utf-8").read()
i = s.rfind(anchor)
if i < 0:
    print("ANCHOR NOT FOUND:", repr(anchor))
    sys.exit(1)
lo, hi = max(0, i - before), min(len(s), i + len(anchor) + after)
for c in s[lo:hi]:
    try:
        name = unicodedata.name(c)
    except ValueError:
        name = "UNNAMED"
    print("U+%04X %r [%s]" % (ord(c), c, name))
