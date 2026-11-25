#!/bin/sh
set -eu
if [ "$(id -u)" -ne 0 ];then echo "Run as root";exit 1;fi
rm -rf /service/jk-bms-monitor /data/JK-BMS-Monitor
echo "JK-BMS-Monitor removed. No reboot or other services changed."
