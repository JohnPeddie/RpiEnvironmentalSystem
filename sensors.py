##!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os
import sys
import globals

values = [0]*8

def getData(channel, delay):
	mcp = Adafruit_MCP3008.MCP3008(clk=globals.tempCLK, cs=globals.tempCS, mosi=globals.tempMOSI, miso=globals.tempMISO)
	try:
		while True:
			values[0] = mcp.read_adc(0)
			time.sleep(delay)
	except KeyboardInterrupt:
			spi.close()

	return values
