#temp.py
import time
import Adafruit_DHT as dht

sensor=dht.DHT11
pin=4


try:
    while True:
        h,t=dht.read_retry(sensor,pin) #  pin 4
        if h is not None and t is not None :
            print("Temperature = {0:0.1f}*C Humidity = {1:0.1f}%".format(t, h))
        else:
            print('Read error')
        time.sleep(100)
        
except KeyboardInterrupt:
    print("Terminated by keyboard")
    
finally:
    print("End of Program")



