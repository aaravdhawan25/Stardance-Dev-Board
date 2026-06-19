Stardance Dev Board

A custom 6-key macropad built from the ground up for streaming, programming, and productivity. Powered by the Seeed Studio XIAO and featuring brilliant per-key RGB lighting.

## ✨ Features

* **Compact 6-Key Layout:** A perfectly symmetrical 3x2 grid, ideal for macro execution, app launching, or stream deck controls.
* **Per-Key RGB:** Utilizes reverse-mounted SK6812MINI-E LEDs shining through custom PCB cutouts for vibrant, diffused lighting.
* **XIAO Core:** Driven by the tiny but mighty Seeed Studio XIAO microcontroller (RP2040).
* **Custom PCB:** Designed in KiCad with a clean 2-layer routed matrix and a custom developer silkscreen logo on the bottom layer.
* **Open-Source Firmware:** Compatible with both QMK and KMK firmware ecosystems.
* **3D Printable Case:** Includes STL files for a sleek, low-profile housing perfectly fitted for the board and USB-C port.

## 🛠️ Bill of Materials (BOM)

To build your own Stardance Dev Board, you will need:

| Component | Quantity | Notes |
| :--- | :---: | :--- |
| **Seeed Studio XIAO** | 1 | RP2040 recommended for optimal KMK/QMK support. |
| **Mechanical Switches** | 6 | Any Cherry MX-compatible switch (5-pin or 3-pin). |
| **SK6812MINI-E LEDs** | 6 | Must be the "-E" (Reverse-Mount/Embedded) variant. |
| **Keycaps** | 6 | Transparent or shine-through keycaps recommended for the LEDs. |
| **Custom PCB** | 1 | Fabricated from the provided Gerber files. |

## 🖨️ Hardware & PCB

The PCB was designed from scratch in KiCad. The matrix utilizes a top-layer (Red) and bottom-layer (Blue) routing strategy to avoid short circuits, with vias safely transitioning the signals. 

* **`/Hardware`**: Contains the raw KiCad project files (`.kicad_pro`, `.kicad_sch`, `.kicad_pcb`).
* **`/Gerbers`**: Contains the generated, production-ready `.zip` file. You can upload this directly to manufacturers like JLCPCB or PCBWay.
* **`/Case`**: Contains the `.stl` files for 3D printing the enclosure.

## 💻 Firmware Setup

*(Add your specific QMK or KMK installation instructions, pinout definitions, and flashing guide here once your code is ready!)*

---
*Designed and built by Aarav Dhawan.*
