# Architecture — JK-BMS-Monitor

## Status
Initial design. No implementation or behavior verification completed yet.

## Intended data flow
JK-BMS (read-only telemetry interface)
→ transport/reader
→ parser and data normalization
→ validation and health reporting
→ minimal D-Bus monitoring service
→ Venus OS monitoring consumers

## Principles
- Read-only at the BMS communication layer.
- Monitoring-only at the D-Bus layer.
- Avoid control-oriented fields, flags, and limits.
- Do not assume D-Bus naming or service conventions are harmless; inspect the systemcalc and charger consumers.
- Minimize the published data set to monitoring values that are demonstrably safe.

## Candidate monitoring data
To be finalized after upstream/source research and D-Bus consumer review:
- Battery voltage
- Battery current
- State of charge (SOC)
- Remaining capacity and total capacity, if supported and reliably derived
- Cell voltages and cell-voltage spread
- Temperatures
- BMS status and communication health
- Monitoring alarms/status only, after checking their semantics and consumer behavior

## Transport
The first implementation target is the JK-BMS serial connection used in the camper. BLE may be considered separately for testing or future compatibility, but it must not complicate the first safe implementation.

## Upstream research
The upstream dbus-serialbattery project is a research reference for transport, parsing, and telemetry techniques. Reuse is conditional on source review, license compliance, attribution, and removing control-related behavior. No upstream code has yet been copied.

## Control isolation
Do not publish charge-voltage limits (CVL), charge-current limits (CCL), discharge-current limits (DCL), control mode flags, or other control-related properties. The precise D-Bus surface must be checked against actual Venus OS consumer code, including systemcalc and charger/MPPT behavior.

## Validation plan
1. Inspect upstream driver implementation and license.
2. Map the relevant D-Bus battery service conventions and consumers in Venus OS.
3. Define a minimal D-Bus contract for monitoring only.
4. Implement isolated transport/parser modules.
5. Perform static/source checks for prohibited control properties and BMS writes.
6. Conduct controlled testing on a test system with no live charger-control risk.
7. Verify MPPT/charger behavior and independence, including monitor stop/removal, before deployment.
8. Document actual test observations and limitations.
