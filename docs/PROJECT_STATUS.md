# Project status — v0.2.0

- Fresh v0.2.0 source line on branch v0.2.0-upstream-monitor.
- Publisher namespace changed to `com.victronenergy.sensor.jkmonitor`, not battery service.
- Read-only JK BLE/UART parsing and telemetry retained.
- No BMS-control paths or flags.
- SetupHelper packaging structure retained.

Static review only. Target installation, service execution, BLE/UART and systemcalc/DVCC/MPPT behavior are not tested. Generic sensor visibility and classification remain unverified.

Validation still required: PackageManager/SetupHelper, service discovery, systemcalc/DVCC selection, MPPT behavior during monitor loss/reboot/stop, live transports, GUI and uninstall.
