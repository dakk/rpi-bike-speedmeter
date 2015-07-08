#!/usr/bin/python2
import wiringpi
import time

# Sleep time
ST = 0.05

# Wheel radius (mm)
WR = 260.0

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

while True:
	while cs < 1/ST:
		time.sleep (ST)
		v = wiringpi.digitalRead(17)
		cs += 1
		rounds += int (v)

	rpm = (rpm + (rounds * 60)) / 2
	kmm = rpm * CFK
	kmh = rpm * CFK * 60
	print 'RPS:',rounds,'RPM:',rpm,'km/m:',kmm,'km/h:',kmh

	rounds = 0
	cs = 0
