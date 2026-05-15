import time
import board
import adafruit_dht

# Initialize the DHT11 device on GPIO 4
# Using board.D4 maps directly to physical pin 7
dhtDevice = adafruit_dht.DHT11(board.D4)

print("Telemetry Active. Initializing Sensor...")
print("Note: Occasional read failures are expected due to Linux timing.\n")

try:
    while True:
        try:
            # Attempt to pull telemetry data
            temperature_c = dhtDevice.temperature
            humidity = dhtDevice.humidity
            
            # Print the validated data
            print(f"TEMP: {temperature_c}°C | HUMIDITY: {humidity}%")

        except RuntimeError as error:
            # This catches the pulse-width timing failures
            # Professional systems log the error and continue, they do not crash.
            print(f"Read Fault: {error.args[0]} - Retrying...")
            time.sleep(2.0)
            continue
            
        except Exception as error:
            # Fatal errors force a safe shutdown of the sensor object
            dhtDevice.exit()
            raise error

        # The DHT11 requires at least 2 seconds between reads
        time.sleep(2.0)

except KeyboardInterrupt:
    print("\nCommand received. Terminating telemetry.")
finally:
    # Always cleanly release hardware resources
    dhtDevice.exit()
    print("Hardware released. System offline.")
