# temp.py
import os
import time
import RPi.GPIO as GPIO
import Adafruit_DHT as dht

sensor = dht.DHT11
temp_pin =4
red= 17
green= 27
GPIO.setmode(GPIO.BCM)

GPIO.setup(green, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(red,GPIO.OUT,initial=GPIO.LOW)
GPIO.setwarnings(False)

def printTemp():
    h, t = dht.read_retry(sensor,temp_pin)
    if h is not None and t is not None:
        print("Temperature = {0:0.1f}*C Humidity = {1:0.1f}%".format(t, h))
    else:
        print('Read error')

printTemp()
GPIO.output(red,GPIO.HIGH)
GPIO.output(green,GPIO.HIGH)
print("on")
time.sleep(5)

GPIO.output(red, GPIO.LOW)
printTemp()
GPIO.output(green, GPIO.LOW)
print("off")
time.sleep(5)





