import smbus
import time
from datetime import datetime

I2C_ADDR = 8
bus = smbus.SMBus(1)  # Use I2C bus 1
logfile = "/path/to/your/logfile.txt"  # Specify your log file path

def log_data(data):
    with open(logfile, 'a') as file:
        file.write(data + '\n')

def read_i2c():
    try:
        data = bus.read_i2c_block_data(I2C_ADDR, 0, 2)
        command = chr(data[0])
        value = data[1]
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if command == 'B':
            battery_percentage = value
            log_message = f"{timestamp} - Battery Percentage: {battery_percentage}%"
            print(log_message)
            log_data(log_message)
        elif command == 'S':
            log_message = f"{timestamp} - Shutdown command received"
            print(log_message)
            log_data(log_message)
            # Execute shutdown command
        elif command == 'L':
            log_message = f"{timestamp} - Sleep command received"
            print(log_message)
            log_data(log_message)
            # Execute sleep command
        elif command == 'T':
            temperature = value
            log_message = f"{timestamp} - Battery Temperature: {temperature}°C"
            print(log_message)
            log_data(log_message)
        elif command == 'C':
            log_message = f"{timestamp} - Charging"
            print(log_message)
            log_data(log_message)
    except IOError:
        print("I2C communication error")

try:
    while True:
        read_i2c()
        time.sleep(600)  # Check for new data every 10 minutes
except KeyboardInterrupt:
    pass
