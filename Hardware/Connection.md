# PowerPack Project Connections

## Connections Table

| Component          | Pin                | Connected To                                   |
|--------------------|--------------------|------------------------------------------------|
| **Battery**        | Positive Terminal  | BAT+ on TP4056                                 |
|                    | Negative Terminal  | BAT- on TP4056                                 |
| **TP4056**         | BAT+               | Positive Terminal of Battery                   |
|                    | BAT-               | Negative Terminal of Battery                   |
|                    | OUT+               | Input of Buck Converter                        |
|                    | OUT-               | GND                                            |
| **Buck Converter** | Input              | OUT+ and OUT- of TP4056                        |
|                    | Output             | 5V Rail (VCC)                                  |
| **ATmega328P**     | VCC                | 5V Rail (from Buck Converter)                  |
|                    | GND                | Common Ground (GND)                            |
| **Push Button**    | PD2 (INT0)         | One terminal of Button                         |
|                    |                    | Other terminal to VCC (5V)                     |
|                    |                    | 10k ohm Pull-Down Resistor to GND              |
| **Green LED**      | PD4                | Anode through 100 ohm Resistor, Cathode to GND |
| **Red LED**        | PD5                | Anode through 150 ohm Resistor, Cathode to GND |
| **N-Channel MOSFET** | Gate              | PD3 through 10k ohm Resistor                   |
|                    | Source             | Common Ground (GND)                            |
|                    | Drain              | Negative Terminal of SBC Power Input           |
| **Voltage Divider**| R1 (28.4k ohm)     | Battery Positive Terminal                      |
|                    | Junction Point     | A1 (Analog Input on ATmega328P)                |
|                    | R2 (10k ohm)       | GND                                            |
| **Thermistor Circuit** | Thermistor (100k ohm) | VCC (5V)                              |
|                    | Junction Point     | A0 (Analog Input on ATmega328P)                |
|                    | 10k ohm Resistor   | GND                                            |
| **Capacitor**      | 0.1µF              | Across A1 (Analog Input) and GND               |

## Summary of Components
1. **Microcontroller**: ATmega328P
2. **Single Board Computer**: Raspberry Pi (or similar)
3. **Push Button**: Momentary push button switch
4. **LEDs**: Green and Red LEDs
5. **Resistors**:
   - 100 ohm (for Green LED)
   - 150 ohm (for Red LED)
   - 10k ohm (pull-down resistor for button, series resistor for thermistor, gate resistor for MOSFET)
   - 28.4k ohm (voltage divider)
6. **MOSFET**: N-channel MOSFET
7. **Voltage Regulator**: Buck converter (to step up voltage to 5V)
8. **Charging Module**: TP4056
9. **Capacitors**: 0.1µF (for noise filtering on voltage divider)
10. **Thermistor**: NTC thermistor (typically 100k ohm for 3D printer applications)
11. **Battery**: Li-ion 18650 (or similar)
