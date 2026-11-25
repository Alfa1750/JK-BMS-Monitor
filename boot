#!/bin/sh
set -eu
APP=/data/JK-BMS-Monitor
SERVICE=/service/jk-bms-monitor

# Ensure the supervised service exists in the live Venus service overlay.
mkdir -p "$SERVICE"
cp "$APP/services/jk-bms-monitor/run" "$SERVICE/run"
mkdir -p "$SERVICE/log"
cp "$APP/services/jk-bms-monitor/log/run" "$SERVICE/log/run"
chmod 755 "$SERVICE/run" "$SERVICE/log/run"

# Venus OS uses daemontools; bring the service up after provisioning.
svc -u "$SERVICE"
