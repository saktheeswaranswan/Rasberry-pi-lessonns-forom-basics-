#pip install luma.oled
#pip install pillow
#pip install gpiozero

from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from PIL import Image, ImageDraw, ImageFont
import time

# Initialize the OLED display
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, width=128, height=32)

# Load a font
font = ImageFont.load_default()

try:
    while True:
        # Create a blank image with mode '1' for 1-bit color
        image = Image.new('1', (128, 32))
        
        # Create a drawing object
        draw = ImageDraw.Draw(image)
        
        # Clear the image
        draw.rectangle((0, 0, 128, 32), outline=0, fill=0)
        
        # Draw the message on the image
        draw.text((0, 0), "Hello, World!", font=font, fill=255)
        
        # Display the image on the OLED
        device.display(image)
        
        # Wait for a few seconds before changing the message
        time.sleep(2)
        
except KeyboardInterrupt:
    pass

# Clean up
device.clear()

