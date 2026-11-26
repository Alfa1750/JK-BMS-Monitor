# JK-BMS-Monitor

Read-only JK-BMS telemetry monitor for Venus OS. **v0.1.4 PackageManager test candidate** supports BLE and UART transport selection.

## Configure
Edit `/data/JK-BMS-Monitor/config/jk-bms-monitor`:
- `JKMONITOR_MODE=ble` (default) or `serial`
- BLE: set `JKMONITOR_BLE_ADDRESS` to the JK BMS MAC address
- UART: set `JKMONITOR_PORT` and `JKMONITOR_BAUD`

The monitor publishes telemetry only and does not expose Victron control-limit paths. BLE uses protocol read requests only; no BMS configuration/control register implementation is included.

## PackageManager installation
Install/update through Venus OS PackageManager with SetupHelper. SetupHelper installs the package's `services/jk-bms-monitor` service into the persistent and active service locations and manages service startup, updates and removal. No custom `/data/rc.local` hook or service-overlay copying is used.

The service launcher checks for the pinned BLE dependencies and installs them app-locally under `/data/JK-BMS-Monitor/vendor` when missing. This may take some time on its first start and requires network access. System Python packages are not intentionally modified. User configuration is stored outside the package payload in `/data/JK-BMS-Monitor/config` and is preserved across package updates; a prior v0.1.3 config is migrated if present.

Logs are captured under `/data/log/jk-bms-monitor`. Configure the BMS MAC in the config file after installation.

## Important test boundary
v0.1.4 is prepared for isolated-device testing, not validated on-device. SetupHelper PackageManager recognition, installation/update/uninstall, service startup, dependency bootstrap, BLE protocol compatibility, Bluetooth permissions, reconnect behavior, D-Bus paths and systemcalc/charger independence still require user-controlled validation on an isolated test GX.
