# Project Status — JK-BMS-Monitor

## Version 0.1.5 — test candidate
- Retains v0.1.4 SetupHelper package/service flow and app-local pinned BLE dependency bootstrap.
- On telemetry read errors, publishes disconnected/error state and clears telemetry values to prevent stale readings being presented as current.
- Process version path reports 0.1.5.
- Strict read-only boundary retained; no control paths or BMS write functions added.

## Not verified
- PackageManager recognition and SetupHelper install/update/uninstall behavior.
- Service startup and logger behavior on target Venus OS.
- Dependency bootstrap via pip, network behavior, BLE/UART protocol operation.
- D-Bus/systemcalc/MPPT independence, disconnect/reconnect and telemetry comparison.
- No device installation, service start, reboot or telemetry tests performed by the assistant.
