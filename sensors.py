#!/usr/bin/python
import RPi.GPIO as GPIO
import spidev
import time
import os
import sys
spi = spidev.SpiDev()

def getData(channel):
	adc = spi.xfer2([1,(8+channel)<<4,0]) # sending 3 bytes
	data = ((adc[1]&3) << 8) + adc[2]
	return data

def ConvertVolts(data, places):
	volts = (data*3.3)/float(1023)
	volts = round(volts, places)
	return volts


def getSensors(channel, delay):
	global spi
	spi.open(0,0)

	try:
		while True:
			sensor_data = getData(channel)
			sensor_volt = ConvertVolts(sensor_data, 2)
			time.sleep(delay)
			print sensor_volt
	except KeyboardInterrupt:
			spi.close()

	return sensor_volt
