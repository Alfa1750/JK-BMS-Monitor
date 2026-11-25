# Installation and configuration

Install/update from Venus OS PackageManager on the isolated test GX.

After installation, configure the monitor file:
`/data/JK-BMS-Monitor/etc/jk-bms-monitor`

For BLE:
- `JKMONITOR_MODE=ble`
- `JKMONITOR_BLE_ADDRESS=<BMS MAC>`

For UART:
- `JKMONITOR_MODE=serial`
- `JKMONITOR_PORT=/dev/ttyUSB0`
- `JKMONITOR_BAUD=115200`

Restarting the monitor service is needed after changing the configuration. Only do so after the user explicitly requests the service restart. Confirm BLE support/dependency and behavior on the isolated Pi before considering this validated.
