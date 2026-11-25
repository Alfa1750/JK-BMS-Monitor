#!/bin/sh
set -eu
OUT=JK-BMS-Monitor-v0.1.3.tar.gz
tar -czf "$OUT" README.md AGENTS.md LICENSE NOTICE.md CHANGELOG.md docs monitor etc boot run install.sh uninstall.sh tests requirements.txt setup services version gitHubInfo
echo "Created candidate archive: $OUT"
