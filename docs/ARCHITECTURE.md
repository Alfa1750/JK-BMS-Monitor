# Architecture — v0.1.2

## Data path
JK-BMS (BLE or UART) → transport selector → protocol reader/parser → read-only telemetry normalization → D-Bus monitor.

## BLE dependencies
Bleak 0.21.1 and dbus-fast 2.20.0 are pinned in `requirements.txt` and installed app-locally under `/data/JK-BMS-Monitor/vendor`. The runtime sets `PYTHONPATH` to this vendor folder and the monitor directory. System Python package installation is not intended.

## Telemetry
Voltage/current/power, SOC, capacity, cells/count/min/max/spread, temperatures, cycles/version and communication health.

## Control exclusion
No BMS write/configuration functions and no control-limit paths or flags. Specifically omit /Info/MaxChargeVoltage (systemcalc BatteryService marker), /Info/MaxChargeCurrent, /Info/MaxDischargeCurrent and /Capabilities/ChargeVoltageControl.

Dependency installation, D-Bus behavior and charger/MPPT independence are not yet tested on-device.
