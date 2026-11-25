# Project Status — JK-BMS-Monitor

## Version 0.1.1
- Added transport selector for BLE and UART serial.
- BLE reader added as a reduced read-only JK protocol subset; only protocol read requests (settings/device info request opcodes) are implemented, no control/configuration writes.
- Configuration now selects BLE or serial, BLE MAC configurable.
- D-Bus publisher updated for telemetry from either transport and version marker 0.1.1.

## Not verified
- Runtime compatibility and installed Bleak availability on Venus OS.
- BLE protocol/notification framing across supported JK models.
- UART operation after transport selection.
- Service lifecycle/restart after configuration.
- D-Bus/systemcalc/MPPT independence, disconnect/reconnect and telemetry comparison.
- No build, tests, installation, service start or live device actions performed by the assistant.
