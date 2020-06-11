import Adafruit_GPIO.SPI as SPI 
import Adafruit_SSD1306 

from PIL import Image 
from PIL import ImageDraw 
from PIL import ImageFont 

disp = Adafruit_SSD1306.SSD1306_128_64(rst=6, dc=12, spi=SPI.SpiDev(0,0,max_speed_hz=8000000))

disp.begin() 
disp.clear()
disp.display() 

image = Image.new('1',(disp.width, disp.height)) 

draw = ImageDraw.Draw(image) 
h=70.3
t=23.4
font = ImageFont.load_default()
font1 = ImageFont.truetype('Minecraftia.ttf',13)


draw.text((1,1),"Temperature:"+str(t), font=font1, fill=255)
draw.text((1,20),"Temperature:"+str(h), font=font1, fill=255)

disp.image(image) 
disp.display()

