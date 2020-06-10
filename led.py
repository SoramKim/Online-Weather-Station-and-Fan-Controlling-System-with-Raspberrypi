# led.py
import os
import time
import RPi.GPIO as GPIO


red= 11
green= 13

GPIO.setmode(GPIO.BOARD)

GPIO.setup(red, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(green, GPIO.OUT, initial=GPIO.LOW)

GPIO.output(red,GPIO.HIGH)
GPIO.output(green,GPIO.HIGH)
print(" on")
time.sleep(5)

GPIO.output(red, GPIO.LOW)
GPIO.output(green, GPIO.LOW)
print("off")
time.sleep(5)




