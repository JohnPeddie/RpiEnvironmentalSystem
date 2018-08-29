#!/usr/bin/python
import RPi.GPIO as GPIO

def initADC():
    # TODO: set up adc number initialisation that can be set in main.py
    #initialise ADC

def initPins(tempSensorPin,potPin,ldrPin,resetPin):
    #initialise all the pins
    GPIO.setup(resetPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) #eg of a pin being initialised
    print("Pin initialised")


def someOtherInit():
    #blablabla
