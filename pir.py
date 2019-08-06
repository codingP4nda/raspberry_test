import RPi.GPIO as GPIO
import time
import logging
import datetime

SENSOR_PIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)


def my_callback(channel):
    # Here, alternatively, an application / command etc. can be started.
    print('There was a movement!')
    logging.info(datetime.datetime.now().time())


try:
    GPIO.add_event_detect(SENSOR_PIN, GPIO.RISING, callback=my_callback)
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    print("Finish...")
GPIO.cleanup()
