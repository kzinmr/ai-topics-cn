# hot-topics.yaml: patch Escape-Drift Workaround & Script-Based Update Pattern

Problem: the `patch` tool's YAML notes field editing frequently fails with
`Escape-drift detected` when the notes contain quote characters.

## Root Cause

The `notes:` value in hot-topics.yaml is a double-quoted YAML string that may itself contain
literal `"` characters (from Chinese text or nested quotes). When the agent serializes
`old_string`/`new_string`, the JSON serialization adds `\"` before each quote inside the string.
The patch tool's comparison then finds no match because the file has `"` not `\"`.

## Verified Workaround: write + python3 /tmp/script.py

Used successfully in the 2026-06-08 session. Steps:

1. Write a Python script to /tmp/ using `write_file`:
```python
with open('config/hot-topics.yaml') as f:
    content = f.read()

# Use content.replace() — no serialization layer, works on raw bytes
old_notes = 'notes: "2026.05.24更新: ...全文..."'
new_notes = 'notes: "2026.06.08更新: ...新規情報を先頭に追記...2026.05.24更新: ...全文..."'
content = content.replace(old_notes, new_notes, 1)

# Update last_crawled
content = content.replace(
    "    last_crawled: 2026-05-24\n",
    "    last_crawled: 2026-06-08\n",
    1
)

with open('config/hot-topics.yaml', 'w') as f:
    f.write(content)
```

2. Run the script:
```bash
python3 /tmp/script.py
```

## Pitfalls of content.replace()

1. **Date collision**: `content.replace('last_crawled: 2026-05-28', '2026-06-08')` changes EVERY topic
   with that date, not just the intended one. **Anchor on unique notes content**, not dates.

2. **Notes must be exact match**: Copy the notes string exactly as it appears in the file.
   A single character difference (whitespace, punctuation) means the replace silently no-ops.
   Verify by reading the notes line fresh with `read_file` before crafting the script.

3. **file_path ordering**: The second `with open()` for writing must use a raw string, not a
   variable that was modified — avoid any accidental path manipulation between read and write.

4. **YAML structure integrity**: content.replace() is string-blind. It cannot detect if the
   replacement breaks YAML indentation, quoting, or structure. Always verify the result with
   `read_file` after writing.

## Alternative: scripts/update-hot-topics-tracking.py

A reusable script at `scripts/update-hot-topics-tracking.py` encapsulates this pattern.
Usage:
```bash
python scripts/update-hot-topics-tracking.py deepseek "2026.06.08更新: 新しい情報..."
```
Requires pyyaml. If unavailable, use the content.replace() workaround above.
