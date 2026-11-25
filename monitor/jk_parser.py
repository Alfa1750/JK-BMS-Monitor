"""Read-only JK serial telemetry parser; reduced adaptation based on protocol research."""
from dataclasses import dataclass
from typing import Optional
STATUS_REQUEST=bytes.fromhex("4e5700130000000006030000000000006800000129")
@dataclass
class Telemetry:
    voltage:float; current:float; soc:Optional[int]; cells:list; temperatures:list
    capacity:Optional[int]=None; cycles:Optional[int]=None; version:Optional[str]=None
def tag(data,marker,start,size):
    pos=data.find(bytes([marker]),start)
    if pos<0 or pos+1+size>len(data): raise ValueError("Missing/short JK tag")
    return data[pos+1:pos+1+size]
def parse_payload(data):
    cellbytes=tag(data,0x79,1,1)[0]
    if cellbytes<3 or cellbytes>96 or cellbytes%3: raise ValueError("Invalid cell-data length")
    raw=tag(data,0x79,1,cellbytes+1)
    cells=[int.from_bytes(raw[i+1:i+3],"big")/1000 for i in range(0,cellbytes,3)]
    if not cells or any(v<=0 or v>5 for v in cells): raise ValueError("Invalid cell voltages")
    temps=[]
    for marker,offset in ((0x80,cellbytes+3),(0x81,cellbytes+6),(0x82,cellbytes+9)):
        try:
            v=int.from_bytes(tag(data,marker,offset,2),"big");temps.append(v if v<99 else 100-v)
        except ValueError: pass
    voltage=int.from_bytes(tag(data,0x83,cellbytes+12,2),"big")/100
    x=int.from_bytes(tag(data,0x84,cellbytes+15,2),"big");current=x/-100 if x<32768 else (x-32768)/100
    try: soc=tag(data,0x85,cellbytes+18,1)[0];soc=soc if soc<=100 else None
    except ValueError: soc=None
    try: cycles=int.from_bytes(tag(data,0x87,cellbytes+22,2),"big")
    except ValueError: cycles=None
    try: capacity=int.from_bytes(tag(data,0xaa,cellbytes+121,4),"big")
    except ValueError: capacity=None
    try: version=tag(data,0xb7,cellbytes+174,15).decode("ascii","replace").replace("_"," ").strip("\x00 ")
    except ValueError: version=None
    return Telemetry(voltage,current,soc,cells,temps,capacity,cycles,version)
def validate_frame(frame):
    if len(frame)<15 or frame[:2]!=b"\x4e\x57" or frame[-5]!=0x68: raise ValueError("Malformed frame")
    length=int.from_bytes(frame[2:4],"big")
    if length!=len(frame)-4: raise ValueError("Frame length mismatch")
    if (sum(frame[:-4])&0xffff)!=int.from_bytes(frame[-2:],"big"): raise ValueError("Checksum mismatch")
    return frame[10:len(frame)-7]
