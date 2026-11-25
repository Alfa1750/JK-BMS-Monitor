# Project Status — JK-BMS-Monitor

**Status:** Initial setup / design phase  
**Implementation:** Not started  
**Testing:** Not performed  
**Deployment:** Not authorized or performed

## Goal
Create a separate, read-only JK-BMS monitoring service for Venus OS. It must not influence charger or battery control.

## Confirmed repository baseline
- Repository: Alfa1750/JK-BMS-Monitor
- Default branch: main
- Initial README existed; project scope was expanded in the initial setup.
- No code implementation is present or verified at this stage.

## Decisions and constraints
- This is a separate project, not part of VantourerDisplayBridge.
- Monitoring only: no BMS control commands and no control-oriented D-Bus properties or flags.
- Source methods from dbus-serialbattery may be studied; reuse requires license/attribution review and careful isolation.
- The target connection method is initially serial.
- DVCC being disabled is not considered proof of control independence.
- No builds, installs, service starts, flashes, or live Pi changes without explicit user approval.

## Roadmap
1. Research upstream communication/parser methods and licensing.
2. Review Venus OS D-Bus battery conventions and relevant systemcalc/MPPT consumer behavior.
3. Define and review the minimal monitor-only D-Bus contract.
4. Implement a minimal reader/parser/service.
5. Static audit: prohibit control properties and BMS writes.
6. Controlled tests on a test system.
7. Document evidence for charger/MPPT independence.
8. Prepare installation instructions only after safety validation.

## Open questions
- Which exact D-Bus properties are required for monitoring, and which consumer code reacts to them?
- What is the minimum safe service/property set?
- Which upstream methods can be reused under the applicable license?
- How can monitor stop/removal be tested without causing unintended charger behavior?

## Activity
- 2026-11-25: Repository confirmed accessible via GitHub connection with read/write permissions. Initial project constraints and architecture documentation being established.
