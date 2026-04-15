#!/bin/bash
# Scheduled crawl script for Chinese AI topics
set -euo pipefail

cd /home/exedev/ai-topics-cn

echo "[$(date)] Starting scheduled crawl..."

# Run all Tier 1 crawlers (V2EX, Juejin, 36kr)
python3 scripts/crawl_all.py --tier 1 --limit 20 2>&1

# Run trending topics analysis
echo ""
python3 scripts/trending_topics.py --days 3 2>&1

# Git commit if there are changes
if [ -n "$(git status --porcelain inbox/ wiki/)" ]; then
  git add inbox/ wiki/
  git commit -m "crawl: $(date +%Y-%m-%d-%H%M) auto-crawl $(find inbox/ -name '*.md' -newer /tmp/last_crawl_marker 2>/dev/null | wc -l) new items" 2>/dev/null || true
fi

touch /tmp/last_crawl_marker
echo "[$(date)] Crawl complete."
