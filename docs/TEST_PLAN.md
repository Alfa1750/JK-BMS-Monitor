# Test plan — v0.1.1 test candidate

No tests or live system actions have been performed by the assistant.

1. Install/update on isolated test GX only.
2. Confirm whether Python Bleak is available; do not install dependencies without approval.
3. Configure BLE mode and MAC address in `/data/JK-BMS-Monitor/etc/jk-bms-monitor`.
4. User-controlled service restart; verify connection and telemetry against JK app.
5. Validate BLE frame assembly, checksum, cells, current, SOC, capacity and temperature values.
6. Test disconnect/reconnect and service restart.
7. Confirm serial mode still works using `JKMONITOR_MODE=serial`.
8. Inspect D-Bus paths; no control paths or DVCC/CVL/CCL/DCL values.
9. Observe systemcalc and MPPT behavior under isolated/safe test procedure.
10. Uninstall and verify service/files cleanup.
