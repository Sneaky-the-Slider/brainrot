#!/bin/bash
# Trendjacker daily update wrapper - cron-friendly
# Add to crontab: 0 9 * * * cd /root/brainrot && ./scripts/trendjacker_daily.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
OUTPUT_FILE="$PROJECT_ROOT/trendjacker_feed.json"

cd "$PROJECT_ROOT" || exit 1

python3 "$SCRIPT_DIR/trendjacker.py" \
    --json \
    --subreddit popular \
    --limit 50 \
    --output "$OUTPUT_FILE" 2>&1

# Optional: git commit if in a repo
if [ -d .git ]; then
    if [ -n "$(git status --porcelain trendjacker_feed.json 2>/dev/null)" ]; then
        git add trendjacker_feed.json
        git commit -m "chore(trendjacker): daily feed update [$(date +%Y-%m-%d)]" >/dev/null 2>&1
    fi
fi
