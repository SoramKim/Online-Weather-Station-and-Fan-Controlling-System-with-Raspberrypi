# temp.py
import os
import time
import RPi.GPIO as GPIO
import Adafruit_DHT as dht

sensor = dht.DHT11
temp_pin = 7
fan_pin = 40
red= 17
green= 27

def setupFan():
    GPIO.setup(fan_pin, GPIO.OUT)
    GPIO.setwarnings(False)


def printTemp():
    h, t = dht.read_retry(sensor, temp_pin)
    if h is not None and t is not None:
        print("Temperature = {0:0.1f}*C Humidity = {1:0.1f}%".format(t, h))
    else:
        print('Read error')

    # if t > 26:
    #     GPIO.output(fan_pin, True)
    # else:
    #     GPIO.output(fan_pin, False)


#
# def checkTemperature():
#     if t> maxTmp:
#         GPIO.output(fan_pin, True)
#     else:
#         GPIO.output(fan_pin, False)


try:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(red,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(green, GPIO.OUT, initial=GPIO.LOW)
    setupFan()

    while True:
        printTemp()
        GPIO.output(fan_pin,GPIO.HIGH)
        GPIO.output(red,GPIO.HIGH)
        GPIO.output(green, GPIO.HIGH)
        print("fan on")
        time.sleep(5)
        
        GPIO.output(fan_pin,GPIO.LOW)
        GPIO.output(red, GPIO.LOW)
        GPIO.output(green, GPIO.HIGH)
        print("fan off")
        time.sleep(5)


except KeyboardInterrupt:
    print("Terminated by keyboard")
    GPIO.cleanup()
finally:
    print("End of Program")



