# Decisions

## D-001 — Separate read-only service
Accepted 2026-11-25: separate project from VantourerDisplayBridge.

## D-002 — Strict control exclusion
Accepted: no BMS writes, control limits or control-related D-Bus flags.

## D-003 — Upstream research and licensing
Accepted: dbus-serialbattery used as protocol research; provenance recorded and AGPL-compatible licensing adopted.

## D-004 — No live actions without approval
Accepted: no builds, installs, service starts, flashes or Pi changes without explicit approval.

## D-005 — Omit systemcalc BMS marker
Accepted: omit /Info/MaxChargeVoltage; source inspection shows systemcalc BatteryService uses it to classify a service as BMS.

## D-006 — Serial-only v0.1
Historical decision; BLE was subsequently added in v0.1.1.

## D-007 — App-local Python dependencies
Accepted for v0.1.2 test candidate: pin Bleak and dbus-fast and install via pip --target into the application's vendor folder, avoiding system Python package changes. Target-device installation remains unverified.
