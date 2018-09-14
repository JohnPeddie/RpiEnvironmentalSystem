#!/usr/bin/python
import RPi.GPIO as GPIO
import spidev
import time
import os
import sys

def getTemperature(channel):
	adc = spi.xfer2([1,(8+channel)<<4,0]) # sending 3 bytes
    	data = ((adc[1]&3) << 8) + adc[2]
    	return data

def ConvertVolts(data, places)
    	volts = (data*3.3)/float(1023)
    	volts = round(volts, places)
    	return volts


def checkSensor(channel, delay)
    	spi = spidev.SpiDev()
    	spi.open(0,0)
    
    	try:
        	while True:
			sensor_data = GetData(channel)
			sensor_volt = ConvertVolts(sensor_data, 2)
			time.sleep(delay)
		except KeyboardInterrupt:
			spi.close()

	return sensor_volt
