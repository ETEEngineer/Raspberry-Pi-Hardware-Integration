from gpiozero import Servo
from time import sleep


#GPIO
servo = Servo(18)



print("Starting Low-Power Servo Test")



try:
    while True:
        #Gradually move Min to Max
        print("Sweeping Forward")
        for i in range(-100, 101, 5):
            servo.value = i /100.0
            sleep(0.05) #Small delay to reduce current Spike
        print("Sweeping Backward........")
        for i in range(100, -101, -5):
            servo.value = i / 100.0
            

            
            sleep(0.05)
except KeyboardInterrupt:
    servo.detach()
    print("\nServo Detached and Safe")
            
        
            
