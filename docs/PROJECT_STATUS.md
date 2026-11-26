# Project Status — JK-BMS-Monitor

## Version 0.1.5 — test candidate
- Retains v0.1.4 SetupHelper package/service flow and app-local BLE dependency bootstrap.
- BLE bootstrap now installs Bleak with pip without dependency/build resolution, then unpacks the pinned pure-Python dbus-fast source package into the app-local vendor directory; this avoids invoking dbus-fast's Poetry/Cython source build backend.
- On telemetry read errors, publishes disconnected/error state and clears telemetry values to prevent stale readings being presented as current.
- Process version path reports 0.1.5.
- Strict read-only boundary retained; no control paths or BMS write functions added.

## Not verified
- PackageManager recognition and SetupHelper install/update/uninstall behavior.
- Service startup and logger behavior on target Venus OS.
- Bootstrap download/extraction/import behavior on target, network behavior, BLE/UART protocol operation.
- D-Bus/systemcalc/MPPT independence, disconnect/reconnect and telemetry comparison.
- No device installation, service start, reboot or telemetry tests performed by the assistant.
