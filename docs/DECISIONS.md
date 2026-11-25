# Decisions — JK-BMS-Monitor

## D-001 — Separate read-only monitoring service
**Date:** 2026-11-25  
**Status:** Accepted

Develop a separate Venus OS service for JK-BMS monitoring, distinct from VantourerDisplayBridge and any control integration.

## D-002 — Strictly exclude control behavior
**Date:** 2026-11-25  
**Status:** Accepted

The service must not send BMS configuration/control commands or expose charge/discharge control limits or control-oriented D-Bus properties/flags. The intended behavior must be verified against Venus OS consumers and testing.

## D-003 — Upstream code is a research reference, not an assumed safe base
**Date:** 2026-11-25  
**Status:** Accepted

Study dbus-serialbattery communication, parsing, and telemetry methods. Reuse is conditional on license review, attribution, and removal/isolation of all control behavior.

## D-004 — No live system actions without user approval
**Date:** 2026-11-25  
**Status:** Accepted

Do not build, install, start, flash, or modify the user's Raspberry Pi/Venus OS system unless explicitly authorized.
