import smbus2
import time

from rpi_lcd import LCD

#Addresses
MPU_ADDR = 0x68

#MPU6050 Registers
PWR_MGMT_1 = 0x6B
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
#Initliaze Hardware
bus = smbus2.SMBus(1)

lcd = LCD() #Default address 0x27




#wake up MPU6050
bus.write_byte_data(MPU_ADDR, PWR_MGMT_1, 0)

def read_accel(addr):
    high = bus.read_byte_data(MPU_ADDR, addr)
    low = bus.read_byte_data(MPU_ADDR, addr + 1)
    value = (high << 8)  | low
    if value  > 32768:
        value -= 65536
    return value / 16384.0 #Scale to 'g'

print("System Active: Outputting to LCD......")


try:
    while True:
        ax = read_accel(ACCEL_XOUT_H)
        ay = read_accel(ACCEL_YOUT_H)
        
        #Format strings for the LCD
        
        line1 = f"Accel X: {ax:+.2f}g"
        line2 = f"Accel Y: {ay:+.2f}g"
        
        
        lcd.text(line1, 1)
        lcd.text(line2, 2)
        
        
        time.sleep(0.2)
        
        
except KeyboardInterrupt:
    lcd.clear()
    print("\n System Shutdown.")
        
    