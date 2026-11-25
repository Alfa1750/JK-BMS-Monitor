# Installation and configuration — v0.1.3 test candidate

Install/update through Venus OS PackageManager on the isolated test GX.

The installer:
- Operates in the PackageManager application directory, `/data/JK-BMS-Monitor`.
- Creates the configuration from `etc/jk-bms-monitor.default` only if it is missing.
- Installs pinned BLE dependencies app-locally under `vendor`.
- Registers the persistent startup helper in `/data/rc.local` idempotently.
- Provisions and starts the service automatically.
- Installs supervised logging to `/data/log/jk-bms-monitor`.

A network connection is required to download dependencies.

Configuration file: `/data/JK-BMS-Monitor/etc/jk-bms-monitor`

For BLE: `JKMONITOR_MODE=ble` and `JKMONITOR_BLE_ADDRESS=<BMS MAC>`.

For UART: `JKMONITOR_MODE=serial`, `JKMONITOR_PORT=/dev/ttyUSB0` and `JKMONITOR_BAUD=115200`.

Expected user workflow: install via PackageManager, enter the MAC address, then restart the GX only if needed. Manual service commands are not intended for normal use.

This candidate's automatic service lifecycle, boot hook and logging remain unverified on-device.
