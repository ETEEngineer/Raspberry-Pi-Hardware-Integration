import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

# --- 1. Hardware Initialization ---
i2c = busio.I2C(board.SCL, board.SDA)
oled_width = 128
oled_height = 64
oled = adafruit_ssd1306.SSD1306_I2C(oled_width, oled_height, i2c, addr=0x3c)

# Clear display
oled.fill(0)
oled.show()

# --- 2. Graphics Buffer Initialization (Pillow) ---
# Create a blank 1-bit color image (matching the OLED)
image = Image.new("1", (oled.width, oled.height))

# Create a drawing object to render onto the image
draw = ImageDraw.Draw(image)

# Load the default system font (Bypasses the missing .bin file error)
font = ImageFont.load_default()

# --- 3. Render Text to the Buffer ---
# Syntax: draw.text((X, Y), "Text", font=font, fill=255)
draw.text((0, 0), "DISPLAY ACTIVE", font=font, fill=255)
draw.text((0, 16), "I2C Bus: NOMINAL", font=font, fill=255)
draw.text((0, 32), "Graphics: PIL", font=font, fill=255)

# --- 4. Push Buffer to Hardware ---
oled.image(image)
oled.show()

print("Hardware Override Successful. Check OLED.")