# temp.py
import os
import time
import RPi.GPIO as GPIO
import Adafruit_DHT as dht

sensor = dht.DHT11
temp_pin = 7
red= 11
green= 13
GPIO.setmode(GPIO.BOARD)

def printTemp():
    h, t = dht.read_retry(sensor, temp_pin)
    if h is not None and t is not None:
        print("Temperature = {0:0.1f}*C Humidity = {1:0.1f}%".format(t, h))
    else:
        print('Read error')

try:
    GPIO.setup(red,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(green, GPIO.OUT, initial=GPIO.LOW)

    while True:
        printTemp()
        GPIO.output(red,GPIO.HIGH)
        GPIO.output(green,GPIO.HIGH)
        print("on")
        time.sleep(5)
        GPIO.output(red, GPIO.LOW)
        GPIO.output(green, GPIO.HIGH)
        print("off")
        time.sleep(5)


except KeyboardInterrupt:
    print("Terminated by keyboard")
    GPIO.cleanup()
finally:
    print("End of Program")



