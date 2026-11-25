# Project Status — JK-BMS-Monitor

Version: v0.1.0 test candidate

## Package format correction
- Added the required root `version`, `gitHubInfo`, and SetupHelper `setup` entry point.
- Added a service template in `services/jk-bms-monitor/run`, using the package launcher.
- Updated README and packaging documentation to describe PackageManager recognition and the verification boundary.
- This correction is based on SetupHelper PackageDevelopmentGuidelines (v6.0): root metadata and setup entry point; services managed from `services/`.

## Not yet verified
- PackageManager GitHub detection and download.
- Package installation/uninstallation via PackageManager.
- Service registration, startup and removal on Venus OS.
- D-Bus behavior, systemcalc selection, charger/MPPT independence, JK serial telemetry.

No device actions or tests were performed during this correction. Test only on an isolated Venus OS device before camper deployment.
