#!/bin/sh
set -eu

SOURCE_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
APP="$SOURCE_DIR"
BOOT_HOOK=/data/JK-BMS-Monitor/boot
RC_LOCAL=/data/rc.local

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
if ! command -v svc >/dev/null 2>&1; then
    echo "Venus OS svc command not found; aborting"
    exit 1
fi
if ! command -v svlogd >/dev/null 2>&1; then
    echo "Venus OS svlogd command not found; aborting"
    exit 1
fi

mkdir -p "$APP/vendor" "$APP/etc"

# Preserve existing user configuration on upgrades; initialize only on first install.
if [ ! -f "$APP/etc/jk-bms-monitor" ]; then
    cp "$APP/etc/jk-bms-monitor.default" "$APP/etc/jk-bms-monitor"
fi

# Install pinned runtime dependencies into the application's own vendor directory.
python3 -m pip install --disable-pip-version-check --no-cache-dir --upgrade --target "$APP/vendor" -r "$APP/requirements.txt"

# Install the persistent boot helper and register it in rc.local idempotently.
chmod 755 "$APP/boot"
if [ ! -f "$RC_LOCAL" ]; then
    printf '#!/bin/sh\n' > "$RC_LOCAL"
    chmod 755 "$RC_LOCAL"
fi
if ! grep -Fq "$BOOT_HOOK" "$RC_LOCAL"; then
    TMP_RC="$RC_LOCAL.tmp"
    awk -v hook="$BOOT_HOOK" '
        /^exit 0$/ && !inserted {
            print "# JK-BMS-Monitor persistent service startup"
            print hook
            inserted=1
        }
        { print }
        END {
            if (!inserted) {
                print "# JK-BMS-Monitor persistent service startup"
                print hook
            }
        }
    ' "$RC_LOCAL" > "$TMP_RC"
    mv "$TMP_RC" "$RC_LOCAL"
fi

# Provision the live service and start it without requiring a reboot.
"$BOOT_HOOK"

echo "JK-BMS-Monitor installed; service started and boot startup registered."
echo "Configuration: $APP/etc/jk-bms-monitor"
echo "Logs: /data/log/jk-bms-monitor"
