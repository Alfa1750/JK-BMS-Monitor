# JK-BMS-Monitor

A strictly read-only JK-BMS battery monitor service for Venus OS.

## Goal

Expose JK-BMS telemetry to Venus OS over D-Bus for monitoring, while deliberately avoiding any role in battery charge/discharge control.

**Safety design objective:** this service must not cause Victron system components, including MPPT chargers, to adopt BMS-controlled charging or discharge limits or modes. This is an objective to be verified through source review and testing—not yet a proven property.

## Scope

- Read JK-BMS telemetry and expose monitoring values only.
- Support the intended JK-BMS connection method(s), beginning with serial.
- Reuse and adapt upstream communication/parsing approaches only after reviewing upstream code, license, and required attribution.
- Keep the monitor service separate from other camper/display projects.

## Explicit exclusions

- No CVL, CCL, DCL, charge-voltage/current-limit, discharge-current-limit, or equivalent control outputs.
- No writes/commands to the BMS for configuration, switching, charging, discharging, or protection control.
- No D-Bus properties, flags, or service behavior intended to signal battery-control authority to Victron system components.
- No automatic installation, build, flashing, or live-system changes as part of development without explicit user approval.

## Project status

Initial repository setup and design constraints. Implementation and behavior validation are pending.

See [AGENTS.md](AGENTS.md), [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), [docs/PROJECT_STATUS.md](docs/PROJECT_STATUS.md), and [CHANGELOG.md](CHANGELOG.md).
