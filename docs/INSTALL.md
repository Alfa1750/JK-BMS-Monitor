# Installation and configuration — v0.1.2

Install/update through Venus OS PackageManager on the isolated test GX.

The package installer automatically:
- Copies the monitor files to `/data/JK-BMS-Monitor`.
- Creates the configuration only on first install; upgrades preserve existing configuration.
- Installs pinned BLE dependencies into `/data/JK-BMS-Monitor/vendor` using pip's `--target`, not into system Python.
- Creates the service wrapper.

A network connection is required to download dependencies during install. The installer does not automatically restart the service or reboot.

Configuration file:
`/data/JK-BMS-Monitor/etc/jk-bms-monitor`

For BLE:
- `JKMONITOR_MODE=ble`
- `JKMONITOR_BLE_ADDRESS=<BMS MAC>`

For UART:
- `JKMONITOR_MODE=serial`
- `JKMONITOR_PORT=/dev/ttyUSB0`
- `JKMONITOR_BAUD=115200`

After installation, configure the MAC and then perform any service restart only when explicitly directed by the user. Validate BLE on the isolated test Pi first.
