import smbus
import time

I2C_ADDR = 8
bus = smbus.SMBus(1)  # Use I2C bus 1

def read_i2c():
    try:
        data = bus.read_i2c_block_data(I2C_ADDR, 0, 2)
        command = chr(data[0])
        value = data[1]
        
        if command == 'B':
            battery_percentage = value
            print(f"Battery Percentage: {battery_percentage}%")
        elif command == 'S':
            print("Shutdown command received")
            # Execute shutdown command
        elif command == 'L':
            print("Sleep command received")
            # Execute sleep command
    except IOError:
        print("I2C communication error")

try:
    while True:
        read_i2c()
        time.sleep(600)  # Check for new data every 10 minutes
except KeyboardInterrupt:
    pass
