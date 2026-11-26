# Architecture — v0.1.4

## Data path
JK-BMS (BLE or UART) → transport selector → protocol reader/parser → read-only telemetry normalization → D-Bus monitor.

## BLE dependencies
Bleak 0.21.1 and dbus-fast 2.20.0 are pinned in `requirements.txt`. The package launcher checks imports and installs them app-locally under `/data/JK-BMS-Monitor/vendor` using pip `--target` only if missing. It prepends the vendor and monitor directories to `PYTHONPATH`.

## Configuration
The runtime config is stored in `/data/JK-BMS-Monitor/config/jk-bms-monitor`, outside the PackageManager payload. The launcher migrates an older `etc/jk-bms-monitor` file when present or copies the default template on first startup.

## Service lifecycle
The package `setup` entrypoint delegates the standard install/uninstall flow to SetupHelper. The service definition is in `services/jk-bms-monitor`; SetupHelper manages the persistent `/opt/victronenergy/service` and active `/service` locations. The package no longer uses `/data/rc.local` or a custom service-copy boot helper.

## Logging
The service logger script uses `svlogd` and writes logs to `/data/log/jk-bms-monitor`.

## Telemetry
Voltage/current/power, SOC, capacity, cells/count/min/max/spread, temperatures, cycles/version and communication health.

## Control exclusion
No BMS write/configuration functions and no control-limit paths or flags. Specifically omit /Info/MaxChargeVoltage (systemcalc BatteryService marker), /Info/MaxChargeCurrent, /Info/MaxDischargeCurrent and /Capabilities/ChargeVoltageControl.

Service lifecycle, dependency bootstrap, log behavior, D-Bus behavior and charger/MPPT independence remain unverified on-device.
