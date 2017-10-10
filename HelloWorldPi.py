import RPi.GPIO as GPIO
import time

pin = 21
interations = 10
interval = .25

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)

for x in range(1, interations+1):
    
    #print "Loop %d: LED on" % (x)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(interval)
    
    #print "Loop %d: LED off" % (x)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(interval)