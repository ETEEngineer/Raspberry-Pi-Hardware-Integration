from gpiozero import DistanceSensor, LED
from time import sleep

# Integration: Echo=18, Trigger=4, LED=17
sensor = DistanceSensor(echo=18, trigger=4)
led = LED(17)

print("Autonomous Obstacle Detection System: ACTIVE")

try:
    while True:
        distance_cm = sensor.distance * 100
        
        if distance_cm < 10:
            print(f"DANGER! Object at {distance_cm:.1f}cm")
            led.on()
        else:
            print(f"Path Clear: {distance_cm:.1f}cm")
            led.off()
            
        sleep(0.1) 

except KeyboardInterrupt:
    led.off()
    print("\nSystem Disarmed.")
