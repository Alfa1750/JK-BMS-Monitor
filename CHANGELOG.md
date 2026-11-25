# Changelog

## v0.1.3 — 2026-11-25 test candidate
- Fix service lifecycle: installer provisions and starts the live service automatically instead of requiring manual `svc -u`.
- Registers an idempotent startup hook in `/data/rc.local` so service provisioning/startup is restored at boot.
- Adds a supervised log service using `svlogd`, writing logs to `/data/log/jk-bms-monitor`.
- Uninstaller stops the service and removes the boot hook and application logs.
- No device-side v0.1.3 installation, boot, log or BLE test has been performed.

## v0.1.2 — 2026-11-25 test candidate
- Corrected application/configuration path to `/data/JK-BMS-Monitor`.
- Installer installs pinned Bleak and dbus-fast dependencies into application-local `vendor` directory using pip target; system Python packages are not modified.
- Runtime sets app-local vendor path for BLE imports.
- Upgrade preserves existing configuration.
- Updated package scripts, documentation and test plan.
- No install, dependency resolution, BLE runtime, D-Bus or charger-independence tests performed on-device.

## v0.1.1 — 2026-11-25 test candidate
- Added BLE read-only transport alongside retained UART serial transport.
- BLE address and transport selection configuration.
- Updated D-Bus publisher to use selected transport.
- No on-device tests, dependency installation, service start or charger-independence validation performed.

## v0.1.0
- Initial serial telemetry parser, D-Bus publisher and package structure.
