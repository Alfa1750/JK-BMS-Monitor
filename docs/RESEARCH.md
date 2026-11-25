# Research notes

## BLE dependency and packaging investigation (2026-11-25)
- The v0.1.1 BLE reader imports `bleak`, but the package installer did not provide that dependency. The test GX confirmed `ModuleNotFoundError: No module named 'bleak'`.
- The isolated test GX reported Python 3.12.15 and pip 24.0. No package installation was attempted in this investigation.
- Upstream `mr-manuel/venus-os_dbus-serialbattery` uses BLE via Bleak and documents installing Bleak through its enable/install workflow. Its recent release notes also describe shipping dependencies with the driver. This is reference research only; no upstream files were copied.
- v0.1.2 uses a local pip target in the application's vendor folder to avoid altering Venus OS system Python. Requirements are pinned: Bleak 0.21.1 and dbus-fast 2.20.0.
- This dependency-install approach is not yet verified on the target GX; pip may need network access and may resolve/build platform dependencies.

## Protocol
- BLE read-only subset introduced for v0.1.1, based on JK BLE protocol research and upstream `venus-os_dbus-serialbattery`.
- Attribution: https://github.com/mr-manuel/venus-os_dbus-serialbattery (AGPL-3.0).
- The BLE subset uses characteristic UUID 0000ffe1-0000-1000-8000-00805f9b34fb with handle fallback 4 and parses the 300-byte notification frame. Only request opcodes 0x96 and 0x97 are implemented; upstream configuration/control-writing methods intentionally omitted.
- Frame compatibility and BLE stack behavior still need isolated Pi validation.
- Monitor intentionally excludes CVL/CCL/DCL, charge limits, discharge limits and charge-voltage-control paths.
