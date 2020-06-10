#temp.py
import time
import Adafruit_DHT as dht

sensor=dht.DHT11
pin=4
h,t=dht.read_retry(sensor,pin) #  pin 4

try:
    while True:

print(h) # print humidity
print(t) # print temp





