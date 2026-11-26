# Installation and configuration — v0.1.5 test candidate

Install or update through Venus OS PackageManager using SetupHelper.

SetupHelper manages service installation, update, startup and removal using the package service directory. No custom `/data/rc.local` hook is used.

The service launcher creates `/data/JK-BMS-Monitor/config/jk-bms-monitor` from a prior configuration when available, or from `etc/jk-bms-monitor.default`. The configuration is outside the package payload.

On first BLE bootstrap, pip installs pinned Bleak into `vendor` with dependency resolution disabled. A separate bootstrap helper downloads and safely extracts the pure-Python dbus-fast 2.20.0 package into `vendor/dbus_fast`, bypassing its source-build backend. Network access is required. System Python packages are not changed.

Configuration file: `/data/JK-BMS-Monitor/config/jk-bms-monitor`.

For BLE: `JKMONITOR_MODE=ble` and `JKMONITOR_BLE_ADDRESS=<BMS MAC>`.

For UART: `JKMONITOR_MODE=serial`, `JKMONITOR_PORT=/dev/ttyUSB0` and `JKMONITOR_BAUD=115200`.

Logs are intended to be captured under `/data/log/jk-bms-monitor` by the SetupHelper-installed logger service.

On read failures, telemetry is cleared and the service marks itself disconnected/error.

This package is a test candidate. PackageManager, SetupHelper lifecycle, bootstrap download/extraction/import, BLE/UART operation, D-Bus behavior and charger independence remain unverified on-device.
