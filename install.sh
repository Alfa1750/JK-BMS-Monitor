#!/bin/sh
set -eu
APP=/data/apps/JK-BMS-Monitor
SERVICE=/service/jk-bms-monitor
if [ "$(id -u)" -ne 0 ];then echo "Run as root";exit 1;fi
if [ ! -d /opt/victronenergy/dbus-systemcalc-py/ext/velib_python ];then echo "Venus OS velib_python not found; aborting";exit 1;fi
mkdir -p "$APP/monitor" "$APP/etc" "$SERVICE"
cp monitor/*.py "$APP/monitor/"
cp etc/jk-bms-monitor "$APP/etc/"
cp run "$APP/run";chmod 755 "$APP/run"
cat > "$SERVICE/run" <<'RUN'
#!/bin/sh
exec /data/apps/JK-BMS-Monitor/run
RUN
chmod 755 "$SERVICE/run"
echo "Files installed. No reboot or service restart performed. Installer is preliminary."
