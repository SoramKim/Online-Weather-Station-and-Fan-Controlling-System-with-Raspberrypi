# fan.py

import time
import RPi.GPIO as GPIO


fan_pin = 40
GPIO.setmode(GPIO.BOARD)

GPIO.setup(fan_pin, GPIO.OUT)
GPIO.setwarnings(False)
print("setup clear")

GPIO.output(fan_pin,True)
print("fan on")
time.sleep(5)

GPIO.output(fan_pin,False)
print("fan off")
time.sleep(5)

GPIO.output(fan_pin,True)
print("fan on")
time.sleep(5)

GPIO.output(fan_pin,False)
print("fan off")
time.sleep(5)



