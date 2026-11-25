# v0.1 test plan

No tests have been executed.

1. Review installer, configuration and package script.
2. Test on isolated Venus OS, not the camper.
3. Confirm service starts and D-Bus identity appears.
4. Inspect published paths and ensure prohibited control paths are absent.
5. Compare telemetry with JK app and validate serial protocol/baud/port.
6. Verify systemcalc battery selection and behavior.
7. Observe charger/MPPT behavior under a safe test plan.
8. Stop/remove monitor and verify unaffected operation.
9. Test disconnect/reconnect, checksum errors, timeouts and parser boundary cases.
10. Review install/uninstall idempotency and service-manager behavior.
