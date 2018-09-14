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

pot_adc = 0
temp_adc = 0
light_adc = 0
values = [0]*3

def getData():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(SPIMOSI, GPIO.OUT)
        GPIO.setup(SPIMISO, GPIO.IN)
        GPIO.setup(SPICLK, GPIO.OUT)
        GPIO.setup(SPICS, GPIO.OUT)
        mcp = Adafruit_MCP3008.MCP3008(clk=SPICLK, cs=SPICS, mosi=SPIMOSI, miso=SPIMISO)

	pot_adc = mcp.read_adc(0)
	temp_adc = mcp.read_adc(1)
	light_adc = mcp.read_adc(2)
	potV = round((pot_adc/1024.0)*3.3, 2)
	temp = round(((((temp_adc*3.3)/1024)-0.5)/0.01),2)
	light = round((light_adc/985.0)*100.0,2)
	values[0] = potV
	values[1] = temp
	values[2] = light

	return values
