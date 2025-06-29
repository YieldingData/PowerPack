# PowerPack

**PowerPack** is a universal low-power battery management system designed for use with single board computers (SBCs) such as the Raspberry Pi or Orange Pi. It provides intelligent power sequencing, battery monitoring, and communication via I2C. The system is modular and supports multiple microcontrollers, with current implementations for the Xiao ESP32-S3 and ATmega328P.

---

## Features

- **Custom Power Sequences**  
  Long press for power on/off with LED indicators for startup and shutdown.
  
- **Voltage Monitoring**  
  Periodic battery voltage checks and percentage reporting via I2C.

- **Low Power Consumption**  
  Microcontroller enters deep sleep mode when idle to conserve energy.

- **Universal Compatibility**  
  Modular firmware libraries support multiple MCU platforms.

- **I2C Communication**  
  Simple integration with SBCs using minimal GPIOs.

- **Integrated Battery Charging**  
  Designed to work with TP4056 or similar modules for safe lithium-ion battery charging.

---

## Quick Start

1. Connect the microcontroller and SBC using the provided circuit diagram.
2. Flash the appropriate firmware to your microcontroller:
   - [`ESP32-S3 firmware`](firmware/ESP32S3_code.ino)
   - [`ATmega328P firmware`](firmware/ATmega328P_code.ino)
3. Install required Python libraries on your SBC if needed.
4. Run the I2C communication script:
   ```bash
   python3 firmware/powerpack_monitor.py
