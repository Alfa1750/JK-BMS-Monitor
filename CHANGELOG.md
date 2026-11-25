# Changelog

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
