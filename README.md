# JK-BMS-Monitor v0.2.0

Read-only JK telemetry monitor for Venus OS, a fresh monitor-only version based on existing JK protocol support and dbus-serialbattery research.

## D-Bus boundary
Publishes as **`com.victronenergy.sensor.jkmonitor`**, not `com.victronenergy.battery`. It is intentionally not registered as a battery/BMS and does not publish charge/discharge limits, DVCC flags or control capabilities. This separation is intended to keep it outside systemcalc battery selection and charger control, but requires GX validation.

## Telemetry
Voltage/current/power, SOC, cell voltages/count/spread, temperatures, cycles, firmware and connection status. UART remaining-capacity data is not currently provided by this parser.

## Installation and configuration
Install/update/remove using the existing SetupHelper PackageManager flow. Persistent configuration is in `/data/JK-BMS-Monitor/config/jk-bms-monitor`.
- `JKMONITOR_MODE=ble` or `serial`
- BLE: `JKMONITOR_BLE_ADDRESS`
- UART: `JKMONITOR_PORT`, `JKMONITOR_BAUD`
- Optional: `JKMONITOR_INSTANCE`, `JKMONITOR_POLL_SECONDS`

No GX installation, service execution, BLE/UART live testing or hardware changes have been performed.
