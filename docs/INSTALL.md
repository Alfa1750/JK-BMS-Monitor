# Installation and configuration — v0.1.4 test candidate

Install or update through Venus OS PackageManager using SetupHelper.

SetupHelper's standard action flow installs the package service from `services/jk-bms-monitor` and handles its service lifecycle and removal. The package no longer registers a custom `/data/rc.local` startup hook or manually creates the active `/service` overlay.

On first service start, the launcher creates `/data/JK-BMS-Monitor/config/jk-bms-monitor` from the prior configuration (when available) or from `etc/jk-bms-monitor.default`. This config is outside the PackageManager payload. The launcher checks for Bleak and dbus-fast; if missing, it installs the pinned requirements into `/data/JK-BMS-Monitor/vendor` using pip `--target`, then starts the monitor. Network access is required for that first dependency bootstrap. The system Python package set is not intentionally changed.

Configuration file: `/data/JK-BMS-Monitor/config/jk-bms-monitor`.

For BLE: `JKMONITOR_MODE=ble` and `JKMONITOR_BLE_ADDRESS=<BMS MAC>`.

For UART: `JKMONITOR_MODE=serial`, `JKMONITOR_PORT=/dev/ttyUSB0` and `JKMONITOR_BAUD=115200`.

Logs are intended to be captured under `/data/log/jk-bms-monitor` by the SetupHelper-installed logger service.

This package is a test candidate. PackageManager, SetupHelper service lifecycle, dependency bootstrap, BLE/UART operation, D-Bus behavior and charger independence remain unverified on-device.
