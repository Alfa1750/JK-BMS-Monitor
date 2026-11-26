# Architecture — v0.1.5

## Data path
JK-BMS (BLE or UART) → transport selector → protocol reader/parser → read-only telemetry normalization → D-Bus monitor.

## BLE dependencies
Bleak 0.21.1 is installed app-locally using pip with dependency resolution disabled. dbus-fast 2.20.0 is downloaded as a source archive and its pure-Python package files are safely extracted by `bootstrap_ble.py`. This bypasses its build backend, avoiding a build toolchain and isolated source build. Network access is required for bootstrap.

## Configuration and service lifecycle
User configuration is stored in `/data/JK-BMS-Monitor/config/jk-bms-monitor`, outside the package payload. SetupHelper manages service lifecycle and logger templates.

## Logging
The service logger script uses `svlogd` and writes logs to `/data/log/jk-bms-monitor`.

## Telemetry
Voltage/current/power, SOC, capacity, cells/count/min/max/spread, temperatures, cycles/version and communication health.

## Read-failure behavior
On a read exception, the monitor marks disconnected/error and clears telemetry values so stale readings are not retained as current.

## Control exclusion
No BMS write/configuration functions and no control-limit paths or flags. Specifically omit /Info/MaxChargeVoltage (systemcalc BatteryService marker), /Info/MaxChargeCurrent, /Info/MaxDischargeCurrent and /Capabilities/ChargeVoltageControl.

Service lifecycle, dependency bootstrap, D-Bus behavior and charger/MPPT independence remain unverified on-device.
