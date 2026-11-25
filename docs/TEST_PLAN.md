# v0.1 test plan

No tests have been run.

1. Review installer and configuration.
2. Test only on an isolated Venus OS unit, not the camper installation.
3. Confirm service starts and D-Bus identity appears.
4. Inspect all published D-Bus paths and verify excluded control paths remain absent.
5. Validate telemetry against JK app readings.
6. Verify systemcalc selection and behavior; ensure no BMS-control role is triggered.
7. Observe MPPT/charger behavior under a safe test plan with service present.
8. Stop/remove monitor and verify behavior is unchanged.
9. Test disconnect/reconnect, checksum failures, and serial timeout handling.
10. Review install/uninstall idempotency and service-manager behavior.
