# Raspberry Pi I2C Data Logger

This project demonstrates how to use a **Raspberry Pi** to communicate with an **Arduino-based power management controller** (e.g. PowerPack) over I2C. It periodically logs battery data, temperature, and command signals (e.g. shutdown or sleep), along with a **unique serial number** for each battery.

---

## 📦 Overview

The system:
- Requests the serial number of the connected battery device.
- Reads battery status and commands via I2C.
- Logs all data with timestamps to a specified log file.
- Optionally triggers shutdown or sleep actions on the Raspberry Pi.

---

## 🔧 Hardware Requirements

- Raspberry Pi (any model with I2C support)
- Arduino (e.g., ATmega328P or ATtiny85 with I2C firmware)
- PowerPack battery monitoring system
- I2C connection (SDA, SCL, GND) between Raspberry Pi and Arduino

---

## 💾 Software Requirements

- Python 3
- `smbus` library:
  ```bash
  sudo apt-get install python3-smbus
  ```
  Enable I²C support with `sudo raspi-config`.

  Run the example script:
  ```bash
  python3 RaspberryPi_script.py
  ```
