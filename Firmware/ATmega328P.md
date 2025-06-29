# PowerPack (ATmega328P Version)

**PowerPack** is an Arduino-based power management system for monitoring battery voltage and temperature, managing power states, and communicating with other devices via I2C. It uses the ATmega328P microcontroller and is optimized for low-power operation in embedded systems and SBC applications.

---

## Features

- **Single Button Control**  
  One button handles all power and charging state transitions.

- **LED Feedback**  
  Green and red LEDs indicate power, shutdown, and charging status.

- **Battery Monitoring**  
  Reads voltage and temperature at regular intervals.

- **I2C Communication**  
  Sends battery status and shutdown/sleep signals to external devices.

- **Power Saving**  
  MCU enters low-power sleep mode when idle, waking only on interrupt.

---

## Components & Pin Configuration

| Component           | ATmega328P Pin |
|---------------------|----------------|
| **Button**          | PD2 (INT0)     |
| **MOSFET Control**  | PD3            |
| **Green LED**       | PD4            |
| **Red LED**         | PD5            |
| **Battery Voltage** | A1 (PC1)       |
| **Temperature**     | A0 (PC0)       |

---

## Button Behavior

| Press Duration      | Action                                |
|---------------------|----------------------------------------|
| Short Press         | Send sleep signal over I2C             |
| Long Press (5–10 s) | Toggle power state (on/off)            |
| Very Long Press (>10 s) | Enter charging mode               |

---

## Power States

- **Power On**:  
  Green LED blinks once, MOSFET enables SBC power.

- **Power Off**:  
  Red LED blinks once, MOSFET disables SBC power, MCU sleeps.

---

## Charging Mode

- When in charging state, the green LED performs a soft pulse (fade in/out).
- Charging is visual only — actual battery charging is handled externally (e.g., via TP4056).

---

## Code Overview

### `setup()`

- Initializes pin modes
- Attaches interrupt to PD2 (button)
- Sets up I2C and serial communication
- Configures Timer2 for PWM (green LED pulsing)

### `loop()`

- Monitors button states
- Measures and updates voltage and temperature
- Sends relevant I2C messages
- Enters sleep mode if no activity

### Key Functions

- `handleButtonPress()`: Handles press duration and triggers appropriate state
- `togglePowerState()`: Toggles SBC power and gives LED feedback
- `sendShutdownSignal()` / `sendSleepSignal()`: Transmit I2C commands
- `measureBatteryVoltage()` / `measureBatteryTemperature()`: Analog reads
- `indicateCharging()`: PWM control for LED pulsing
- `enterSleepMode()`: Activates low-power mode
- `wakeUp()`: ISR to resume operation on button press

---

## Notes

- This version assumes the TP4056 or equivalent handles battery charging. PowerPack only provides **visual indication** of charging mode.
- The I2C address and data format are defined in the firmware header and can be adapted for compatibility with your SBC.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Future Improvements

- Add support for monitoring TP4056 CHRG/STDBY pins
- Add EEPROM support for persistent state
- Extend compatibility to Xiao ESP32-S3 (see main `README.md`)
