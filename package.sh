#!/bin/sh
set -eu
OUT=JK-BMS-Monitor-v0.1.4.tar.gz
tar -czf "$OUT" README.md AGENTS.md LICENSE NOTICE.md CHANGELOG.md docs monitor etc requirements.txt setup services version gitHubInfo run tests
echo "Created candidate archive: $OUT"
