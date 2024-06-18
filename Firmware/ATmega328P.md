# PowerPack

PowerPack is an Arduino-based power management system designed for monitoring and controlling battery charging and power states. It leverages the ATmega328P microcontroller, with a focus on power efficiency and reliable performance.

## Features

- **Button Control**: A single button controls power states and charging operations.
- **LED Indicators**: Green and red LEDs provide visual feedback for power and charging states.
- **Battery Monitoring**: Measures battery voltage and temperature at regular intervals.
- **I2C Communication**: Sends battery status and control signals to other devices.
- **Power Saving**: Enters a low-power sleep mode to conserve battery when not in active use.

## Components

- **ATmega328P Microcontroller**
- **Button**: Connected to PD2 (INT0)
- **MOSFET**: Controlled by PD3
- **Green LED**: Connected to PD4
- **Red LED**: Connected to PD5
- **Battery Voltage Sensor**: Connected to A1 (PC1)
- **Temperature Sensor**: Connected to A0 (PC0)

## Pin Configuration

| Component         | Pin       |
|-------------------|-----------|
| Button            | PD2 (INT0)|
| MOSFET            | PD3       |
| Green LED         | PD4       |
| Red LED           | PD5       |
| Battery Voltage   | A1 (PC1)  |
| Temperature Sensor| A0 (PC0)  |

## Usage

### Button Operations

- **Short Press**: Sends a sleep signal.
- **Long Press (5-10 seconds)**: Toggles the power state.
- **Very Long Press (>10 seconds)**: Initiates charging state.

### Power State

- **On**: Green LED lights up briefly, MOSFET is activated.
- **Off**: Red LED lights up briefly, then the system powers down.

### Charging State

- The green LED fades in and out to indicate the charging process.

## Code Overview

### setup()

- Initializes pin modes and states.
- Attaches interrupt to the button pin.
- Initializes I2C communication and serial debugging.
- Configures Timer2 for fast PWM on the green LED.

### loop()

- Handles button press events.
- Monitors and updates battery voltage and temperature.
- Enters sleep mode to conserve power when idle.

### Interrupts and Functions

- **handleButtonPress()**: Processes button presses and determines action based on press duration.
- **togglePowerState()**: Toggles the power state and handles LED indications.
- **sendShutdownSignal()** and **sendSleepSignal()**: Send control signals via I2C.
- **measureBatteryVoltage()** and **measureBatteryTemperature()**: Measure and report battery status.
- **indicateCharging()**: Provides visual feedback for charging.
- **enterSleepMode()**: Puts the MCU into a low-power sleep mode.
- **wakeUp()**: Interrupt service routine to wake up the MCU.
