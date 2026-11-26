#!/usr/bin/env python3
"""Read-only telemetry D-Bus publisher for JK-BMS via BLE or UART."""
import os,sys,logging
import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
sys.path.insert(0,"/opt/victronenergy/dbus-systemcalc-py/ext/velib_python")
from vedbus import VeDbusService
from transport import read_telemetry
logging.basicConfig(level=logging.INFO);log=logging.getLogger("JKMonitor")
INSTANCE=int(os.getenv("JKMONITOR_INSTANCE","290"));POLL=int(os.getenv("JKMONITOR_POLL_SECONDS","2"))
DBusGMainLoop(set_as_default=True)
bus=dbus.bus.BusConnection(dbus.bus.BusConnection.TYPE_SYSTEM)
svc=VeDbusService("com.victronenergy.battery.jkmonitor",bus,register=False)
paths={"/DeviceInstance":INSTANCE,"/ProductName":"JK-BMS Monitor (read-only)","/ProductId":0,
"/CustomName":"JK-BMS Monitor","/Connected":0,"/Mgmt/Connection":"BLE/UART",
"/Mgmt/ProcessName":"JK-BMS-Monitor","/Mgmt/ProcessVersion":"0.1.5",
"/Dc/0/Voltage":None,"/Dc/0/Current":None,"/Dc/0/Power":None,"/Soc":None,
"/Capacity":None,"/InstalledCapacity":None,"/System/MinCellVoltage":None,
"/System/MaxCellVoltage":None,"/System/CellCount":None,"/System/CellVoltageSpread":None,
"/System/CellVoltages":None,"/Dc/0/Temperature":None,"/System/Temperatures":None,
"/ChargeCycles":None,"/FirmwareVersion":"","/Error":0}
for p,v in paths.items():svc.add_path(p,v,writeable=False)
svc.register()
def poll():
 try:
  t=read_telemetry();cells=t["cells"];temps=t["temperatures"]
  if not cells: raise ValueError("Telemetry contains no cell voltage data")
  svc["/Connected"]=1;svc["/Error"]=0
  svc["/Dc/0/Voltage"]=t["voltage"];svc["/Dc/0/Current"]=t["current"]
  svc["/Dc/0/Power"]=round(t["voltage"]*t["current"],2)
  svc["/Soc"]=t["soc"];svc["/Capacity"]=t["capacity"];svc["/InstalledCapacity"]=t["capacity"]
  svc["/System/CellCount"]=len(cells);svc["/System/MinCellVoltage"]=min(cells)
  svc["/System/MaxCellVoltage"]=max(cells);svc["/System/CellVoltageSpread"]=max(cells)-min(cells)
  svc["/System/CellVoltages"]=cells;svc["/System/Temperatures"]=temps
  svc["/Dc/0/Temperature"]=max(temps) if temps else None
  svc["/ChargeCycles"]=t["cycles"];svc["/FirmwareVersion"]=t["version"] or ""
  log.info("Telemetry %.2fV %.2fA SOC=%s",t["voltage"],t["current"],t["soc"])
 except Exception as e:
  # Clear telemetry on failure so stale values are not presented as current.
  svc["/Connected"]=0;svc["/Error"]=1
  for p in ("/Dc/0/Voltage","/Dc/0/Current","/Dc/0/Power","/Soc","/Capacity",
            "/InstalledCapacity","/System/MinCellVoltage","/System/MaxCellVoltage",
            "/System/CellCount","/System/CellVoltageSpread","/System/CellVoltages",
            "/Dc/0/Temperature","/System/Temperatures","/ChargeCycles"):
   svc[p]=None
  svc["/FirmwareVersion"]=""
  log.warning("Read failed; telemetry cleared: %s",e)
 return True
poll();GLib.timeout_add_seconds(max(1,POLL),poll);GLib.MainLoop().run()
