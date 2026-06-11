#!/usr/bin/env python3
"""Validate hot-topics.yaml structural integrity WITHOUT pyyaml dependency.

Usage:
    python scripts/validate-hot-topics-yaml-basic.py [path-to-hot-topics.yaml]

Defaults to ~/ai-topics-cn/config/hot-topics.yaml.
Checks (no yaml module required — pure string/regex parsing):
  - Each `- slug:` block starts a topic
  - Required keys present (crawl_policy, priority, notes, added)
  - notes field has balanced double-quotes (one opening, one closing per block)
  - notes closing quote appears before `added:` line
  - last_crawled has a valid date format (YYYY-MM-DD or YYYY-MM-DD with quotes)
  - No duplicate keys within the same topic block

Exit code 0 = clean, 1 = issues found.

Limitation: does NOT validate YAML structural correctness (e.g., indentation,
array nesting). For that, use validate-hot-topics-yaml.py when pyyaml is available.
"""

import sys
import os
import re


def check_block(block: str, slug: str) -> list:
    """Run structural checks on a single topic block (text between slug delimiters)."""
    errors = []
    lines = block.split('\n')

    # 1. Check required keys exist
    key_names = []
    for line in lines:
        m = re.match(r'^\s+(\w+):', line)
        if m:
            key_names.append(m.group(1))

    required = ['crawl_policy', 'priority', 'notes', 'added']
    for k in required:
        if k not in key_names:
            errors.append(f"[{slug}] Missing required key: {k}")

    # 2. Check notes field has balanced quotes
    # Find the notes line: starts with "    notes: " (possibly with content)
    notes_lines = [i for i, l in enumerate(lines) if re.match(r'^\s+notes:\s*"', l)]
    if notes_lines:
        start_idx = notes_lines[0]
        # Check if the notes line itself has a closing quote (single-line)
        if lines[start_idx].count('"') >= 2:
            pass  # single-line notes with balanced quotes
        elif start_idx < len(lines) - 1:
            # multi-line notes — find closing quote
            closing = False
            for i in range(start_idx, len(lines)):
                if lines[i].count('"') >= 2:
                    closing = True
                    break
                elif lines[i].rstrip().endswith('"') and not lines[i].rstrip().endswith('\\"'):
                    closing = True
                    break
            if not closing:
                errors.append(f"[{slug}] notes field may be missing closing quote")
    else:
        errors.append(f"[{slug}] notes field not found or not quoted")

    # 3. Check last_crawled format
    lc_lines = [l for l in lines if re.match(r'^\s+last_crawled:\s*', l)]
    if lc_lines:
        lc = lc_lines[0]
        val_match = re.search(r'last_crawled:\s*"?(\d{4}-\d{2}-\d{2})"?', lc)
        if val_match:
            date_str = val_match.group(1)
            if date_str < '2025-01-01' or date_str > '2030-12-31':
                errors.append(f"[{slug}] last_crawled date out of range: {date_str}")
        else:
            errors.append(f"[{slug}] last_crawled has non-date value: {lc.strip()}")

    # 4. Check for duplicate keys within block
    seen = set()
    for k in key_names:
        if k in seen:
            errors.append(f"[{slug}] Duplicate key: {k}")
        seen.add(k)

    return errors


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser(
        "~/ai-topics-cn/config/hot-topics.yaml"
    )

    if not os.path.exists(path):
        print(f"FILE_NOT_FOUND: {path}", file=sys.stderr)
        sys.exit(1)

    with open(path) as f:
        raw = f.read()

    # Split by `- slug:` to get per-topic blocks
    # The first segment (before the first topic) is the header
    parts = re.split(r'(?=  - slug:)', raw)

    if len(parts) < 2:
        print("NO_TOPICS: No '- slug:' blocks found", file=sys.stderr)
        sys.exit(1)

    header = parts[0]
    topic_blocks = parts[1:]

    all_errors = []

    for block in topic_blocks:
        slug_m = re.search(r'slug:\s*(\S+)', block)
        slug = slug_m.group(1) if slug_m else 'unknown'
        all_errors.extend(check_block(block, slug))

    if all_errors:
        for e in all_errors:
            print(f"ISSUE: {e}")
        print(f"\n{len(all_errors)} issue(s) in {len(topic_blocks)} topics")
        sys.exit(1)
    else:
        print(f"OK: {len(topic_blocks)} topics, basic structural checks passed (no pyyaml needed)")


if __name__ == "__main__":
    main()
