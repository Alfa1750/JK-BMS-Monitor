# JK-BMS-Monitor

Read-only JK-BMS monitor for Venus OS. **v0.1.2 test candidate** supports BLE and UART transport selection.

## Configure
Edit `/data/JK-BMS-Monitor/etc/jk-bms-monitor`:
- `JKMONITOR_MODE=ble` (default) or `serial`
- BLE: set `JKMONITOR_BLE_ADDRESS` to the JK BMS MAC address
- UART: set `JKMONITOR_PORT` and `JKMONITOR_BAUD`

The monitor publishes telemetry only and does not expose Victron control-limit paths. BLE uses protocol read requests only; no BMS configuration/control register implementation is included.

## Installation and dependencies
Package installation automatically installs pinned BLE Python packages (Bleak and dbus-fast) into the application's own `vendor` directory. It does not install these packages into system Python and does not require the user to run pip manually. A default configuration template is used only if the configuration is missing.

A network connection is required during installation to retrieve Python dependencies. Installation does not automatically restart the service or reboot the GX.

## Important test boundary
v0.1.2 is a test candidate. BLE protocol compatibility, runtime dependency installation on the test GX, Bluetooth permissions, reconnect behavior, D-Bus paths and systemcalc/charger independence still require user-controlled validation on an isolated test device.
