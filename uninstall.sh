#!/bin/sh
set -eu
if [ "$(id -u)" -ne 0 ];then echo "Run as root";exit 1;fi
rm -rf /service/jk-bms-monitor /data/apps/JK-BMS-Monitor
echo "Files removed; no reboot or other services changed."
