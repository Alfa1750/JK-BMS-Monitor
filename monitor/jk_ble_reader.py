"""JK BLE telemetry reader, read-only subset of JK protocol.

Protocol framing/field layout adapted with attribution to venus-os_dbus-serialbattery
(AGPL-3.0); write/control register routines are intentionally not included.
"""
import asyncio
import struct
import time

CHAR_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"
CHAR_HANDLE_FALLBACK = 4
FRAME_START = b"\x55\xaa\xeb\x90"
FRAME_SIZE = 300

def signed_temp(raw):
    # JK temperature fields use tenths of a degree and encode negative
    # values in the upper half of the unsigned range.
    value=raw/10.0
    return value if raw < 32767 else (65535-raw)/10.0*-1

class JKFrameDecoder:
    def __init__(self):
        self.buffer = bytearray()
        self.last = None
        self.cell_count = 0
    def feed(self, chunk):
        if chunk[:4] == FRAME_START:
            self.buffer.clear()
        self.buffer.extend(chunk)
        if len(self.buffer) > 600:
            self.buffer.clear()
            return
        if len(self.buffer) >= FRAME_SIZE:
            frame = bytes(self.buffer[:FRAME_SIZE])
            self.buffer.clear()
            if sum(frame[:299]) & 0xff == frame[299]:
                self.decode(frame)
    def decode(self, frame):
        kind=frame[4]
        if kind == 1:
            self.cell_count=struct.unpack_from("<I",frame,114)[0]
            if not 1 <= self.cell_count <= 32: self.cell_count=0
        elif kind == 2:
            if not self.cell_count:
                self.cell_count=sum(1 for i in range(32) if struct.unpack_from("<H",frame,6+2*i)[0])
            count=min(max(self.cell_count,1),32)
            cells=[struct.unpack_from("<H",frame,6+2*i)[0]/1000 for i in range(count)]
            if not cells or any(v<1 or v>5 for v in cells): return
            voltage=struct.unpack_from("<H",frame,118)[0]/1000
            current=struct.unpack_from("<i",frame,126)[0]/1000
            t1=signed_temp(struct.unpack_from("<H",frame,130)[0])
            t2=signed_temp(struct.unpack_from("<H",frame,132)[0])
            tm=signed_temp(struct.unpack_from("<H",frame,134)[0])
            soc=frame[141]
            if soc>100: soc=None
            remaining=struct.unpack_from("<I",frame,142)[0]/1000
            capacity=struct.unpack_from("<I",frame,146)[0]/1000
            cycles=struct.unpack_from("<I",frame,150)[0]
            self.last={"voltage":voltage,"current":current,"soc":soc,"cells":cells,
                "temperatures":[x for x in (tm,t1,t2) if -100<x<200],
                "remaining_capacity":remaining,"capacity":capacity,"cycles":cycles,
                "version":"","timestamp":time.monotonic()}
async def read_ble(address, timeout=15):
    """Connect, request telemetry read blocks, return latest telemetry.

    Only 0x96/0x97 read requests are issued; no configuration/control registers.
    """
    from bleak import BleakClient
    dec=JKFrameDecoder()
    def notify(sender,data):
        dec.feed(bytes(data))
    async with BleakClient(address,timeout=10) as client:
        try: await client.start_notify(CHAR_UUID,notify)
        except Exception: await client.start_notify(CHAR_HANDLE_FALLBACK,notify)
        # Read requests: settings (0x96) and device information (0x97).
        for command in (0x96,0x97):
            request=bytearray(20);request[:4]=b"\xaa\x55\x90\xeb";request[4]=command
            request[5]=0;request[19]=sum(request[:19])&0xff
            try: await client.write_gatt_char(CHAR_UUID,request,response=False)
            except Exception: await client.write_gatt_char(CHAR_HANDLE_FALLBACK,request,response=False)
            await asyncio.sleep(1)
        end=time.monotonic()+timeout
        while time.monotonic()<end and dec.last is None:
            await asyncio.sleep(.25)
        if dec.last is None: raise TimeoutError("No valid JK BLE telemetry frame received")
        return dec.last
