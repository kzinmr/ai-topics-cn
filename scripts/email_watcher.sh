#!/bin/bash
# Watch Maildir/new/ for incoming emails and process them
set -euo pipefail

MAILDIR_NEW="$HOME/Maildir/new"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

mkdir -p "$MAILDIR_NEW"

echo "[$(date)] Email watcher started. Watching $MAILDIR_NEW"

# Process any existing emails first
python3 "$SCRIPT_DIR/process_newsletter.py"

# Watch for new files
inotifywait -m -e create -e moved_to "$MAILDIR_NEW" --format '%f' | while read -r filename; do
    echo "[$(date)] New email detected: $filename"
    sleep 2
    python3 "$SCRIPT_DIR/process_newsletter.py"
done
