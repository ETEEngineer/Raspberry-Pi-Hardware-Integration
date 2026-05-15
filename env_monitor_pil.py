import time
import board
import busio
import adafruit_ssd1306
import adafruit_dht
from PIL import Image, ImageDraw, ImageFont

# --- 1. Hardware Initialization ---
# I2C Bus for OLED
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c)

# GPIO 4 for DHT11
dhtDevice = adafruit_dht.DHT11(board.D4)

# --- 2. Graphics Setup ---
font = ImageFont.load_default()

def update_display(line1, line2, line3):
    """Renders text in RAM using Pillow, then blasts it to the OLED."""
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)
    
    draw.text((0, 0), line1, font=font, fill=255)
    draw.text((0, 16), line2, font=font, fill=255)
    draw.text((0, 32), line3, font=font, fill=255)
    
    oled.image(image)
    oled.show()

print("Unified Telemetry System Active. Press Ctrl+C to stop.")

# --- 3. Main Execution Loop ---
try:
    while True:
        try:
            # Poll the sensor
            temp_c = dhtDevice.temperature
            humidity = dhtDevice.humidity
            
            # Format the output strings
            t_str = f"TEMP: {temp_c} C"
            h_str = f"HUM:  {humidity} %"
            
            # Push to the OLED
            update_display("ENVIRONMENT DATA", t_str, h_str)
            
            # Log to terminal
            print(f"[{time.strftime('%H:%M:%S')}] {t_str} | {h_str}")

        except RuntimeError as error:
            # Handle Linux timing faults without crashing the system
            update_display("SENSOR FAULT", "OS Timing Error", "Retrying...")
            print(f"Read Fault: {error.args[0]}")
            time.sleep(2.0)
            continue
            
        except Exception as error:
            # Fatal error
            dhtDevice.exit()
            raise error

        # The DHT11 requires a 2-second delay between reads
        time.sleep(2.0)

except KeyboardInterrupt:
    print("\nTermination command received.")
finally:
    # Clean hardware release
    update_display("SYSTEM OFFLINE", "Hardware Released", "")
    dhtDevice.exit()