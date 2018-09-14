#!/usr/bin/python
import init.py
import sensors.py
import display.py
import datetime
import time

#global variables:
resetPin = 23
frequencySwitch = 24
stopSwitch = 22
displaySwitch = 27

#ADC PINS
SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8

def main():
	global resetPin, SPICLK, SPIMISO, SPIMOSI, SPICS

	#run initialisation
	init.initADC(SPICLK, SPIMISO, SPIMOSI, SPICS)
	init.initPins(tempSensorPin,potPin,ldrPin,resetPin)

	timer = 0
	state = False #if state is false program is not running
    	while(True):
		#check if reset button is pushed to start program
		#bla bla bla bla
		#timer

		while(state):#will run until reset button is bushed
			#if reset button pressed: state = False and break

			## TODO: write function to choose between 500ms, 1s, 2s$
			#if 500 ms chosen then let delay = 500ms etc etc
			#sysTime = datetime.datetime.now().time() 
			#gets the cur$
			#display.display(sysTime, timer, sensors.getPot(potPin)$
			#timer += delay
			#time.sleep(delay)

			data = sensors.getSensors(0, 0.5)
			print data
