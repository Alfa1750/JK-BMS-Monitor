# SetupHelper / PackageManager packaging

The repository now follows the package recognition structure documented by SetupHelper:

- `version`: package version string
- `gitHubInfo`: `owner:branch` metadata
- `setup`: executable SetupHelper entry point, sourcing IncludeHelpers
- `services/jk-bms-monitor/run`: service template installed and tracked by SetupHelper
- `run`: package-owned launcher
- `monitor/` and `etc/`: monitor code and configuration

SetupHelper v6+ automatically manages service directories located in `services/`. The service template runs the package launcher under `/data/JK-BMS-Monitor`. The setup entry point delegates package install/uninstall handling to SetupHelper CommonResources.

Static repository corrections are committed, but PackageManager recognition, download, installation, service lifecycle, D-Bus behavior and telemetry remain unverified on Venus OS. Do not consider this tested/ready for live deployment until the isolated-device test plan is completed.
