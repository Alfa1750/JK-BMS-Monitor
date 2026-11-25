# JK-BMS-Monitor

Read-only JK-BMS telemetry monitor for Venus OS.

## v0.1.0 — test candidate
Initial serial parser/reader, preliminary D-Bus service and install/uninstall scripts.

**Not validated:** this code has not been executed on Venus OS. Do not deploy to the camper before testing D-Bus behavior and charger/MPPT independence on an isolated device.

## Scope
Telemetry only: voltage/current/power, SOC, capacity, cell voltages and temperatures.

## Excluded
No BMS writes; no CVL/CCL/DCL; no /Info/MaxChargeVoltage, /Info/MaxChargeCurrent, /Info/MaxDischargeCurrent or /Capabilities/ChargeVoltageControl.

## Package candidate
Review install.sh and docs/TEST_PLAN.md first. package.sh creates a source archive. Neither script has been executed. Venus OS package-manager compatibility is not yet validated.
