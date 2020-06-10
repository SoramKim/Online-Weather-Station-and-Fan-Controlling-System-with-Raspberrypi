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

font = ImageFont.load_default() 
draw.text((1,1),'Temperature : 27.8', font=font, fill=255) 

disp.image(image) 
disp.display()

