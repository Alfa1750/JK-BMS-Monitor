import serial
from jk_parser import STATUS_REQUEST, validate_frame, parse_payload

def read_once(port, baud=115200, timeout=1.5):
    with serial.Serial(port,baudrate=baud,timeout=timeout,write_timeout=timeout) as s:
        s.reset_input_buffer()
        s.write(STATUS_REQUEST); s.flush()
        h=s.read(4)
        if len(h)!=4 or h[:2]!=b"\x4e\x57": raise TimeoutError("JK response header timeout")
        n=int.from_bytes(h[2:4],"big")
        if n<11 or n>2048: raise ValueError("Invalid frame size")
        body=s.read(n)
        if len(body)!=n: raise TimeoutError("Incomplete frame")
        return parse_payload(validate_frame(h+body)
