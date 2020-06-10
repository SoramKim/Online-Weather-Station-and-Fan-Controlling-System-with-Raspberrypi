#!/usr/bin/env python
import os
import threading
import urllib2
from gpiozero import CPUTemperature



def readSensor():

	global temperature
	global humidity
	global pressure
	global cpu_temp

	cpu= CPUTemperature()
	cpu_temp =cpu.temperature

	temperature =cpu_temp
	humidity = 10
	pressure = 0


def sendDataToServer():
	global temperature
	global pressure
	global humidity

	threading.Timer(60,sendDataToServer).start()
	print("Sensing...")
	readSensor()
	print(temperature)
	print(humidity)
	print(pressure)
        temp= "%.1f" %temperature
	hum ="%.1f" %humidity
	press = "%.1f" %pressure
	urllib2.urlopen("http:192.168.137.236/weather/add_data.php?temp="+temp+"&hum="+hum+"&pr="+press).read()

sendDataToServer()
