
#https://www.raspberry-buy.de/I2C_OLED-Display_Raspberry_Pi_Python_SH1106_SSD1306.html
#https://luma-oled.readthedocs.io/en/develop/python-usage.html

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106, ssd1306
from PIL import ImageFont, ImageDraw, Image
import time

serial = i2c(port=1, address=0x3C)
device = sh1106(serial)


oled_font = ImageFont.truetype('FreeSans.ttf', 14)
with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline = "white", fill = "black")
    draw.text((10, 10), "OLED-Display", font = oled_font, fill = "white")

while True:
    time.sleep(3)