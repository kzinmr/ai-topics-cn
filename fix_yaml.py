#!/usr/bin/env python3
"""Fix YAML indentation in hot-topics.yaml"""

with open('config/hot-topics.yaml', 'r') as f:
    lines = f.readlines()

# Find lines that should be indented but aren't
new_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    stripped = line.rstrip('\n')
    
    # Lines that start with "- slug:" at column 0 (should be 2-space)
    if stripped.startswith('- slug:') and not line.startswith('  -'):
        new_lines.append('  ' + stripped + '\n')
        i += 1
        continue
    
    # Lines that start with property names at 2-space indent inside topics (should be 4-space)
    # But only for entries that are NOT list items (not starting with '- ')
    if line.startswith('  ') and not line.startswith('  -') and not line.startswith('    '):
        # This is a 2-space indented property inside a list item - should be 4-space
        if not stripped.startswith('#'):
            new_lines.append('    ' + stripped.lstrip() + '\n')
            i += 1
            continue
    
    new_lines.append(line)
    i += 1

with open('config/hot-topics.yaml', 'w') as f:
    f.writelines(new_lines)

print('Done fixing indentation')
