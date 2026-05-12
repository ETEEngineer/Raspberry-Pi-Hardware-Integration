import smbus2
import time
#MPU6050 I2C Address
DEVICE_ADDRESS = 0x68

PWR_MGMT_1 = 0x6B
ACCEL_XOUTH_H = 0x3B
ACCEL_YOUTH_H = 0x3D
ACCEL_ZOUTH_H = 0x3F

#Initialize SMBus
bus = smbus2.SMBus(1)
#Wake up the MPU6050
bus.write_byte_data(DEVICE_ADDRESS, PWR_MGMT_1, 0)
def read_raw_bits(register):
    high = bus.read_byte_data(DEVICE_ADDRESS, register)
    low = bus.read_byte_data(DEVICE_ADDRESS, register + 1)
    
    
    value = (high << 8) | low
    
    if value > 32768:
        value -= 65536
    return value
print("Reading Accelerometer Data.... Press Ctrl+C to stop")


try:
    while True:
        raw_x = read_raw_bits(ACCEL_XOUTH_H)
        raw_y = read_raw_bits(ACCEL_YOUTH_H)
        raw_z = read_raw_bits(ACCEL_ZOUTH_H)
        
        
        ax = raw_x / 16384.0
        ay = raw_y / 16384.0
        az = raw_z / 16384.0
        
        
        print(f"X: {ax:+.2f}g | Y: {ay:+.2f}g | Z: {az:+.2f}g")
        
        
        time.sleep(0.2)
        
except KeyboardInterrupt:
    print("\n Sensors Disarmed")
    
        

