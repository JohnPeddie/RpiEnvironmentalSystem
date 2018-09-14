#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os
import sys

values = [0]*8

def getData(channel, delay)
	try:
		while True:
			for i in range(8):
				values[i] = mcp.read_adc(i)
			time.sleep(delay)
	except KeyboardInterrupt:
			spi.close()

	return values
