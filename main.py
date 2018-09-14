#!/usr/bin/python
import init
import sensors
import display
import datetime
import time

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

	timer = 0
	state = True #if state is false program is not running
    	while(True):
		
		

		while(state):#will run until reset button is bushed
			#if reset button pressed: state = False and break

			## TODO: write function to choose between 500ms, 1s, 2s$
			#if 500 ms chosen then let delay = 500ms etc etc
			#sysTime = datetime.datetime.now().time() 
			#gets the cur$
			#display.display(sysTime, timer, sensors.getPot(potPin)$
			#timer += delay
			#time.sleep(delay)
			
			GPIO.add_event_detech(frequencySwitch, GPIO.FALLING, callback=frequencyChange, bouncetime=200)


			data = sensors.getData(0, delay)
			print data

def frequencyChange (channel):
	global delay
	
	if (delay = 0.5):
		delay = 1
	elif (delay = 1):
		delay = 2
	elif (delay = 2):
		delay = 0.5


if __name__ == '__main__':
	main()
