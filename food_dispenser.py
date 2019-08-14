#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
import pyttsx

NAME_OF_DOG = 'Ollie'

# credit to Alex Wilkinson
# http://thingswatihavedonewithmyraspberrypi.blogspot.com/2012/10/controlling-bigtrack-motors-with-my.html
# for providing code for RPi.GPIO settings

engine = pyttsx.init()
engine.say('Pouring food, for', NAME_OF_DOG)
engine.runAndWait()

# Declare the GPIO settings
GPIO.setmode(GPIO.BOARD)

# set up GPIO pins
GPIO.setup(7, GPIO.OUT) # PWMA
GPIO.setup(11, GPIO.OUT) # AIN2
GPIO.setup(12, GPIO.OUT) # AIN1
GPIO.setup(13, GPIO.OUT) # STBY

# Drive the motor clockwise
GPIO.output(12, GPIO.HIGH)
GPIO.output(11, GPIO.LOW)

# Set the motor speed
GPIO.output(7, GPIO.HIGH)

# Disable STBY (standby)
GPIO.output(13, GPIO.HIGH)

#turn the dispenser
time.sleep(3)

# Reset all the GPIO pins by setting them to LOW
GPIO.output(12, GPIO.LOW)
GPIO.output(11, GPIO.LOW)
GPIO.output(7, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
