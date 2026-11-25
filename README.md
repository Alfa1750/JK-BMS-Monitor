# JK-BMS-Monitor

Read-only JK-BMS telemetry monitor for Venus OS.

## PackageManager package
This repository is structured as a SetupHelper / Venus OS PackageManager package. Required package metadata is at repository root (`version`, `gitHubInfo`, executable `setup`); the service template is under `services/jk-bms-monitor/`.

Add this repository in PackageManager using GitHub user `Alfa1750` and branch `main`. PackageManager recognition/download and installation are not yet verified on a GX device. **Do not install on the camper before isolated-device testing.**

## Scope
Telemetry only: voltage/current/power, SOC, capacity, cell voltages and temperatures.

## Excluded
No BMS writes; no CVL/CCL/DCL; no `/Info/MaxChargeVoltage`, `/Info/MaxChargeCurrent`, `/Info/MaxDischargeCurrent` or `/Capabilities/ChargeVoltageControl`.

## Validation status
The package structure is being corrected for SetupHelper. No on-device install, service start, D-Bus verification or charger/MPPT independence test has been performed. See `docs/TEST_PLAN.md`.
