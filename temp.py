#temp.py
import datetime
import Adafruit_DHT as dht

h,t=dht.read_retry(dht,DHT11,4) #  pin 4

print(h) # print humidity
print(t) # print temp





