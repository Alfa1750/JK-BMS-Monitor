# JK-BMS-Monitor

Read-only JK-BMS telemetry monitor for Venus OS. **v0.1.5 test candidate** supports BLE and UART transport selection.

## Configure
Edit `/data/JK-BMS-Monitor/config/jk-bms-monitor`:
- `JKMONITOR_MODE=ble` (default) or `serial`
- BLE: set `JKMONITOR_BLE_ADDRESS` to the JK BMS MAC address
- UART: set `JKMONITOR_PORT` and `JKMONITOR_BAUD`

The monitor publishes telemetry only and does not expose Victron control-limit paths. BLE protocol requests remain read-only; no BMS configuration/control register implementation is included.

## PackageManager installation
Install/update through Venus OS PackageManager with SetupHelper. SetupHelper manages service lifecycle. Dependencies Bleak and dbus-fast are pinned and bootstrapped into the application-local vendor directory on first service start (network access is required). User configuration remains outside the package payload.

## v0.1.5 change
On a telemetry read failure, the monitor now clears the telemetry values it previously published, rather than leaving old values visible as if they were current. It also updates the published process version to 0.1.5.

## Test boundary
Static review only; no target GX installation, service startup, BLE/UART operation, D-Bus/systemcalc behavior or charger independence tests have been performed.
