#!/usr/bin/python2
import wiringpi
import time

# Sleep time
ST = 0.01

# Wheel size
WS = 26.0



wiringpi.wiringPiSetupGpio()

wiringpi.pinMode(17, 1)
cs = 0
rounds = 0

while True:
	while cs < 1/ST:
		time.sleep (ST)
		v = wiringpi.digitalRead(17)
		cs += 1
		rounds += int (v)

	rpm = (rpm + (rounds * 60)) / 2

	print 'Round per second:',rounds
	print 'Round per minute:',rpm

	rounds = 0
	cs = 0
