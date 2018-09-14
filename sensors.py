##!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os
import sys
import Adafruit_MCP3008 #required library for adc, see prac sheet for how to install adafruit

#ADC PINS
SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8

values = [0]*8

def getData(channel, delay):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(SPIMOSI, GPIO.OUT)
        GPIO.setup(SPIMISO, GPIO.IN)
        GPIO.setup(SPICLK, GPIO.OUT)
        GPIO.setup(SPICS, GPIO.OUT)
        mcp = Adafruit_MCP3008.MCP3008(clk=SPICLK, cs=SPICS, mosi=SPIMOSI, miso=SPIMISO)

	try:
		while True:
			values[0] = mcp.read_adc(0)
			time.sleep(delay)
			print values
	except KeyboardInterrupt:
			spi.close()

	return values
