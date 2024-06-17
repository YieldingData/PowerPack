### PowerPack

This project provides a universal low-power battery management system for use with single board computers (SBCs) like the Raspberry Pi. The system includes customizable power up and down sequences, voltage monitoring, and communication with the SBC via I2C. The project is designed to be flexible, supporting different microcontroller chips such as the ATmega328P.

---

## Features

- **Custom Power Sequences**: Long press for power on/off with LED indicators for startup and shutdown.
- **Voltage Monitoring**: Periodic battery voltage checks with data sent to the SBC.
- **Low Power Consumption**: Microcontroller enters deep sleep mode when not actively managing power.
- **Universal Compatibility**: Modular design with libraries for different microcontrollers.
- **I2C Communication**: Efficient use of GPIO pins on the SBC.

---

## Hardware Requirements

- **Microcontroller**: ATmega328P or other supported chips
- **Single Board Computer**: Raspberry Pi or similar
- **Push Button**: For power control
- **LEDs**: Green and Red for status indication
- **MOSFET**: To control power to the SBC
- **Voltage Divider**: For battery monitoring
- **Battery**: With connectors

---

## Software Overview

### Microcontroller Firmware

1. **Initialization**:
   - Set up I2C communication.
   - Configure pins for button, MOSFET, and LEDs.
   - Enable interrupt on button pin for waking up from sleep.

2. **Power Management**:
   - Detect long and short button presses.
   - Toggle power states and send signals to the SBC.
   - Enter deep sleep mode to save power.

3. **Voltage Monitoring**:
   - Measure battery voltage periodically.
   - Send battery percentage data to the SBC over I2C.

4. **Libraries**:
   - Include libraries for different microcontrollers to support universal compatibility.

### SBC Script

1. **I2C Communication**:
   - Read data from the microcontroller.
   - Handle commands for power state changes and battery status.

2. **Shutdown Sequence**:
   - Customizable shutdown script executed upon receiving the shutdown signal.



## Repository Structure

```
/project-root
│
├── /hardware
│   ├── circuit_diagram.png
│   └── parts_list.txt
│
├── /firmware
│   ├── ATmega328P_code.ino
│   ├── RaspberryPi_script.py
│   └── /libraries
│       └── /ATmega328P
│           └── atmega328p_lib.ino
│       └── /OtherMicrocontroller
│           └── other_microcontroller_lib.ino
│
├── README.md
└── LICENSE
```

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

This setup provides a robust and customizable battery management system for SBCs, with modular support for various microcontrollers, making it adaptable for different hardware configurations and use cases.
