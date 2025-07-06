# 📌 ATTiny1616 Pin Map — PowerPack v1

This document defines how each physical pin of the ATTiny1616 (SOIC-20 or QFN-20) is assigned to support the hardware interfaces of PowerPack v1.

---

## 🔢 Pin Assignments

| Pin # | ATTiny1616 Pin | Signal Name         | Type        | Description                                       |
|-------|----------------|---------------------|-------------|---------------------------------------------------|
| 1     | PA0            | `UPDI`              | UPDI        | 1-wire programming line (can share with `LED_PWR` if needed) |
| 2     | PA1            | `LED_PWR`           | Output      | Power state LED                                   |
| 3     | PA2            | `SDA`               | I²C         | I²C data line to SBC                              |
| 4     | PA3            | `SCL`               | I²C         | I²C clock line to SBC                             |
| 5     | PA4            | `PWR_BTN`           | Input       | Power on/off button input                         |
| 6     | PA5            | `HEARTBEAT`         | Input       | Optional SBC heartbeat input                      |
| 7     | PA6            | `HOLD`              | Input       | Optional force shutdown or safety hold line       |
| 8     | PA7            | `LED_CHG`           | Output      | Charge/full status LED                            |
| 9     | PB5            | `LED_WARN`          | Output      | Low battery or overtemp warning LED               |
| 10    | PB4            | `MODE_SEL`          | Analog In   | Voltage divider for solder jumper config selection|
| 11    | PB3            | `TEMP_SENSE_EXT`    | Analog In   | External thermistor near battery pack             |
| 12    | PB2            | `TEMP_SENSE_INT`    | Analog In   | Onboard thermistor for ambient sensing            |
| 13    | PB1            | `VBAT_SENSE`        | Analog In   | Voltage divider for battery level monitoring      |
| 14    | PB0            | `SWITCH_EN`         | Output      | **Main power switch (MOSFET gate control)**       |
| 15    | PC0            | (Unused / Spare)    | GPIO        | General-purpose or future use                     |
| 16    | PC1            | (Unused / Spare)    | GPIO        | General-purpose or future use                     |
| 17    | VDD            | `VCC`               | Power       | Logic power (3.3V or 5V regulated)                |
| 18    | GND            | `GND`               | Power       | Ground                                            |
| 19    | PC2            | (Unused / Spare)    | GPIO        | General-purpose or debug output                   |
| 20    | PC3            | (Unused / Spare)    | GPIO        | General-purpose or debug output                   |

---

## 🧠 Summary

- **Total used pins:** 14  
- **Available spare pins:** 4 (PC0–PC3)   

---

## 🔍 Key Features Confirmed in Pin Map

- ✅ Main power switch (`SWITCH_EN`)  
- ✅ Button input for startup/shutdown  
- ✅ I²C communication to host SBC  
- ✅ Battery voltage monitoring  
- ✅ External & internal temperature sensors  
- ✅ LED indicators for state, charging, and error  
- ✅ Optional heartbeat and hold pins for system safety  
- ✅ Optional mode select for input config or behavior  
- ✅ Spare pins for future expansion or test/debug


