# ✨ PowerPack Features

This document outlines the current and future feature set of the **PowerPack** system.  
Confirmed features are already implemented or tested. Dreamed features are planned, under development, or proposed for future versions.

---

## ✅ Confirmed Features

### 🔋 Power Control
- Long press to power on/off with LED indicators
- Safe shutdown support via I²C command from the SBC
- Optional hardware hold pin for emergency SBC shutdown detection
- Digital control of output power via MOSFET or boost converter enable pin (`SWITCH_EN`)

### 📡 Communication
- I²C protocol for simple 2-wire communication with the host SBC
- Compatible with Raspberry Pi, Orange Pi, and similar Linux-based boards
- Python script (`powerpack_monitor.py`) for querying voltage, temperature, and state

### 📈 Battery & Thermal Monitoring
- Voltage divider reads battery voltage internally
- Battery percentage estimated from voltage curve
- **External thermistor input** for direct battery cell temperature monitoring
- **Onboard thermistor** for ambient PCB temperature and reference accuracy

### 🌙 Low Power Operation
- Microcontroller enters deep sleep when idle
- Wake on power button or optional external signal
- Optimized for long-term battery-powered deployments

### 🧩 Modular Firmware Architecture
- Core firmware developed for **ATTiny1616**
- Previous support for ATmega328P and Xiao ESP32-S3 (legacy)
- Shared I²C command protocol allows easy porting to other MCUs (STM32, RP2040, etc.)

### 🔌 Integrated Charging Support
- Designed for use with **TP4056** Li-ion charging module (4.2 V / 1S)
- Charge/full status passthrough via LED or logic-level GPIO
- PowerPack can operate independently while charging

### ⚡ Regulated Power Output
- Step-up boost converter (e.g. **MT3608**) provides regulated 5 V output from single-cell Li-ion
- Power to SBC is gated by the microcontroller (`SWITCH_EN`) for safe boot/shutdown control
- Optional enable pin control or power path MOSFET depending on board layout

---

## 🌱 Dreamed Features

### 🔋 Advanced Power Logic
- Auto power-on when charger is connected
- Auto shutdown at configurable low-voltage threshold
- Heartbeat pin from SBC to detect freeze/crash and trigger safe shutdown
- Button debounce and multiple press patterns (reset, bootloader, etc.)

### 📊 Data Logging & Diagnostics
- Log battery voltage, shutdown events, and uptime
- Log file tagging per-device (by serial number or ID EEPROM)
- Optional real-time clock for time-based logs (via RTC chip)

### ⚡ Output Enhancements
- USB-A or USB-C power output
- QC3.0 or USB-PD 5V/9V/12V negotiation
- Over-current and over-temperature protection
- Add support for LiFePO₄ batteries or 2S configurations
- **Solder-selectable input voltage range**  
  Add a jumper or solder pad to configure boost/buck behavior based on expected input voltage:  
  - 3–5 V (e.g. single-cell Li-ion)  
  - 5–24 V (e.g. 2S–5S packs, solar panels)  
  - 24–60 V (industrial applications, DC rails)  
  Allows PowerPack to auto-scale or switch converter and protection thresholds accordingly.

### 🔋 Smart Battery Features
- Fuel gauge integration (e.g., MAX17048, INA219)
- Real-time charge/discharge current monitoring
- Capacity estimation over time

### ☀️ Renewable Energy Support
- Solar panel input with MPPT-lite logic
- Supercapacitor compatibility
- Overvoltage/undervoltage protection for harsh environments

### 🌐 Advanced Interfaces
- ~~Wireless control via ESP32 Bluetooth or Wi-Fi~~ ❌  *(Not included)*  
  To conserve power, PowerPack does not include any always-on wireless interfaces. All communication is handled through I²C by the connected device (e.g. SBC).
  
- ~~Wireless control via ESP32 Bluetooth or Wi-Fi~~ ❌ *(Not planned)*  
  PowerPack avoids always-on radios to preserve battery life. All monitoring is done via I²C, allowing the connected device (e.g. Raspberry Pi) to handle higher-level logic and interfaces.

- ~~Web UI for battery and power stats~~ ❌ *(Not needed)*  
  UI and stats are delegated to the SBC side via I²C integration.

---

## 🧠 Want to Suggest a Feature?

