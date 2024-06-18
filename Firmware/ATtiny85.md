# PowerPack Firmware for ATtiny85

This firmware for the ATtiny85 microcontroller provides power management and monitoring features. It uses various pins to manage a button, MOSFET, LEDs, and sensors. The key functionalities include:

## Features

1. **Button Handling**:
   - Detects short and long button presses.
   - Toggles power state or initiates charging based on the duration of the press.
   - Implements debounce logic to prevent false triggers.

2. **Power Management**:
   - Manages power state using a MOSFET and visual indicators (LEDs).
   - Sends shutdown or sleep signals via I2C to an external device.

3. **Battery Monitoring**:
   - Measures battery voltage and temperature.
   - Sends battery status and temperature data over I2C and serial communication.
   - Indicates charging state with a fading LED effect.

4. **Energy Efficiency**:
   - Enters sleep mode to conserve power, waking up on button press interrupts.

5. **I2C Communication**:
   - Uses I2C to communicate with external devices for shutdown, sleep, and battery status.

6. **Timer Configuration**:
   - Configures Timer0 for fast PWM to control LED brightness during the charging indication.

## Pinout Table

| Pin        | Description                        | ATtiny85 Pin |
|------------|------------------------------------|--------------|
| buttonPin  | Charge detection circuit           | PB3 (2)      |
| mosfetPin  | MOSFET control                     | PB4 (3)      |
| greenLEDPin| Green LED                          | PB0 (0)      |
| redLEDPin  | Red LED                            | PB1 (1)      |
| batteryPin | Battery voltage measurement        | PB2 (A1)     |
| tempPin    | Temperature monitoring (repurposed)| PB5 (A0)     |

## Code Breakdown

- **Pin Definitions**: Configures pins for the button, MOSFET, LEDs, battery voltage, and temperature sensors.
- **Setup Function**: Initializes pin modes, I2C communication, serial communication, and configures Timer0 for PWM.
- **Main Loop**: 
  - Handles button presses to toggle power state or start charging.
  - Periodically measures battery voltage and temperature.
  - Enters sleep mode to save power.
- **Helper Functions**:
  - `handleButtonPress()`: Processes button press actions.
  - `togglePowerState()`: Toggles the power state and manages LEDs.
  - `measureBatteryVoltage()`: Reads and processes battery voltage.
  - `measureBatteryTemperature()`: Reads and processes battery temperature.
  - `indicateCharging()`: Indicates charging state with a fading LED.
  - `enterSleepMode()`: Puts the microcontroller into sleep mode to save power.
  - `wakeUp()`: Interrupt service routine to wake up the microcontroller on button press.
- **I2C Handlers**:
  - `requestEvent()`: Placeholder for handling I2C requests.
  - `receiveEvent(int howMany)`: Placeholder for handling I2C data reception.

This code is designed for low-power applications, efficiently managing power states and monitoring battery status with periodic measurements and sleep modes.
