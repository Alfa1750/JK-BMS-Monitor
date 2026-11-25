# Project Rules — JK-BMS-Monitor

## Mission and safety boundary
This project is a read-only JK-BMS telemetry monitor for Venus OS. It is not a BMS control integration.

The non-negotiable design goal is that this service must not influence Victron charging, discharging, DVCC, MPPT network mode, or battery control decisions. This must be demonstrated through code inspection and documented tests before any claim of safety or independence is made.

## Allowed
- Read telemetry from the JK-BMS.
- Parse and normalize monitoring data.
- Publish appropriate monitoring-only D-Bus values.
- Provide logs, diagnostics, and installation/removal documentation.

## Forbidden unless this project is explicitly re-scoped and approved
- BMS configuration writes or commands.
- Charge/discharge control or protection actions.
- Publishing CVL, CCL, DCL, charge/discharge limits, control flags, or equivalent control signals.
- Properties or service patterns intended to trigger BMS-controlled behavior in Victron system components.
- Modifying live Raspberry Pi/Venus OS systems, starting builds, flashing, installing, or running services without explicit user approval.

## Development workflow
- Review current project docs and repository state before each significant change.
- Research upstream sources carefully; review licensing and attribution before reuse.
- Keep the implementation minimal and isolated.
- Do not assume that setting DVCC off is sufficient to prevent control influence.
- Document hypotheses as hypotheses until verified.
- Never claim a behavior is tested unless the test was actually run and its result recorded.
- The user decides when live-system testing, builds, installs, and service execution occur.
- Record decisions, progress, test results, and open issues in project documentation.

## Required verification
Before deployment, source review and tests must establish:
1. Which D-Bus paths and properties are published.
2. That no control-oriented properties or flags are exposed.
3. That the service does not write commands to the BMS.
4. Whether Venus OS systemcalc or charger services react to the published data.
5. With DVCC disabled and the monitor service running, charger/MPPT behavior remains independent of the monitor service.
6. Removing/stopping the monitor does not create unintended charger behavior.

## Documentation
Keep README.md, docs/PROJECT_STATUS.md, docs/ARCHITECTURE.md, docs/DECISIONS.md and CHANGELOG.md current.
