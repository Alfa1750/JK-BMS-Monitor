# Architecture — v0.1.5

## Data path
JK-BMS (BLE or UART) → transport selector → protocol reader/parser → read-only telemetry normalization → D-Bus monitor.

## BLE dependencies
Bleak 0.21.1 and dbus-fast 2.20.0 are pinned in `requirements.txt`. The package launcher installs them app-locally under `/data/JK-BMS-Monitor/vendor` using pip if imports are missing. Network access is required for that bootstrap.

## Configuration and service lifecycle
User configuration is stored in `/data/JK-BMS-Monitor/config/jk-bms-monitor`, outside the PackageManager payload. SetupHelper manages service lifecycle and logger templates.

## Logging
The service logger script uses `svlogd` and writes logs to `/data/log/jk-bms-monitor`.

## Telemetry
Voltage/current/power, SOC, capacity, cells/count/min/max/spread, temperatures, cycles/version and communication health.

## Read-failure behavior
On a read exception, the monitor marks disconnected/error and clears telemetry values so stale readings are not retained as current.

## Control exclusion
No BMS write/configuration functions and no control-limit paths or flags. Specifically omit /Info/MaxChargeVoltage (systemcalc BatteryService marker), /Info/MaxChargeCurrent, /Info/MaxDischargeCurrent and /Capabilities/ChargeVoltageControl.

Service lifecycle, dependency bootstrap, D-Bus behavior and charger/MPPT independence remain unverified on-device.
