import smbus2
import time
import paho.mqtt.client as mqtt

# 1. Initialize Hardware (MPU6050 only)
bus = smbus2.SMBus(1)
bus.write_byte_data(0x68, 0x6B, 0) # Wake up

# 2. Initialize Network (MQTT)
client = mqtt.Client()
client.connect("127.0.0.1", 1883, 60)
client.loop_start() # CRITICAL: Starts the background network thread

print("Transmission Protocol Active...")

try:
    while True:
        # Read raw X-axis data
        high = bus.read_byte_data(0x68, 0x3B)
        low = bus.read_byte_data(0x68, 0x3C)
        val = (high << 8) | low
        if val > 32768: 
            val -= 65536
        
        ax = val / 16384.0 # Scale to 'g'
        payload = f"X-Axis: {ax:+.2f}g"
        
        # Publish to the exact topic we tested in Phase 2
        client.publish("test/data", payload)
        print(f"Sent: {payload}")
        
        time.sleep(1) # 1-second delay for stability

except KeyboardInterrupt:
    client.loop_stop()
    print("\nTransmission Terminated.")