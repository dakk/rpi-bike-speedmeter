#!/usr/bin/python2
import wiringpi
import time
from threading import Thread
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import urlparse

# HTTP Port
PORT = 6061

# Sleep time
ST = 0.01

# Wheel radius (mm)
WR = 180.0

# Circonference 2 * pi * r (m) and (km)
CF = (2 * 3.14 * WR) / 1000.0
CFK = CF / 1000.0



wiringpi.wiringPiSetupGpio()

wiringpi.pinMode(17, 1)
cs = 0
rounds = 0
rpm = 0
kmm = 0
kmh = 0

pstate = 0


# HTTP JOB
class GetHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.end_headers()
		self.wfile.write(str (kmh))
		return

def serveJob ():
	server = HTTPServer(('', PORT), GetHandler)
	print 'Starting server, use <Ctrl-C> to stop'
	server.serve_forever()

t = Thread(target=serveJob, args=())
t.start()

kmh_avg = 0

while True:
	while cs < 1/ST:
		time.sleep (ST)
		v = wiringpi.digitalRead(17)
		cs += 1

		if pstate == 1 and int(v) == 0:
			rounds += 1
		pstate = int (v)

	rpm = (rpm + (rounds * 60.0)) / 2.0
	kmm = rpm * CF
	kmh = rpm * CF * 60
	kmh_avg = (kmh_avg + kmh) / 2.0
	print 'RPS:',rounds,'RPM:',rpm,'km/m:',kmm,'km/h:',kmh

	rounds = 0
	cs = 0

	f = open ('v.txt', 'w')
	f.write (str (kmh_avg))
	f.close ()
