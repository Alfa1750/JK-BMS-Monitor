# Project Status — JK-BMS-Monitor

## Version 0.1.2 — test candidate
- Application path standardized to `/data/JK-BMS-Monitor`, matching configuration path previously used during test installation.
- Installer now installs pinned runtime dependencies (`bleak==0.21.1`, `dbus-fast==2.20.0`) app-locally in `vendor` using pip target.
- Run script sets `PYTHONPATH` to app-local vendor and monitor directories.
- Upgrade preserves existing user config.
- BLE remains default transport; UART selection retained.
- Package Manager test installation is the next user-controlled step.

## Not verified
- Package Manager invocation of the dependency installer and its success on the isolated GX.
- Pip resolution/download/build behavior on Venus OS Python 3.12 and Pi hardware.
- BLE protocol/notification framing across JK models.
- UART operation after transport selection.
- Service lifecycle/restart after configuration.
- D-Bus/systemcalc/MPPT independence, disconnect/reconnect and telemetry comparison.
- No live install, service restart, build or device tests performed by the assistant.
