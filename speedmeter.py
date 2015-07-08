#!/usr/bin/python2
import wiringpi
import time

wiringpi.wiringPiSetupGpio()

wiringpi.pinMode(17, 1)
cs = 0
ST = 0.01
ones = 0

while True:
	while cs < 1/ST:
		time.sleep (ST)
		v = wiringpi.digitalRead(17)
		cs += 1
		if int (v) == 1:
			ones += 1
	print 'Contact in one second:',ones
	ones = 0
	cs = 0
