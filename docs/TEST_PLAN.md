# Test plan — v0.1.4 test candidate

No v0.1.4 device test has been performed by the assistant.

1. Update/install v0.1.4 through PackageManager on the isolated test GX.
2. Verify SetupHelper handles the package and installs the service into persistent and active service locations.
3. Verify service/logger startup and dependency bootstrap; confirm pinned dependencies are installed app-locally and system Python is not modified.
4. Set BLE mode and MAC in `/data/JK-BMS-Monitor/etc/jk-bms-monitor`.
5. Verify telemetry and logs under `/data/log/jk-bms-monitor`.
6. Reboot the GX under the user's control and verify automatic service startup.
7. Validate BLE frame assembly, checksum, cells, current, SOC, capacity and temperature values against JK app.
8. Test disconnect/reconnect and service restart behavior.
9. Confirm serial mode still works using `JKMONITOR_MODE=serial`.
10. Inspect D-Bus paths; no control paths or DVCC/CVL/CCL/DCL values.
11. Observe systemcalc and MPPT behavior under isolated/safe test procedure.
12. Uninstall through PackageManager and verify service removal and retained/removed app data behavior.
