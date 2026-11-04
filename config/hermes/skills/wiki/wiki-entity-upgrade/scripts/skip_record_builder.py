#!/usr/bin/env python3
# -*- coding: ascii -*-
# Build a [SKIP] record for a no-op cron run with hiragana copied from a
# committed good ancestor.
# Usage: python3 skip_record_builder.py <output_path> <run_id> <summary_ja_line> <extra_line1> ...
# Lines after the 3rd arg are appended as "- <line>" bullets.
# This builder adds one leading "" and "[SKIP] newsletter-triage ingest run_id <run_id>".
# Hiragana tokens are grabbed ONLY from the committed ai-topics-cn/wiki/log.md
# (never hand-typed). The build asserts good-tuple presence over the WRITTEN
# region, then prints a tail repr for the operator's flow read.
import io, sys, json
T = lambda *cps: "".join(chr(c) for c in cps)
def grab(source, anchor_regex, desc):
    import re
    m = re.search(anchor_regex, source)
    assert m, "grab failed for " + desc
    tok = m.group(0)
    print("GRAB", desc, " ".join("U+%04X" % ord(c) for c in tok))
    return tok
out_path = sys.argv[1]; run_id = sys.argv[2]
extra = sys.argv[3:]
log = io.open("/opt/data/ai-topics-cn/wiki/log.md", encoding="utf-8").read()
# copy-derive from the newest committed entry
tail = log[log.rfind(run_id[:8]) if run_id[:8] in log else log.rfind("## ["):]
MICHIBIKI = grab(tail, "\u307f\u3061\u3073\u304d", "michibiki")
HIRAGANA  = grab(tail, "\u3072\u3089\u304c\u306a", "hiragana")
NOOP      = grab(tail, "\u30ce\u30fc\u30aa\u30da\u30ec\u30fc\u30b7\u30e7\u30f3", "noop")
NEWS      = grab(tail, "\u30cb\u30e5\u30fc\u30b9\u30ec\u30bf\u30fc", "newsletter")
CAND      = grab(tail, "\u30ab\u30f3\u30c7\u30a4\u30c8", "candidate")
BOILER    = grab(tail, "\u30dc\u30a4\u30e9\u30fc\u30d7\u30ec\u30fc\u30c8", "boilerplate")
REKOODO   = grab(tail, "\u30ec\u30b3\u30fc\u30c9", "record")
LINES = ["", "[SKIP] newsletter-triage ingest run_id " + run_id, "",
         "- " + NOOP + " (case-a " + MICHIBIKI + " queue, decisions [] intact in ## Response)."]
LINES += ["- " + l for l in extra]
s = io.open(out_path, encoding="utf-8").read()
assert ("[SKIP] newsletter-triage ingest run_id " + run_id) not in s, "already present"
if not s.endswith("\n"): s += "\n"
before = len(s)
s += "\n".join(LINES) + "\n"
io.open(out_path, "w", encoding="utf-8").write(s)
region = s[before:]
bad = [c for c in region if c in "\u8282\u5b9e\u76d1\u67e5\u4fa7\u5fdc\u7741"]
print("CN-leak:", bad if bad else "clean")
for name, tok in [("NEWS", NEWS), ("CAND", CAND), ("BOILER", BOILER), ("NOOP", NOOP), ("REK", REKOODO), ("HIRA", HIRAGANA), ("MICHI", MICHIBIKI)]:
    n = region.count(tok)
    print(name, "count", n, " ".join("U+%04X" % ord(c) for c in tok))
print("--- tail repr (FLOW READ THIS) ---")
print(repr(region))
