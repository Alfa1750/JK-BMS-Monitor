#!/bin/sh
set -eu
# Produce a candidate source archive for manual review; this script is not executed during development.
OUT=JK-BMS-Monitor-v0.1.0.tar.gz
tar -czf "$OUT" README.md AGENTS.md LICENSE NOTICE.md CHANGELOG.md docs monitor etc run install.sh uninstall.sh tests
echo "Created candidate archive: $OUT"
