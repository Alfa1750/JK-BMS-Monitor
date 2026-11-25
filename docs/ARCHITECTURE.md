# Architecture — v0.1

Serial JK-BMS → bounded status request → frame/checksum validation → reduced parser → D-Bus monitor.

Telemetry scope: voltage/current/power, SOC, capacity, cells/count/min/max/spread, temperatures, cycles/version and communication health.

Control exclusion: no BMS write/configuration functions and no control-limit paths or flags. Specifically omit /Info/MaxChargeVoltage (systemcalc BatteryService marker), /Info/MaxChargeCurrent, /Info/MaxDischargeCurrent and /Capabilities/ChargeVoltageControl.

No on-device tests have been run. D-Bus behavior and charger/MPPT independence remain unproven.
