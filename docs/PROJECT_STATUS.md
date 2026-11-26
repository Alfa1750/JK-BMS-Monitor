# Project Status — JK-BMS-Monitor

## Version 0.1.4 — PackageManager test candidate
- Reworked package setup to use the SetupHelper standard action flow and service-directory lifecycle.
- Removed the custom `/data/rc.local` boot helper/service overlay provisioning approach from the package workflow.
- SetupHelper is expected to install/update/remove the `services/jk-bms-monitor` service from the package service directory.
- Runtime launcher bootstraps pinned BLE dependencies into the package-local `vendor` directory if they are absent, then launches the monitor. This keeps dependency installation outside the SetupHelper setup script's foreground processing.
- Logging is defined in the service's `log/run` script and is intended to use Venus OS `svlogd`.

## Not verified
- PackageManager download/recognition and SetupHelper installation/update/uninstall behavior.
- Service startup and logger behavior on target Venus OS.
- Dependency bootstrap via pip and network behavior.
- BLE protocol/notification framing across JK models; UART operation after transport selection.
- D-Bus/systemcalc/MPPT independence, disconnect/reconnect and telemetry comparison.
- No device installation, service start, reboot or telemetry tests performed by the assistant.
