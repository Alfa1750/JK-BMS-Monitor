#!/usr/bin/env python3
"""Minimal read-only JK monitor publisher. Not validated on Venus OS yet."""
import os,sys,logging
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
sys.path.insert(0,"/opt/victronenergy/dbus-systemcalc-py/ext/velib_python")
from vedbus import VeDbusService
from serial_reader import read_once
logging.basicConfig(level=logging.INFO)
log=logging.getLogger("JKMonitor")
PORT=os.environ.get("JKMONITOR_PORT","/dev/ttyUSB0")
BAUD=int(os.environ.get("JKMONITOR_BAUD","115200"))
INSTANCE=int(os.environ.get("JKMONITOR_INSTANCE","290"))
POLL=int(os.environ.get("JKMONITOR_POLL_SECONDS","2"))
DBusGMainLoop(set_as_default=True)
svc=VeDbusService("com.victronenergy.battery.jkmonitor")
paths={"/DeviceInstance":INSTANCE,"/ProductName":"JK-BMS Monitor (read-only)","/ProductId":0,"/CustomName":"JK-BMS Monitor","/Connected":0,"/Mgmt/Connection":"Serial","/Mgmt/ProcessName":"JK-BMS-Monitor","/Mgmt/ProcessVersion":"0.1.0","/Dc/0/Voltage":None,"/Dc/0/Current":None,"/Dc/0/Power":None,"/Soc":None,"/Capacity":None,"/InstalledCapacity":None,"/System/MinCellVoltage":None,"/System/MaxCellVoltage":None,"/System/CellCount":None,"/System/CellVoltageSpread":None,"/System/CellVoltages":None,"/Dc/0/Temperature":None,"/System/Temperatures":None,"/ChargeCycles":None,"/FirmwareVersion":None,"/Error":0}
for p,v in paths.items(): svc.add_path(p,v,writeable=False)
def poll():
    try:
        t=read_once(PORT,BAUD)
        svc["/Connected"]=1;svc["/Error"]=0
        svc["/Dc/0/Voltage"]=t.voltage;svc["/Dc/0/Current"]=t.current
        svc["/Dc/0/Power"]=round(t.voltage*t.current,2);svc["/Soc"]=t.soc
        svc["/Capacity"]=t.capacity;svc["/InstalledCapacity"]=t.capacity
        svc["/System/CellCount"]=len(t.cells);svc["/System/MinCellVoltage"]=min(t.cells)
        svc["/System/MaxCellVoltage"]=max(t.cells);svc["/System/CellVoltageSpread"]=max(t.cells)-min(t.cells)
        svc["/System/CellVoltages"]=t.cells;svc["/System/Temperatures"]=t.temperatures
        svc["/Dc/0/Temperature"]=max(t.temperatures) if t.temperatures else None
        svc["/ChargeCycles"]=t.cycles;svc["/FirmwareVersion"]=t.version or ""
        log.info("Telemetry refreshed: %.2f V, %.2f A, SOC=%s",t.voltage,t.current,t.soc)
    except Exception as e:
        svc["/Connected"]=0;svc["/Error"]=1;log.warning("Read failed: %s",e)
    return True
poll();GLib.timeout_add_seconds(max(1,POLL),poll);GLib.MainLoop().run()
