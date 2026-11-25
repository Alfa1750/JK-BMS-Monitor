# Test plan — v0.1.2 test candidate

No installation, build or live device test has been performed by the assistant.

1. Install/update v0.1.2 through PackageManager on the isolated test GX.
2. Verify PackageManager invokes the package installer and installs pinned Bleak and dbus-fast under `/data/JK-BMS-Monitor/vendor`; no user pip command should be needed.
3. Confirm manually edited configuration is preserved and created from the default template only if absent.
4. Set BLE mode and MAC in `/data/JK-BMS-Monitor/etc/jk-bms-monitor`.
5. User-controlled service restart; verify connection and telemetry against JK app.
6. Validate BLE frame assembly, checksum, cells, current, SOC, capacity and temperature values.
7. Test disconnect/reconnect and service restart.
8. Confirm serial mode still works using `JKMONITOR_MODE=serial`.
9. Inspect D-Bus paths; no control paths or DVCC/CVL/CCL/DCL values.
10. Observe systemcalc and MPPT behavior under isolated/safe test procedure.
11. Uninstall and verify service/files cleanup.
