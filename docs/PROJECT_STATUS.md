# Project Status — JK-BMS-Monitor

Version: v0.1.0 test candidate  
Initial code and package scripts committed  
Tests: not run  
Package creation: not run  
Installation: not performed  
Live system changes: none

## v0.1 contents
- Reduced JK serial telemetry parser and bounded reader.
- Preliminary D-Bus monitor service.
- Manual configuration, installer, uninstaller and archive helper.
- Research and test documentation.
- Control-limit paths and BMS marker paths intentionally omitted.

## Validation gate
Not validated for deployment. D-Bus registration, systemcalc selection, charger/MPPT independence, serial protocol parsing, startup and removal must be tested on an isolated Venus OS device.

## Next
Review v0.1 on a test device. Confirm published paths, service-manager integration and behavior before any camper deployment.
