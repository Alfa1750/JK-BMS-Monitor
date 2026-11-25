#!/bin/sh
set -eu
if [ "$(id -u)" -ne 0 ];then echo "Run as root";exit 1;fi
svc -d /service/jk-bms-monitor 2>/dev/null || true
rm -rf /service/jk-bms-monitor /data/JK-BMS-Monitor
if [ -f /data/rc.local ]; then
    sed -i '/# JK-BMS-Monitor persistent service startup/d;/\/data\/JK-BMS-Monitor\/boot/d' /data/rc.local
fi
rm -rf /data/log/jk-bms-monitor
echo "JK-BMS-Monitor removed; startup hook and logs removed."
