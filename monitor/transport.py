"""Transport selector: BLE or UART serial."""
import os,asyncio
from serial_reader import read_once
from jk_ble_reader import read_ble

def read_telemetry():
    mode=os.getenv("JKMONITOR_MODE","ble").lower()
    if mode=="serial":
        t=read_once(os.getenv("JKMONITOR_PORT","/dev/ttyUSB0"),int(os.getenv("JKMONITOR_BAUD","115200")))
        return {"voltage":t.voltage,"current":t.current,"soc":t.soc,"cells":t.cells,
          "temperatures":t.temperatures,"remaining_capacity":None,"capacity":t.capacity,
          "cycles":t.cycles,"version":t.version}
    if mode=="ble":
        addr=os.getenv("JKMONITOR_BLE_ADDRESS","").strip()
        if not addr: raise ValueError("Set JKMONITOR_BLE_ADDRESS in configuration for BLE mode")
        return asyncio.run(read_ble(addr))
    raise ValueError("JKMONITOR_MODE must be ble or serial")
