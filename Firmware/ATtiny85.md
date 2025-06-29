# PowerPack Firmware for ATtiny85

This firmware enables low-power battery management using the **ATtiny85** microcontroller. It provides button-controlled power sequencing, battery monitoring, and I2C communication with an external host device. Ideal for embedded and space-constrained projects, this implementation emphasizes energy efficiency and minimal external components.

---

## Features

- **Button Input with Debounce**  
  Detects short, long, and very long presses to control power state and initiate charging behavior.

- **Power State Control**  
  Uses a MOSFET to switch power to connected devices, with visual status from green/red LEDs.

- **Battery Monitoring**  
  Reads battery voltage and temperature periodically. Sends updates via I2C and serial debug.

- **Charging Indication**  
  Green LED fades in/out to visually show charging mode.

- **Sleep Mode for Power Saving**  
  Automatically enters deep sleep when idle. Wakes via external interrupt on button press.

- **I2C Communication**  
  Sends shutdown/sleep commands and battery info to an external SBC or controller.

- **PWM LED Effects**  
  Uses Timer0 to control LED brightness during charging.

---

## Pinout

| Signal              | Description                         | ATtiny85 Pin |
|---------------------|--------------------------------------|--------------|
| `buttonPin`         | Button input (w/ debounce + INT)     | PB3 (Pin 2)  |
| `mosfetPin`         | Controls external power (MOSFET)     | PB4 (Pin 3)  |
| `greenLEDPin`       | Green LED for status/charging        | PB0 (Pin 5)  |
| `redLEDPin`         | Red LED for shutdown indication      | PB1 (Pin 6)  |
| `batteryPin`        | Analog voltage read from battery     | PB2 (A1, Pin 7) |
| `tempPin`           | Temperature sensor analog read       | PB5 (A0, Pin 1) |

---

## Button Functions

| Press Duration      | Action                                |
|---------------------|----------------------------------------|
| Short Press         | Sends sleep signal via I2C             |
| Long Press (5–10 s) | Toggles power state                    |
| Very Long Press (>10 s) | Initiates charging indication     |

---

## Firmware Breakdown

### `setup()`
- Configures I/O pins and PWM
- Starts serial and I2C communication
- Sets up Timer0 for LED PWM
- Attaches interrupt on button pin

### `loop()`
- Handles button press logic
- Measures battery voltage and temperature
- Sends data via I2C
- Enters sleep mode to conserve power

### Helper Functions

- `handleButtonPress()` – Determines press type and takes action  
- `togglePowerState()` – Enables/disables output power via MOSFET  
- `measureBatteryVoltage()` – Reads and processes battery voltage  
- `measureBatteryTemperature()` – Reads analog temperature input  
- `indicateCharging()` – Pulses green LED during charging mode  
- `enterSleepMode()` – Puts ATtiny85 into power-down sleep  
- `wakeUp()` – Interrupt to wake MCU from sleep  

### I2C Handlers

- `requestEvent()` – Placeholder for responding to I2C read requests  
- `receiveEvent(int howMany)` – Placeholder for receiving commands via I2C  

---

## Notes

- Battery charging is handled by an external module like a TP4056.  
- This firmware provides **visual charging indication** only; it does not control charging logic.  
- Designed for extreme energy efficiency: runtime is minimal, and sleep mode is default behavior.

---

## License

This firmware is licensed under the MIT License. See the [LICENSE](LICENSE) file for full terms.
