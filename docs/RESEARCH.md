# Research notes

- UART parser remains available from v0.1.0.
- BLE read-only subset introduced for v0.1.1, based on JK BLE frame decoding research and upstream `venus-os_dbus-serialbattery` jkbms_brn.py.
- Upstream attribution: https://github.com/mr-manuel/venus-os_dbus-serialbattery (AGPL-3.0).
- The BLE subset uses the characteristic UUID 0000ffe1-0000-1000-8000-00805f9b34fb with handle fallback 4 and parses the 300-byte notification frame. Only request opcodes 0x96 and 0x97 are implemented; upstream configuration/control-writing methods intentionally omitted.
- This port is preliminary. Frame compatibility and BLE stack behavior need isolated Pi validation.
- Monitor still intentionally excludes CVL/CCL/DCL, charge limits, discharge limits and charge-voltage-control paths.
