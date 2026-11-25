#!/bin/sh
set -eu
OUT=JK-BMS-Monitor-v0.1.2.tar.gz
tar -czf "$OUT" README.md AGENTS.md LICENSE NOTICE.md CHANGELOG.md docs monitor etc run install.sh uninstall.sh tests requirements.txt setup services version gitHubInfo
echo "Created candidate archive: $OUT"
