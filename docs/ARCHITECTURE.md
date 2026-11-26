# Architecture — v0.2.0

JK transport/parser → telemetry normalization → read-only generic sensor publisher.

## D-Bus
Service: `com.victronenergy.sensor.jkmonitor`. It is not published in the `com.victronenergy.battery` namespace. Battery control limits, control flags and DVCC capabilities are excluded. Intended separation from systemcalc BMS classification must be validated on Venus OS.

## Lifecycle
Existing SetupHelper lifecycle and service templates retained; persistent configuration is outside package payload.

## Failure behavior
Communication/parser failures update connection/error state and clear telemetry instead of retaining stale data.
