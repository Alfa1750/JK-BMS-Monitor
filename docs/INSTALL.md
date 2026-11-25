# Installation and configuration — v0.1.2 test candidate

Install/update through Venus OS PackageManager on the isolated test GX.

The package installer automatically:
- Operates in the PackageManager application directory, `/data/JK-BMS-Monitor`.
- Creates the configuration from `etc/jk-bms-monitor.default` only if it is missing.
- Installs pinned BLE dependencies into `/data/JK-BMS-Monitor/vendor` using pip's `--target`, not into system Python.
- Creates the service wrapper.

A network connection is required to download dependencies. The installer does not automatically restart the service or reboot.

Configuration file: `/data/JK-BMS-Monitor/etc/jk-bms-monitor`

For BLE: `JKMONITOR_MODE=ble` and `JKMONITOR_BLE_ADDRESS=<BMS MAC>`.

For UART: `JKMONITOR_MODE=serial`, `JKMONITOR_PORT=/dev/ttyUSB0` and `JKMONITOR_BAUD=115200`.

After installation, configure the MAC and perform any service restart only when explicitly directed by the user. Validate BLE on the isolated test Pi first.
