# temp.py
import os
import time
import RPi.GPIO as GPIO
import Adafruit_DHT as dht
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

sensor = dht.DHT11
temp_pin = 4
fan_pin = 21
red= 17
green= 27
maxTmp=26
maxHum=80

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(red, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(green, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(fan_pin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setwarnings(False)
    print("setup finished")

def getTemp():
    h, t = dht.read_retry(sensor, temp_pin)
    if h is not None and t is not None:
        print("Temperature = {0:0.1f}*C Humidity = {1:0.1f}%".format(t, h))
    else:
        print('Read error')
    return h,t

def controlFan(h,t):
    if (t > maxTmp) | (h > maxHum) :
        GPIO.output(fan_pin, True)
        if t>maxTmp :
            GPIO.output(red, GPIO.HIGH)
            print("Temperature is high")
        if h>maxHum :
            GPIO.output(green, GPIO.HIGH)
            print("Humidity is high")
    else:
        GPIO.output(fan_pin, False)

def displayOLED(h,t):
    disp = Adafruit_SSD1306.SSD1306_128_64(rst=6, dc=12, spi=SPI.SpiDev(0, 0, max_speed_hz=8000000))

    disp.begin()
    disp.clear()
    disp.display()
    image = Image.new('1', (disp.width, disp.height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    font1= ImageFont.truetype('Minecraftia.ttf',10)

    draw.text((1, 1), "Temperature, Humidity", font=font, fill=255)
    draw.text(5, 10), str(t)+"*C", font=font1, fill=255)
    draw.text((5, 20), str(h)+"%", font=font1, fill=255)
    disp.image(image)
    disp.display()


try:
    setup()
    while True:
        hum,temp=getTemp()
        displayOLED(hum,temp)
        controlFan(hum,temp)
        time.sleep(5)

except KeyboardInterrupt:
    print("Terminated by keyboard")

finally:
    print("End of Program")
    GPIO.cleanup()


