#!/bin/sh
set -eu

APP=/data/apps/JK-BMS-Monitor
SERVICE=/service/jk-bms-monitor
SOURCE_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

if [ "$(id -u)" -ne 0 ]; then
    echo "Run as root"
    exit 1
fi
if [ ! -d /opt/victronenergy/dbus-systemcalc-py/ext/velib_python ]; then
    echo "Venus OS velib_python not found; aborting"
    exit 1
fi
if ! python3 -m pip --version >/dev/null 2>&1; then
    echo "Python pip is required. Installer did not change the system."
    exit 1
fi

mkdir -p "$APP/monitor" "$APP/vendor" "$APP/etc" "$SERVICE"
cp "$SOURCE_DIR"/monitor/*.py "$APP/monitor/"
cp "$SOURCE_DIR"/requirements.txt "$APP/requirements.txt"
cp "$SOURCE_DIR"/run "$APP/run"
chmod 755 "$APP/run"

# Preserve existing user configuration on upgrades; initialize only on first install.
if [ ! -f "$APP/etc/jk-bms-monitor" ]; then
    cp "$SOURCE_DIR/etc/jk-bms-monitor" "$APP/etc/jk-bms-monitor"
fi

# Install pinned runtime dependencies into the app-local vendor directory.
# This avoids changing Venus OS system Python packages.
python3 -m pip install --disable-pip-version-check --no-cache-dir --upgrade --target "$APP/vendor" -r "$APP/requirements.txt"

cat > "$SERVICE/run" <<'RUN'
#!/bin/sh
exec /data/apps/JK-BMS-Monitor/run
RUN
chmod 755 "$SERVICE/run"

echo "JK-BMS-Monitor files and app-local BLE dependencies installed."
echo "Configuration: $APP/etc/jk-bms-monitor"
echo "No service restart or reboot performed by this installer."
