# Changelog

## v0.1.0 — 2026-11-25 (test candidate)
- Initial reduced JK serial telemetry parser/reader.
- Preliminary Venus OS D-Bus service and installer scripts.
- Research, test plan, licensing and attribution docs.
- Control paths and BMS commands excluded.
- No tests, builds, package creation, installs or live-system actions performed.

### Packaging correction
- Added root SetupHelper package metadata (`version`, `gitHubInfo`, `setup`).
- Added service template in `services/jk-bms-monitor/run` for PackageManager's automatic service management.
- Updated packaging documentation and project status.
- PackageManager recognition and on-device install remain unverified.
