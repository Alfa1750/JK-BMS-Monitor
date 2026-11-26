# Installation and configuration — v0.1.5 test candidate

Install or update through Venus OS PackageManager using SetupHelper.

SetupHelper manages service installation, update, startup and removal using the package service directory. No custom `/data/rc.local` hook is used.

The service launcher creates `/data/JK-BMS-Monitor/config/jk-bms-monitor` from a prior configuration when available, or from `etc/jk-bms-monitor.default`. The configuration is outside the package payload. It checks for Bleak and dbus-fast; if absent, it installs the pinned requirements into `vendor` using pip `--target`. Network access is required for that first bootstrap.

Configuration file: `/data/JK-BMS-Monitor/config/jk-bms-monitor`.

For BLE: `JKMONITOR_MODE=ble` and `JKMONITOR_BLE_ADDRESS=<BMS MAC>`.

For UART: `JKMONITOR_MODE=serial`, `JKMONITOR_PORT=/dev/ttyUSB0` and `JKMONITOR_BAUD=115200`.

Logs are intended to be captured under `/data/log/jk-bms-monitor` by the SetupHelper-installed logger service.

On read failures, telemetry is cleared and the service marks itself disconnected/error.

This package is a test candidate. PackageManager, SetupHelper lifecycle, dependency bootstrap, BLE/UART operation, D-Bus behavior and charger independence remain unverified on-device.
