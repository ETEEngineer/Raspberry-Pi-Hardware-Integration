from gpiozero import LED
from time import sleep

# Use the GPIO number (17), not the physical pin number
led = LED(17)

print("Starting integration test... Press Ctrl+C to stop.")

try:
    while True:
        led.on()
        print("LED is ON")
        sleep(1)
        led.off()
        print("LED is OFF")
        sleep(1)
except KeyboardInterrupt:
    print("\nCleaning up and exiting.")
