# JK-BMS-Monitor

Read-only JK-BMS telemetry monitor for Venus OS.

## v0.1.0 — test candidate
Initial serial parser/reader, preliminary D-Bus service and install scripts.

**Not validated:** has not been executed on Venus OS. Do not deploy to the camper before testing D-Bus behavior and charger/MPPT independence on an isolated device.

## Scope
Telemetry only: voltage/current/power, SOC, capacity, cell voltages and temperatures.

## Excluded
No BMS writes; no CVL/CCL/DCL; no /Info/MaxChargeVoltage, /Info/MaxChargeCurrent, /Info/MaxDischargeCurrent or /Capabilities/ChargeVoltageControl.

## Installation
Review install.sh and docs/TEST_PLAN.md first. This is a preliminary script-based installation, not yet a validated Venus OS package-manager archive.
