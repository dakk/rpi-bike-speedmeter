#!/usr/bin/python2
import wiringpi
import time

wiringpi.wiringPiSetupGpio()

wiringpi.pinMode(17, 1)


while True:
	time.sleep (0.1)
	wiringpi.digitalRead(17)

