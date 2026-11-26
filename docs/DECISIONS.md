# Decisions — v0.2.0
- Separate monitor-only project.
- No BMS writes, control limits or control flags.
- JK protocol research/adaptation with attribution and license requirements retained.
- No live device actions without explicit approval.
- v0.2.0 uses generic `com.victronenergy.sensor` namespace rather than battery service to avoid BMS classification; this is not yet GX-verified.
- Existing SetupHelper lifecycle retained.
