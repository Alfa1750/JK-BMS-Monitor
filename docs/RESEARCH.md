# Research report — v0.1

Date: 2026-11-25

## JK serial protocol
The maintained dbus-serialbattery upstream has a JK serial reader that sends a status request, validates the response frame and checksum, and extracts tagged telemetry. Relevant telemetry includes cell voltage, temperature, battery voltage/current, SOC, capacity and firmware/version data. It also handles limit and protection fields, which are intentionally excluded from this monitor.

The upstream project is AGPLv3. This project adopts AGPL-3.0-or-later for this initial protocol-derived implementation, with attribution. Licensing and provenance must be reviewed before distribution.

## Victron systemcalc source inspection
The systemcalc BatteryService source classifies battery services as BMS when /Info/MaxChargeVoltage is present. The battery-service selection logic also uses this marker in selection ranking. v0.1 therefore intentionally omits that marker and other control paths.

Excluded properties include /Info/MaxChargeVoltage, /Info/MaxChargeCurrent, /Info/MaxDischargeCurrent, /Capabilities/ChargeVoltageControl and any CVL/CCL/DCL/control signal.

This precaution is not proof of charger independence: the complete D-Bus consumer behavior and real systemcalc/DVCC/MPPT response must still be tested on an isolated system.

## Install approach
A preliminary installer and runit-style service wrapper are provided. They have not been executed. The installer assumes Venus OS and its bundled velib_python path, and does not restart or reboot services.

## Sources
- https://github.com/mr-manuel/venus-os_dbus-serialbattery
- https://github.com/victronenergy/dbus-systemcalc-py
- https://github.com/victronenergy/venus/wiki/dbus/
