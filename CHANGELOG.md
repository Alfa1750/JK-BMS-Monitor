# Changelog

## v0.1.5 — 2026-11-26 test candidate
- Clear published telemetry values on read failures, preventing stale measurements from remaining visible while disconnected.
- Updated D-Bus process version to 0.1.5.
- Avoid the dbus-fast source build backend during runtime bootstrap: install Bleak without dependency resolution and unpack dbus-fast 2.20.0's pure-Python source package into the app-local vendor directory.
- Static source review only; no on-device installation, service, BLE/UART or charger-independence tests performed.

## v0.1.4 — 2026-11-26 test candidate
- Replaced the custom boot helper, `/data/rc.local` hook and manual service overlay creation with the SetupHelper standard action/service-directory workflow.
- SetupHelper-managed service and logger templates are packaged under `services/jk-bms-monitor`.
- Runtime launcher bootstraps pinned Bleak and dbus-fast dependencies into the app-local vendor directory when imports are missing.
- User configuration is stored outside the package payload and migrates the prior v0.1.3 config on first startup.
- Updated packaging and test documentation for PackageManager/SetupHelper behavior.
- Static repository review only; no on-device install, service, BLE or charger-independence tests performed.

## v0.1.3 — 2026-11-25 test candidate
- Previous candidate used a custom `/data/rc.local` boot helper and service overlay copying; this approach is superseded in v0.1.4.
- No device-side installation, boot, log or BLE test performed.

## v0.1.2 — 2026-11-25 test candidate
- Corrected application/configuration path to `/data/JK-BMS-Monitor`.
- Installer installs pinned Bleak and dbus-fast dependencies app-locally using pip target.
- Upgrade preserves existing configuration.
- No install, dependency resolution, BLE runtime, D-Bus or charger-independence tests performed on-device.

## v0.1.1 — 2026-11-25 test candidate
- Added BLE read-only transport alongside retained UART serial transport.
- BLE address and transport selection configuration.
- No on-device tests, dependency installation, service start or charger-independence validation performed.

## v0.1.0
- Initial serial telemetry parser, D-Bus publisher and package structure.
