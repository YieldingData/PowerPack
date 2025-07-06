# ✨ PowerPack Features

This document outlines the current and future feature set of the **PowerPack** system.  
Confirmed features are already implemented or tested. Dreamed features are planned, under development, or proposed for future versions.

---

## ✅ Confirmed Features

### 🔋 Power Control
- Long press to power on/off with LED indicators
- Safe shutdown support via I²C trigger
- Optional hardware hold pin for SBC shutdown detection

### 📡 Communication
- I²C protocol for simple 2-wire communication with SBC
- Python script (`powerpack_monitor.py`) for polling battery stats
- Compatible with Raspberry Pi, Orange Pi, and similar SBCs

### 📈 Battery Monitoring
- Voltage divider reads battery voltage
- Converts voltage to estimated battery percentage
- Optional thermistor for temperature monitoring

### 🌙 Low Power Operation
- Deep sleep mode for microcontroller during inactivity
- Wake on button press or external event
- Optimized for long-term battery-powered deployments

### 🧩 Modular Firmware
- ATmega328P and Xiao ESP32-S3 firmware supported
- Shared I²C command structure across MCUs
- Easy to extend to STM32, RP2040, or others

### 🔌 Integrated Charging Support
- Designed for TP4056 charging module (1S Li-ion)
- Charge status passthrough (charging/full detection via GPIO)

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

