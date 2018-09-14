##!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os
import sys
import init

values = [0]*8

def getData(channel, delay):
	try:
		while True:
			values[0] = init.mcp.read_adc(0)
			time.sleep(delay)
	except KeyboardInterrupt:
			spi.close()

	return values
