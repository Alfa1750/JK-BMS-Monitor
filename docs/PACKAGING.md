# SetupHelper / PackageManager packaging — v0.1.5

The package uses the SetupHelper standard action flow:

- `version`: package version
- `gitHubInfo`: repository owner and branch
- `setup`: executable entry point, sets `standardPromptAndActions='yes'` and sources SetupHelper `IncludeHelpers`
- `services/jk-bms-monitor/run` and `services/jk-bms-monitor/log/run`: service templates managed by SetupHelper
- `run`: package launcher
- `monitor/` and `etc/jk-bms-monitor.default`: monitor code and configuration template

SetupHelper manages service lifecycle. User configuration is kept outside the package payload in `/data/JK-BMS-Monitor/config`.

BLE requirements are pinned in `requirements.txt`; the launcher installs them app-locally into `vendor` if missing, then executes the monitor. Bootstrap requires network access.

Static review only; PackageManager recognition, download, installation, service lifecycle, dependency bootstrap, D-Bus behavior and telemetry remain unverified on Venus OS.
