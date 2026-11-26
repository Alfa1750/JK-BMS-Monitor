# Installation — v0.2.0

Install/update/remove through Venus OS PackageManager using SetupHelper. Persistent configuration: `/data/JK-BMS-Monitor/config/jk-bms-monitor`.

BLE: `JKMONITOR_MODE=ble`, set `JKMONITOR_BLE_ADDRESS`.
UART: `JKMONITOR_MODE=serial`, set `JKMONITOR_PORT` and `JKMONITOR_BAUD`.

This release publishes a generic sensor service, not a battery service. Its intended isolation from systemcalc/DVCC is unverified on the GX device; do not treat as field-validated.
