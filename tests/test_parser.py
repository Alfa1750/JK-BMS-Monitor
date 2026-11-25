import os,sys,unittest
sys.path.insert(0,os.path.join(os.path.dirname(__file__),"..","monitor"))
from jk_parser import validate_frame,parse_payload
class ParserTests(unittest.TestCase):
    def test_empty_frame_rejected(self):
        with self.assertRaises(ValueError): validate_frame(b"")
    def test_bad_header_rejected(self):
        with self.assertRaises(ValueError): validate_frame(b"\x00\x00"+b"\x00"*20)
    def test_empty_payload_rejected(self):
        with self.assertRaises(ValueError): parse_payload(b"")
if __name__=="__main__": unittest.main()