Feel free to open an issue or discussion thread on [GitHub](https://github.com/YieldingData/PowerPack) to propose or vote on features.

We prioritize:
- Low-power and portable use cases
- Safe shutdown for SBCs
- Smart off-grid deployments

---

## 📦 Version Tracking

- `v1.0` — Base implementation (power control, I²C, voltage and thermal monitoring, charging, 5V boost control)
- `v1.1+` — Dreamed features to be added incrementally in future versions


# ✨ PowerPack Features

This document outlines the current and future feature set of the **PowerPack** system.  
Confirmed features are already implemented or tested. Dreamed features are planned, under development, or proposed for future versions.

---

## ✅ Confirmed Features

### 🔋 Power Control
- Long press to power on/off with LED indicators
- Safe shutdown support via I²C command from the SBC
- Optional hardware hold pin for emergency SBC shutdown detection

### 📡 Communication
- I²C protocol for simple 2-wire communication with the host SBC
- Compatible with Raspberry Pi, Orange Pi, and similar Linux-based boards
- Python script (`powerpack_monitor.py`) for querying voltage, temperature, and state

### 📈 Battery & Thermal Monitoring
- Voltage divider reads battery voltage internally
- Battery percentage estimated from voltage curve
- **External thermistor input** for direct battery cell temperature monitoring
- **Onboard thermistor** for ambient PCB temperature and reference accuracy

### 🌙 Low Power Operation
- Microcontroller enters deep sleep when idle
- Wake on power button or optional external signal
- Optimized for long-term battery-powered deployments

### 🧩 Modular Firmware Architecture
- Core firmware developed for **ATTiny1616**
- Previous support for ATmega328P and Xiao ESP32-S3 (legacy)
- Shared I²C command protocol allows easy porting to other MCUs (STM32, RP2040, etc.)

### 🔌 Integrated Charging Support
- Designed for use with **TP4056** or similar 1S Li-ion charging modules
- Charge/full status passthrough via GPIO for visual or logic-level indicators

---

## 🌱 Dreamed Features

### 🔋 Advanced Power Logic
- Auto power-on when charger is connected
- Auto shutdown at configurable low-voltage threshold
- Heartbeat pin from SBC to detect freeze/crash and trigger safe shutdown
- Button debounce and multiple press patterns (reset, bootloader, etc.)

### 📊 Data Logging & Diagnostics
- Log battery voltage, shutdown events, and uptime
- Log file tagging per-device (by serial number or ID EEPROM)
- Optional real-time clock for time-based logs (via RTC chip)

### ⚡ Output Enhancements
- USB-A or USB-C power output
- QC3.0 or USB-PD 5V/9V/12V negotiation
- Over-current and over-temperature protection
- Add support for LiFePO₄ batteries or 2S configurations
- **Solder-selectable input voltage range**  
  Add a jumper or solder pad to configure buck converter behavior based on expected input voltage:  
  - 3–5 V (e.g. single-cell Li-ion)  
  - 5–24 V (e.g. 2S–5S packs, solar panels)  
  - 24–60 V (industrial applications, DC rails)  
  Allows PowerPack to auto-scale or switch buck regulator settings and protection thresholds accordingly.

### 🔋 Smart Battery Features
- Fuel gauge integration (e.g., MAX17048, INA219)
- Real-time charge/discharge current monitoring
- Capacity estimation over time

### ☀️ Renewable Energy Support
- Solar panel input with MPPT-lite logic
- Supercapacitor compatibility
- Overvoltage/undervoltage protection for harsh environments

### 🌐 Advanced Interfaces
- ~~Wireless control via ESP32 Bluetooth or Wi-Fi~~ ❌  *(Not included)*  
  To conserve power, PowerPack does not include any always-on wireless interfaces. All communication is handled through I²C by the connected device (e.g. SBC).
  
- ~~Wireless control via ESP32 Bluetooth or Wi-Fi~~ ❌ *(Not planned)*  
  PowerPack avoids always-on radios to preserve battery life. All monitoring is done via I²C, allowing the connected device (e.g. Raspberry Pi) to handle higher-level logic and interfaces.

- ~~Web UI for battery and power stats~~ ❌ *(Not needed)*  
  UI and stats are delegated to the SBC side via I²C integration.

---

## 🧠 Want to Suggest a Feature?

Feel free to open an issue or discussion thread on [GitHub](https://github.com/YieldingData/PowerPack) to propose or vote on features.

We prioritize:
- Low-power and portable use cases
- Safe shutdown for SBCs
- Smart off-grid deployments

---

## 📦 Version Tracking

- `v1.0` — Base implementation (power control, I²C, voltage monitoring)
- `v1.1+` — Dreamed features to be added incrementally in future versions

