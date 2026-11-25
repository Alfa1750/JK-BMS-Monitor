# JK-BMS-Monitor

Read-only JK-BMS monitor for Venus OS. **v0.1.3 test candidate** supports BLE and UART transport selection.

## Configure
Edit `/data/JK-BMS-Monitor/etc/jk-bms-monitor`:
- `JKMONITOR_MODE=ble` (default) or `serial`
- BLE: set `JKMONITOR_BLE_ADDRESS` to the JK BMS MAC address
- UART: set `JKMONITOR_PORT` and `JKMONITOR_BAUD`

The monitor publishes telemetry only and does not expose Victron control-limit paths. BLE uses protocol read requests only; no BMS configuration/control register implementation is included.

## Installation, startup and logs
Package installation automatically installs pinned BLE Python packages (Bleak and dbus-fast) into the application's own `vendor` directory, preserves the existing configuration, provisions and starts the service, and registers a persistent startup hook in `/data/rc.local`. A user should only need to enter the MAC address and restart the GX if needed; no manual service commands are intended.

Service output is captured under `/data/log/jk-bms-monitor`. A network connection is required during installation to retrieve Python dependencies.

## Important test boundary
v0.1.3 is a test candidate. Installer/service lifecycle, boot persistence, log capture, BLE protocol compatibility, Bluetooth permissions, reconnect behavior, D-Bus paths and systemcalc/charger independence still require user-controlled validation on an isolated test device.
