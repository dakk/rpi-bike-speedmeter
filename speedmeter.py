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
CF = (3.14 * WR) / 1000.0




wiringpi.wiringPiSetupGpio()

wiringpi.pinMode(17, 1)
cs = 0
rounds = 0
rpm = 0
kmm = 0
kmh = 0
kmm_avg = 0

pstate = 0


# HTTP JOB
class GetHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.end_headers()
		self.wfile.write(str (kmm_avg))
		return

def serveJob ():
	server = HTTPServer(('', PORT), GetHandler)
	print 'Starting server, use <Ctrl-C> to stop'
	server.serve_forever()

t = Thread(target=serveJob, args=())
t.start()


while True:
	while cs < 3/ST:
		time.sleep (ST)
		v = wiringpi.digitalRead(17)
		cs += 1

		if pstate == 1 and int(v) == 0:
			rounds += 1
		pstate = int (v)

	rpm = (rpm + (rounds / 3.0 * 60.0)) / 2.0
	kmm = rpm * CF
	kmh = rpm * CF * 60
	kmm_avg = (kmm_avg + kmm * 0.3) / 1.3
	print 'RPS:',rounds,'RPM:',rpm,'km/m:',kmm,'km/h:',kmh,'km/h avg',kmm_avg

	rounds = 0
	cs = 0

	f = open ('v.txt', 'w')
	f.write (str (kmm_avg))
	f.close ()
