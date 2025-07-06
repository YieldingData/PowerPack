## 🔌 PowerPack v1 — Inputs & Outputs

### 🔋 Power Connections

| Name         | Type     | Direction | Description                                      |
|--------------|----------|-----------|--------------------------------------------------|
| `VBAT_IN`    | Power    | Input     | Battery input (3.7–6V), connected via JST or pads |
| `VUSB_OUT`   | Power    | Output    | 5V regulated output to SBC (via USB-A, USB-C, or pads) |
| `GND`        | Power    | GND       | Shared ground                                    |

---

### 📡 Communication (to SBC)

| Name          | Type     | Direction | Description                            |
|---------------|----------|-----------|----------------------------------------|
| `SDA`         | Digital  | Bi-dir    | I²C data line                          |
| `SCL`         | Digital  | Bi-dir    | I²C clock line                         |
| `HEARTBEAT`   | Digital  | Input     | Optional signal from SBC to indicate it’s still alive |
| `HOLD`        | Digital  | Input     | Optional hardware hold to delay or force shutdown |

---

### 🧠 Programming (UPDI)

| Name    | Type     | Direction | Description                            |
|---------|----------|-----------|----------------------------------------|
| `UPDI`  | Digital  | I/O       | 1-wire UPDI programming line for ATTiny1616 |
| `VCC`   | Power    | Input     | Supplied by programmer during flashing |
| `GND`   | Power    | GND       | Common ground                          |

---

### 🔧 Control Inputs

| Name         | Type     | Direction | Description                           |
|--------------|----------|-----------|---------------------------------------|
| `PWR_BTN`    | Digital  | Input     | Button for power-on/off               |
| `MODE_SEL`   | Analog   | Input     | Optional jumper or solder pad voltage divider for config selection |

---

### 📈 Sensing Inputs

| Name            | Type     | Direction | Description                                        |
|-----------------|----------|-----------|----------------------------------------------------|
| `TEMP_SENSE_EXT`| Analog   | Input     | External thermistor (10k NTC) for battery pack monitoring |
| `TEMP_SENSE_INT`| Analog   | Internal  | Onboard thermistor for ambient PCB temp sensing     |
| `VBAT_SENSE`    | Analog   | Internal  | Voltage divider connected to battery, may be exposed as test pad `T_VBAT` |

---

### 💡 Indicator Outputs

| Name        | Type     | Direction | Description                       |
|-------------|----------|-----------|-----------------------------------|
| `LED_PWR`   | Digital  | Output    | Power state indicator             |
| `LED_CHG`   | Digital  | Output    | Charging / full indicator         |
| `LED_WARN`  | Digital  | Output    | Optional: low battery, overtemp   |

---

### 🧪 Test Pads (Optional for Debugging)

| Name        | Purpose                                   |
|-------------|-------------------------------------------|
| `T_VBAT`    | Battery voltage sense (ADC input test pad)|
| `T_5VOUT`   | 5V regulated output pad                   |
| `T_SDA/SCL` | I²C line probing                          |
| `T_UPDI`    | UPDI programming pad                      |


