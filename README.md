# JK-BMS-Monitor

Read-only JK-BMS telemetry monitor for Venus OS. **v0.1.5 test candidate** supports BLE and UART transport selection.

## Configure
Edit `/data/JK-BMS-Monitor/config/jk-bms-monitor`:
- `JKMONITOR_MODE=ble` (default) or `serial`
- BLE: set `JKMONITOR_BLE_ADDRESS` to the JK BMS MAC address
- UART: set `JKMONITOR_PORT` and `JKMONITOR_BAUD`

The monitor publishes telemetry only and does not expose Victron control-limit paths. BLE protocol requests remain read-only; no BMS configuration/control register implementation is included.

## PackageManager installation
Install/update through Venus OS PackageManager with SetupHelper. SetupHelper manages service lifecycle. Bleak is pip-installed app-locally with dependency resolution disabled; the pinned pure-Python dbus-fast package is fetched and unpacked separately to bypass its source build backend. Network access is required on first bootstrap. User configuration remains outside the package payload.

## v0.1.5 changes
- On telemetry read failure, clear previously published telemetry values rather than leaving old readings visible.
- Process version is 0.1.5.
- Bootstrap avoids dbus-fast's source build backend.

## Test boundary
Static source review only; no target GX installation, service startup, bootstrap execution, BLE/UART operation, D-Bus/systemcalc behavior or charger independence have been tested.
