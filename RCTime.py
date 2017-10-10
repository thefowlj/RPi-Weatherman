#!/usr/bin/env python

#read RC timing using Raspberry Pi

import RPi.GPIO as GPIO,time,os
import time
import math

DEBUG = 1
GPIO.setmode(GPIO.BCM)
CAPACITOR=math.pow(10,-)
TEMPOFFSET = 273.15

def RCtime(RCpin):
    reading = 0
    GPIO.setup(RCpin,GPIO.OUT)
    GPIO.output(RCpin,GPIO.LOW)
    time.sleep(0.1)
    
    GPIO.setup(RCpin,GPIO.IN)
    #This takes about 1 millisecond per loop cycle
    a = time.clock()
    while(GPIO.input(RCpin) == GPIO.LOW):
        #Blank'
        z = 1
        reading += 1
    b = time.clock()
    R = (b-a)/CAPACITOR
    T=math.pow((1/298.15 + (1/3380)*math.log(R/10000)),-1)-TEMPOFFSET
    
    return R

while True:
    print(RCtime(18))
    time.sleep(1)