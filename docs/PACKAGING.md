# SetupHelper / PackageManager packaging — v0.1.4

The package uses the SetupHelper standard package action flow:

- `version`: package version
- `gitHubInfo`: repository owner and branch
- `setup`: executable entry point, sets `standardPromptAndActions='yes'` and sources SetupHelper `IncludeHelpers`
- `services/jk-bms-monitor/run` and `services/jk-bms-monitor/log/run`: service templates managed by SetupHelper
- `run`: package launcher
- `monitor/` and `etc/`: monitor code and configuration

SetupHelper is responsible for installing/updating/removing the package service in the persistent service directory and active service location. The package does not manually create `/service`, copy service definitions at boot, or add a `/data/rc.local` hook.

BLE requirements are pinned in `requirements.txt`. The service launcher installs them app-locally into `vendor` if the imports are missing, then executes the monitor. Dependency installation is performed during service startup rather than inside the SetupHelper setup script.

Static repository review only; PackageManager recognition, download, installation, service lifecycle, logger behavior, dependency bootstrap, D-Bus behavior and telemetry remain unverified on Venus OS.
