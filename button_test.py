from gpiozero import Button
from time import sleep

# Use GPIO 2 (Physical Pin 3)
button = Button(2)

print("Monitoring Button... Press it now!")

while True:
    if button.is_pressed:
        print("Button status: PRESSED (Ground connection active)")
    else:
        print("Button status: Open (Internal Pull-up active)")
    sleep(0.5)
