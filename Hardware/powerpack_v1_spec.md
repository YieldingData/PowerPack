# ⚡ PowerPack v1 Hardware Specification

> Version: 1.0  
> License: CERN-OHL-W v2  
> Status: In Development

---

## 🧠 Project Summary

**PowerPack** is an intelligent, open-source power management module designed for single-board computers like the Raspberry Pi Zero 2 W, Orange Pi, or Compute Module. It provides safe, efficient, and compact power delivery with built-in I²C communication, battery monitoring, and smart shutdown/startup control.

---

## 📐 Mechanical Overview

| Parameter         | Value              |
|------------------|--------------------|
| Board Size       | ≤ 35 mm × 17 mm × 9 mm |
| Mounting         | M2/M2.5 screw holes or double-sided tape |
| Weight (target)  | ≤ 10 grams         |
| Form Factor      | Stackable / inline / side-mountable |

---

## ⚡ Electrical Specifications

### 🔋 Input
| Parameter       | Value                  |
|----------------|------------------------|
| Voltage Range   | 3.7–6 V (1S Li-ion) or 6–24 V for expanded solar input |
| Connector       | JST 2-pin / Screw Terminal |
| Charging Support| TP4056 / external charger |

### 🔌 Output
| Parameter       | Value                  |
|----------------|------------------------|
| Output Voltage  | 5 V ± 5% (default)     |
| Output Current  | 3 A continuous, 4 A peak |
| Output Interface| USB-A / USB-C / Solder Pads |
| Regulation Type | High-efficiency synchronous buck |
| Efficiency      | ≥ 90% @ 5V/2A          |

---

## 🧠 Smart Power Control

### ✅ Features
- Power on/off via I²C or GPIO
- Safe shutdown trigger with configurable delay
- Auto power-off on low battery voltage
- Startup on charger insertion or button press
- "Heartbeat" pin to detect SBC responsiveness
- Optional LED indicators for state

### 📡 I²C Interface
| Command         | Description                       |
|----------------|-----------------------------------|
| `GET_VOLTAGE`   | Returns battery voltage (mV)      |
| `GET_TEMP`      | Returns battery temperature (°C)  |
| `POWER_ON`      | Enables 5V output                 |
| `POWER_OFF`     | Delayed shutdown sequence         |
| `GET_STATUS`    | Returns state, voltage, temp, etc.|

### 🧰 Optional Sensors
- NTC thermistor for thermal monitoring
- INA219 or voltage divider for battery sensing

---

## 🧩 Integration Use Cases

- 🔊 **InkPop** music player (RPi Zero + DAC + E-Paper)
- 🛰 **Mesh in a Shell** field communicator
- 🧱 Portable SBC testing/debugging rig
- ☀️ Off-grid / solar SBC deployments

---

## 🛠 Roadmap

| Milestone              | Status       |
|------------------------|--------------|
| Electrical Schematic   | ✅ Drafted    |
| KiCad PCB Layout       | 🛠 In Progress|
| I²C Firmware (ATmega328P) | 🛠 Planned  |
| Python SDK             | 🧪 Prototyping|
| Case Design (3D STL)   | ⏳ TBD        |

---

## 📂 Repository Structure (planned)

```
/hardware/
  ├─ powerpack_v1.kicad_pro
  ├─ powerpack_v1.sch
  └─ powerpack_v1.kicad_pcb
/firmware/
  └─ atmega328p_i2c_controller/
      ├─ main.c
      └─ i2c_commands.h
/software/
  └─ powerpack.py (Python SDK)
/docs/
  └─ powerpack_v1_spec.md
```

---

## 📜 License

This project is licensed under the **CERN Open Hardware License v2 – Weakly Reciprocal (CERN-OHL-W)**.  
See `LICENSE.md` for details.

---

## 🙌 Credits & Inspiration

Inspired by DROK modules, IP6505 open hardware, and smart DIY power systems.  
Special thanks to the open hardware community for foundational work on buck converters, Li-ion safety, and microcontroller I²C comms.

---

## 💬 Get Involved

Contributions welcome! Please open an issue or pull request on [GitHub](https://github.com/YieldingData/PowerPack).

