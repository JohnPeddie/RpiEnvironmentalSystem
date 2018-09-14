#!/usr/bin/python
import init
import sensors
import display
import datetime
import time
import RPi.GPIO as GPIO

#global variables:
resetSwitch = 23
frequencySwitch = 24
stopSwitch = 27
displaySwitch = 22

#ADC PINS
SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8

#global variables
delay = 0.5

def main():
	global resetSwitch, frequencySwitch, stopSwitch, displaySwitch, SPICLK, SPIMISO, SPIMOSI, SPICS

	#run initialisation
	init.initPins(resetSwitch, frequencySwitch, stopSwitch, displaySwitch)
	GPIO.add_event_detect(frequencySwitch, GPIO.FALLING, callback=frequencyChange, bouncetime=200)

	timer = 0
	state = True #if state is false program is not running
    	while(True):



		while(state):#will run until reset button is bushed

			data = sensors.getData()
			time.sleep(delay)
			print data

def frequencyChange (channel):
	global delay

	if (delay == 0.5):
		delay = 1
	elif (delay == 1):
		delay = 2
	elif (delay == 2):
		delay = 0.5



if __name__ == '__main__':
	main()
