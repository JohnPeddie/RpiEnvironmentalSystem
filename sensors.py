#!/usr/bin/python
import RPi.GPIO as GPIO
import spidev #required library for adc, see prac sheet for how to install spidev

# Open SPI bus
spi = spidev.SpiDev() # create spi object
spi.open(0,0)
# RPI has one bus (#0) and two devices (#0 & #1)

def getTempreture(tempSensorChannel):
    #code to get getTempreture from sensor
    #get info from pin: tempSensorPin
    #turn it into usable data
    adc = spi.xfer2([1,(8+tempSensorChannel)<<4,0]) # sending 3 bytes
    data = ((adc[1]&3) << 8) + adc[2]
    return data


def getPot(potPin):
    return pot

def getLDR(ldrPin): #bla bla just examples of fetching data from sensors
    return ldr

def readADC(adcNum):  #Each adc has a number with will be set up in initADC()
    return value
