# Architecture — v0.1.3

## Data path
JK-BMS (BLE or UART) → transport selector → protocol reader/parser → read-only telemetry normalization → D-Bus monitor.

## BLE dependencies
Bleak 0.21.1 and dbus-fast 2.20.0 are pinned in `requirements.txt` and installed app-locally under `/data/JK-BMS-Monitor/vendor`. Runtime sets `PYTHONPATH` to vendor and monitor directories.

## Service lifecycle
Application and configuration remain in `/data/JK-BMS-Monitor`. The installer registers the application boot helper in `/data/rc.local`. On boot the helper recreates the service and log wrappers in Venus OS's live `/service` overlay and requests the service to run. This avoids depending on manually-created volatile service files.

## Logging
The service log sub-process uses `svlogd` and writes to `/data/log/jk-bms-monitor`.

## Telemetry
Voltage/current/power, SOC, capacity, cells/count/min/max/spread, temperatures, cycles/version and communication health.

## Control exclusion
No BMS write/configuration functions and no control-limit paths or flags. Specifically omit /Info/MaxChargeVoltage (systemcalc BatteryService marker), /Info/MaxChargeCurrent, /Info/MaxDischargeCurrent and /Capabilities/ChargeVoltageControl.

Service lifecycle, log behavior, D-Bus behavior and charger/MPPT independence remain unverified on-device.
