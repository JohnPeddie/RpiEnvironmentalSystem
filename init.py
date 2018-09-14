#!/usr/bin/python
import RPi.GPIO as GPIO
import Adafruit_MCP3008 #required library for adc, see prac sheet for how to install adafruit
import time

def initPins(resetPin):
	#initialise all the pins
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(resetPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) #eg of a pin being initialised
	print("Pin initialised")
