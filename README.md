## ⚡ PowerPack

**PowerPack** is a universal, low-power battery management system designed for single-board computers (SBCs) like the Raspberry Pi, Orange Pi, or Compute Module. It offers intelligent power sequencing, I²C communication, battery health monitoring, and deep sleep control — all in a modular, firmware-agnostic package.

> Currently implemented for:  
> ✅ Xiao ESP32-S3  
> ✅ ATmega328P

---

## 🚀 Quick Start

1. **Connect hardware**  
   Follow the circuit diagram in `/docs/hardware_schematic.png` (coming soon).

2. **Flash firmware**  
   - [`firmware/esp32s3/`](firmware/esp32s3/) — for Xiao ESP32-S3  
   - [`firmware/atmega328p/`](firmware/atmega328p/) — for ATmega328P

3. **Install software on SBC**  
   Install required Python dependencies and run:
   ```bash
   python3 firmware/powerpack_monitor.py
   ```

---

## ✨ Features

See full [FEATURES.md](features.md) for in-depth detail.

### ✅ Confirmed Features
- **Custom Power Sequences**  
  Long press to power on/off, with LED indicators for startup and shutdown

- **Voltage Monitoring**  
  Battery percentage and raw voltage data over I²C

- **Low Power Consumption**  
  MCU enters deep sleep when idle

- **Modular Firmware Support**  
  Easily portable between MCUs like ESP32-S3, ATmega328P, STM32, etc.

- **I²C Communication**  
  2-wire communication to/from SBC for status and control

- **TP4056 Integration**  
  Safe 1S Li-ion charging via TP4056 or similar charging modules

### 🌱 Dreamed Features
- ⏱️ Auto power-off on inactivity or heartbeat timeout  
- 🪫 Configurable shutdown threshold and low-battery alerts  
- 🌡️ Thermistor-based temperature monitoring  
- 🔌 USB-PD or QC3.0 output stage with 5V/9V/12V support  
- 📈 Power usage logging and trend analysis  
- 🔋 Fuel gauge chip (e.g., MAX17048) integration  
- ☀️ Solar panel input with MPPT-lite logic  
- 📶 Wireless OTA updates for ESP32 versions  
- 🎮 Power control via physical buttons or web UI

---

## 📂 Repository Structure

```
/hardware/        → KiCad schematic & PCB files
/firmware/        → Microcontroller firmware
/software/        → SBC I²C communication scripts
/docs/            → Pinout diagrams, usage docs, feature specs
features.md       → Full confirmed/dreamed feature list
powerpack_v1_spec.md → Electrical & mechanical spec sheet
README.md         → This file
```

---

## 💬 Community & Contributions

We welcome contributions, ideas, and hardware forks!  
Please submit issues or pull requests to help improve PowerPack.

---

## 🛡️ License

Licensed under **CERN-OHL-W v2** (Open Hardware License – Weakly Reciprocal)  
See [LICENSE.md](LICENSE.md) for more information.
