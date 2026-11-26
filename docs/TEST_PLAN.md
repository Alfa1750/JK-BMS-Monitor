# Test plan — v0.2.0
1. PackageManager recognition and SetupHelper install/update/remove.
2. Verify service is `com.victronenergy.sensor.jkmonitor`, never `com.victronenergy.battery.*`.
3. Inspect D-Bus for absence of battery-control limits, flags and DVCC control capabilities.
4. Verify systemcalc does not select it as battery/BMS.
5. Confirm MPPT/charger behavior is unchanged while connected, disconnected, after Pi reboot and service stop.
6. Validate BLE telemetry and reconnection.
7. Validate UART telemetry.
8. Validate display visibility and stale-data clearing.
9. Verify uninstall leaves no control-related changes.
None of these target tests have yet been executed.
