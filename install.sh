#!/bin/sh
set -eu

SOURCE_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
APP="$SOURCE_DIR"
SERVICE=/service/jk-bms-monitor

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

mkdir -p "$APP/vendor" "$APP/etc" "$SERVICE"

# Preserve existing user configuration on upgrades; initialize only on first install.
if [ ! -f "$APP/etc/jk-bms-monitor" ]; then
    cp "$APP/etc/jk-bms-monitor.default" "$APP/etc/jk-bms-monitor"
fi

# Install pinned runtime dependencies into the application's own vendor directory.
# This avoids changing Venus OS system Python packages.
python3 -m pip install --disable-pip-version-check --no-cache-dir --upgrade --target "$APP/vendor" -r "$APP/requirements.txt"

cat > "$SERVICE/run" <<RUN
#!/bin/sh
exec "$APP/run"
RUN
chmod 755 "$SERVICE/run"

echo "JK-BMS-Monitor files and app-local BLE dependencies installed."
echo "Configuration: $APP/etc/jk-bms-monitor"
echo "No service restart or reboot performed by this installer."
