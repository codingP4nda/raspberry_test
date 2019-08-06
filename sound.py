#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import logging
import datetime

logging.basicConfig(level=logging.INFO)

#GPIO SETUP
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
        if GPIO.input(channel):
                print("Sound Detected!")
                logging.info(datetime.datetime.now().time())
                print(GPIO.input(channel))
        else:
                print("Sound Detected!")
                logging.info(datetime.datetime.now().time())

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
        time.sleep(1)