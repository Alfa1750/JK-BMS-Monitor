# JK-BMS-Monitor

Read-only JK-BMS monitor for Venus OS. Version 0.1.1 candidate supports BLE and UART transport selection.

## Configure
Edit `/data/JK-BMS-Monitor/etc/jk-bms-monitor`:
- `JKMONITOR_MODE=ble` (default) or `serial`
- BLE: set `JKMONITOR_BLE_ADDRESS` to the JK BMS MAC address
- UART: set `JKMONITOR_PORT` and `JKMONITOR_BAUD`

The monitor publishes telemetry only and does not expose Victron control-limit paths. BLE uses read-request protocol frames only; no BMS configuration/control register implementation is included. UART uses the serial reader.

## PackageManager
Package metadata is at repository root. Recognition and install lifecycle have been observed on the isolated test Pi for v0.1.0. v0.1.1 runtime behavior remains to be tested there.

## Important test boundary
BLE dependencies (Bleak), BlueZ permissions, protocol compatibility, reconnect behavior, D-Bus paths and systemcalc/charger independence have not yet been validated on-device. Treat v0.1.1 as a test candidate, not proven-safe deployment.
