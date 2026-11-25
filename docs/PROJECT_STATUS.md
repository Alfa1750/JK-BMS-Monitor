# Project Status — JK-BMS-Monitor

## Version 0.1.3 — test candidate
- Corrected the service lifecycle design: installer provisions and starts the service, eliminating the manual `svc -u` step from normal user workflow.
- Persistent startup helper stored in the application data directory and registered idempotently in `/data/rc.local`.
- Helper recreates service and log wrappers in live `/service` overlay and starts it.
- Supervised logs configured under `/data/log/jk-bms-monitor`.
- Uninstaller stops the service and removes startup hook and application log directory.
- Existing configuration is preserved on upgrade.

## Not verified
- PackageManager invokes the updated installer as intended.
- Startup hook and service persistence across GX reboot/firmware lifecycle.
- Log service behavior and log rotation on target Venus OS.
- BLE protocol/notification framing across JK models.
- UART operation after transport selection.
- D-Bus/systemcalc/MPPT independence, disconnect/reconnect and telemetry comparison.
- No live v0.1.3 installation, service start, reboot or device tests performed by the assistant.
