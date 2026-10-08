#!/bin/bash
# Cron entry point: translate new entries, commit and push if anything changed.
set -u
cd "$(dirname "$0")"
exec 9>.run.lock
flock -n 9 || exit 0  # previous run still going

export PATH="$HOME/.local/bin:/usr/local/bin:/usr/bin:/bin"
python3 translate.py
rc=$?

git add -A CHANGELOG.*.md i18n
if ! git diff --cached --quiet; then
  n=$(git diff --cached --name-only -- i18n | wc -l)
  git commit -q -m "Update translations ($n files)"
  git push -q origin HEAD
fi
exit $rc
