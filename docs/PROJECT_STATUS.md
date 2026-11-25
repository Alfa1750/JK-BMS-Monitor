# Project Status — JK-BMS-Monitor

Version: v0.1.0 test candidate  
Files: initial implementation package  
Tests: not run  
Installation: not performed  
Live-system changes: none

## v0.1
- Minimal JK serial parser/reader.
- Preliminary D-Bus monitor service.
- Preliminary install/config/uninstall scripts.
- Research and test documentation.
- Control-limit properties and BMS marker paths deliberately omitted.

## Validation gate
Not validated safe for deployment. D-Bus service behavior, systemcalc selection, charger/MPPT independence, startup and removal must be tested on an isolated Venus OS device.

## Next
Controlled test, inspect D-Bus paths, review package/service-manager compatibility and verify charger behavior.
