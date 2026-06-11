#!/usr/bin/env python3
"""Validate hot-topics.yaml structural integrity.

Usage:
    python scripts/validate-hot-topics-yaml.py [path-to-hot-topics.yaml]

Defaults to ~/ai-topics-cn/config/hot-topics.yaml.
Checks:
  - Valid YAML parsing
  - Required keys per topic (crawl_policy, priority, search_hints, wiki_pages, notes, added)
  - Duplicate YAML keys at the raw text level (PyYAML silently ignores duplicates)
  - search_hints and wiki_pages are non-empty arrays

Exit code 0 = clean, 1 = issues found (with details on stderr).
"""

import sys
import os
import yaml
import re

def find_duplicate_keys(text: str) -> list:
    """Check for duplicate YAML keys within each top-level topic block.

    Uses a simple heuristic: within each `- slug:` block, count key occurrences.
    This is conservative — it catches the common subagent corruption where
    search_hints: or wiki_pages: appears twice in one block.
    """
    # Split by `- slug:` to isolate per-topic blocks
    blocks = re.split(r'(?=  - slug:)', text)
    issues = []
    for block in blocks:
        if not block.strip():
            continue
        # Extract slug
        slug_match = re.search(r'slug:\s*(\S+)', block)
        slug = slug_match.group(1) if slug_match else 'unknown'
        # Count key occurrences
        keys = re.findall(r'^\s+(\w+):', block, re.MULTILINE)
        seen = set()
        for k in keys:
            if k in seen:
                issues.append(f"[{slug}] Duplicate key: {k}")
            seen.add(k)
    return issues

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/ai-topics-cn/config/hot-topics.yaml")

    if not os.path.exists(path):
        print(f"ERROR: File not found: {path}", file=sys.stderr)
        sys.exit(1)

    with open(path) as f:
        raw = f.read()

    # 1. Parse YAML structure
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as e:
        print(f"ERROR: YAML parse failed:\n{e}", file=sys.stderr)
        sys.exit(1)

    if not isinstance(data, dict) or 'topics' not in data:
        print("ERROR: Root key 'topics' not found", file=sys.stderr)
        sys.exit(1)

    topics = data['topics']
    if not isinstance(topics, list):
        print("ERROR: 'topics' is not a list", file=sys.stderr)
        sys.exit(1)

    # 2. Check required keys per topic
    required_keys = ['crawl_policy', 'priority', 'search_hints', 'wiki_pages', 'notes', 'added']
    errors = []
    for i, topic in enumerate(topics):
        slug = topic.get('slug', f'index-{i}')
        for key in required_keys:
            if key not in topic:
                errors.append(f"[{slug}] Missing required key: {key}")
        # Verify search_hints and wiki_pages are non-empty lists
        for list_key in ['search_hints', 'wiki_pages']:
            val = topic.get(list_key)
            if val is not None and not isinstance(val, list):
                errors.append(f"[{slug}] {list_key} is not a list: {type(val).__name__}")
            elif val is not None and len(val) == 0:
                errors.append(f"[{slug}] {list_key} is empty")

    # 3. Check for duplicate keys at raw text level
    dup_issues = find_duplicate_keys(raw)
    errors.extend(dup_issues)

    # 4. Report
    if errors:
        for e in errors:
            print(f"ISSUE: {e}", file=sys.stderr)
        print(f"\nFound {len(errors)} issue(s) in {len(topics)} topics", file=sys.stderr)
        sys.exit(1)
    else:
        print(f"OK: {len(topics)} topics, no structural issues found")

if __name__ == "__main__":
    main()
