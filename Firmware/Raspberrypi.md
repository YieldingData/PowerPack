# Raspberry Pi I2C Data Logger

This project demonstrates how to use a Raspberry Pi to read data from an Arduino via I2C, log the data, and include a unique serial number for each battery. The data includes battery percentage, temperature, and various command signals.

## Overview

The program reads data from an Arduino microcontroller over I2C, logs the received information to a file, and includes the battery's unique serial number in each log entry. This setup is useful for monitoring battery status and maintaining a record of its performance over time.

## Hardware Requirements

- Raspberry Pi (any model with I2C support)
- Arduino (e.g., ATmega328P)
- Battery monitoring circuit
- I2C connections between Raspberry Pi and Arduino

## Software Requirements

- Python 3
- `smbus` library (Install with `sudo apt-get install python3-smbus`)

## Setup Instructions

1. **Arduino Code**: Upload the provided Arduino sketch to your Arduino board. This sketch includes the unique serial number generated based on the compile date and time.

2. **Raspberry Pi Connections**: Connect the Raspberry Pi to the Arduino via I2C. Ensure you enable I2C on your Raspberry Pi by running `sudo raspi-config` and selecting the appropriate options.

3. **Log File Path**: Specify the path where the log file will be saved in the Python script (`logfile = "/path/to/your/logfile.txt"`).

4. **Run the Python Script**: Execute the Python script on your Raspberry Pi to start logging data.

## Python Script

The Python script performs the following functions:
- Requests the battery's unique serial number from the Arduino.
- Reads I2C data from the Arduino, including battery percentage, temperature, and command signals.
- Logs the data with a timestamp and serial number to a specified file.

### Script: `data_logger.py`

```python
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
        # Request serial number first
        bus.write_byte(I2C_ADDR, 0)  # Trigger a request event
        time.sleep(0.1)
        serial_data = bus.read_i2c_block_data(I2C_ADDR, 0, 16)  # Adjust size as needed for your serial number
        serial_number = ''.join(chr(byte) for byte in serial_data).strip()

        # Read actual data
        data = bus.read_i2c_block_data(I2C_ADDR, 0, 2)
        command = chr(data[0])
        value = data[1]
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if command == 'B':
            battery_percentage = value
            log_message = f"{timestamp} - Serial: {serial_number} - Battery Percentage: {battery_percentage}%"
            print(log_message)
            log_data(log_message)
        elif command == 'S':
            log_message = f"{timestamp} - Serial: {serial_number} - Shutdown command received"
            print(log_message)
            log_data(log_message)
            # Execute shutdown command
        elif command == 'L':
            log_message = f"{timestamp} - Serial: {serial_number} - Sleep command received"
            print(log_message)
            log_data(log_message)
            # Execute sleep command
        elif command == 'T':
            temperature = value
            log_message = f"{timestamp} - Serial: {serial_number} - Battery Temperature: {temperature}°C"
            print(log_message)
            log_data(log_message)
        elif command == 'C':
            log_message = f"{timestamp} - Serial: {serial_number} - Charging"
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
