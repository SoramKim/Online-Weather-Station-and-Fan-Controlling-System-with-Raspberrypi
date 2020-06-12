# weatherStation_perSecond.py
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
maxTmp=30
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
            print("Temperature is high")
            GPIO.output(red, GPIO.HIGH)
        else :
            GPIO.output(red, GPIO.LOW)

        if h>maxHum :
            GPIO.output(green, GPIO.HIGH)
            print("Humidity is high")
        else :
            GPIO.output(green,GPIO.LOW)

    else:
        GPIO.output(fan_pin, False)
        GPIO.output(red, GPIO.LOW)
        GPIO.output(red, GPIO.LOW)

def displayOLED(h,t):
    disp = Adafruit_SSD1306.SSD1306_128_64(rst=6, dc=12, spi=SPI.SpiDev(0, 0, max_speed_hz=8000000))
    disp.begin()
    disp.clear()
    disp.display()
    image = Image.new('1', (disp.width, disp.height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    #font1= ImageFont.truetype('Minecraftia.ttf',15)
    draw.text((2, 1),"Soram's Lab", font=font, fill=255)
    draw.text((5, 20),"Temp:", font=font, fill=255)
    draw.text((50, 20),str(t), font=font, fill=255)
    draw.text((100, 20),"*C", font=font, fill=255)
    draw.text((5, 40),"Humi:", font=font, fill=255)
    draw.text((50, 40),str(h), font=font, fill=255)
    draw.text((100, 40),"%", font=font, fill=255)
    disp.image(image)
    disp.display()


setup()
f = open("tempLog_everySecond", "w")

hum, temp = getTemp()
displayOLED(hum, temp)
controlFan(hum, temp)

f.write(str(temp) + " " + str(hum) + "\n")
f.close
GPIO.cleanup()
