#!/usr/bin/python
import RPi.GPIO as GPIO
import Adafruit_MCP3008 #required library for adc, see prac sheet for how to install adafruit

def initADC(SPICLK, SPIMISO, SPIMOSI, SPICS):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(SPIMOSI, GPIO.OUT)
	GPIO.setup(SPIMISO, GPIO.IN)
	GPIO.setup(SPICLK, GPIO.OUT)
	GPIO.setup(SPICS, GPIO.OUT)
	mcp = Adafruit_MCP3008.MCP3008(clk=SPICLK, cs=SPICS, mosi=SPIMOSI, miso=SPIMISO)
	#Add code to deal with mcp


def initPins(tempSensorPin,potPin,ldrPin,resetPin):
	#initialise all the pins
	GPIO.setup(resetPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) #eg of a pin being initialised
	print("Pin initialised")
