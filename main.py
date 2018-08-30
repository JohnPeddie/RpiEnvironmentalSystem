#!/usr/bin/python

import init.py
import sensors.py
import display.py
import datetime
import time
#global variables:
tempSensorPin = 22 #examples, i dont know if these pins are correct
potPin = 23
ldrPin =24
resetPin = 25

#ADC PINS
SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8
#bla bla more pins
#might be better to make the pins an array/linkedList

def main():
    global tempSensorPin, potPin, ldrPin, resetPin, SPICLK, SPIMISO, SPIMOSI, SPICS
    #run initialisation
    init.initADC(SPICLK, SPIMISO, SPIMOSI, SPICS)
    init.initPins(tempSensorPin,potPin,ldrPin,resetPin)
    #bla bla just example code on how to call functions from another file
    timer = 0
    state = False #if state is false program is not running
    while(True):
        #check if reset button is pushed to start program
        #bla bla bla bla
        #timer

        while(state):#will run until reset button is bushed
        #if reset button pressed: state = False and break

            ## TODO: write function to choose between 500ms, 1s, 2s delay
            #if 500 ms chosen then let delay = 500ms etc etc

            sysTime = datetime.datetime.now().time() #gets the current system time
            display.display(sysTime, timer, sensors.getPot(potPin), sensors.getTempreture(tempSensorPin), sensors.getLDR(ldrPin))
            timer += delay
            time.sleep(delay)



if __name__ == "__main__":
    main()
