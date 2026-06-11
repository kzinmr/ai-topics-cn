#!/usr/bin/env python3
"""Update a topic's tracking in hot-topics.yaml.

Reusable template for the reliable "write /tmp/ + python3 /tmp/script.py" pattern
that avoids the `patch` escape-drift issue on YAML notes fields containing quotes.

Usage:
    python scripts/update-hot-topics-tracking.py [topic-slug] [new-notes-prefix]

The script:
  1. Reads hot-topics.yaml
  2. Finds the target topic block by slug
  3. Prepends a new date-stamped entry to the notes field
  4. Updates last_crawled to today's date (YYYY-MM-DD)
  5. Writes back

Requires pyyaml for safe structural editing. If pyyaml is unavailable,
set DRY_RUN=1 and use the output as a guide for manual patch() calls.

DRY_RUN=1 python scripts/update-hot-topics-tracking.py deepseek "2026.06.08更新: ..."

If pyyaml is not installed and you need to edit without it, use this approach
in your own script (as done in the session's fix_filing_tracking.py pattern):
    with open('config/hot-topics.yaml') as f:
        content = f.read()
    content = content.replace('old_notes_block', 'new_notes_block')
    content = content.replace('last_crawled: 2026-05-24', 'last_crawled: 2026-06-08')
    with open('config/hot-topics.yaml', 'w') as f:
        f.write(content)
But beware of the "date change poisons unintended topics" pitfall — anchor on
unique notes content, not just the date string.
"""

import sys
import os
import re
from datetime import date

try:
    import yaml
except ImportError:
    yaml = None


def find_topic_block(raw: str, slug: str) -> tuple:
    """Find topic block boundaries by slug. Returns (start, end) or raises ValueError."""
    # Build a regex that matches the full block from `- slug: X` to the next `- slug:` or end
    pattern = re.compile(
        r'(  - slug:\s*' + re.escape(slug) + r'\n.*?)(?=\n  - slug:|\Z)',
        re.DOTALL
    )
    m = pattern.search(raw)
    if not m:
        raise ValueError(f"Topic slug '{slug}' not found in hot-topics.yaml")
    return m.start(), m.end()


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <topic-slug> [notes-prefix]", file=sys.stderr)
        print("  If notes-prefix is omitted, only last_crawled is updated.", file=sys.stderr)
        sys.exit(1)

    slug = sys.argv[1]
    notes_prefix = sys.argv[2] if len(sys.argv) > 2 else None
    today = date.today().isoformat()
    dry_run = os.environ.get('DRY_RUN', '0') == '1'

    path = os.path.expanduser("~/ai-topics-cn/config/hot-topics.yaml")
    if not os.path.exists(path):
        print(f"FILE_NOT_FOUND: {path}", file=sys.stderr)
        sys.exit(1)

    with open(path) as f:
        raw = f.read()

    # 1. Update notes if prefix provided
    if notes_prefix:
        old_notes_pattern = re.compile(
            r'(notes:\s*")(' + re.escape(slug) + r'.*?)(' + re.escape(notes_prefix.split(':')[0]) if ':' in notes_prefix else '') 
        )
        # Simpler approach: find the notes line and prepend
        topic_start, topic_end = find_topic_block(raw, slug)
        topic_block = raw[topic_start:topic_end]
        
        notes_match = re.search(r'(\s+notes:\s*")(.*)(")', topic_block, re.DOTALL)
        if not notes_match:
            print(f"ERROR: Could not find quoted notes field for '{slug}'", file=sys.stderr)
            sys.exit(1)
        
        indent = notes_match.group(1)  # "    notes: \""
        old_body = notes_match.group(2)
        closing_quote = notes_match.group(3)  # should be `"`
        
        new_body = notes_prefix + old_body
        new_notes_line = indent + new_body + closing_quote
        
        old_full = indent + old_body + closing_quote
        new_block = topic_block.replace(old_full, new_notes_line, 1)
        raw = raw[:topic_start] + new_block + raw[topic_end:]
        print(f"Notes for '{slug}': prepended with new entry")

    # 2. Update last_crawled
    old_lc_pattern = re.compile(
        r'(    last_crawled:\s*"?)(\d{4}-\d{2}-\d{2})("?\n)'
    )
    # Find the last_crawled line within this topic block
    topic_start2, topic_end2 = find_topic_block(raw, slug)
    topic_block2 = raw[topic_start2:topic_end2]
    
    lc_match = old_lc_pattern.search(topic_block2)
    if lc_match:
        old_lc = lc_match.group(0)
        new_lc = lc_match.group(1) + today + (lc_match.group(3) or '\n')
        raw = raw.replace(old_lc, new_lc, 1)
        print(f"last_crawled for '{slug}': {today}")
    else:
        # Try without quotes
        lc_match2 = re.search(r'(    last_crawled:\s*)(\d{4}-\d{2}-\d{2})\n', topic_block2)
        if lc_match2:
            old_lc2 = lc_match2.group(0)
            new_lc2 = lc_match2.group(1) + today + '\n'
            raw = raw.replace(old_lc2, new_lc2, 1)
            print(f"last_crawled for '{slug}': {today} (bare date)")
        else:
            print(f"WARNING: Could not find last_crawled for '{slug}'", file=sys.stderr)

    # 3. Write
    if dry_run:
        print("DRY_RUN: no file written")
    else:
        with open(path, 'w') as f:
            f.write(raw)
        print(f"Written: {path}")


if __name__ == "__main__":
    main()
