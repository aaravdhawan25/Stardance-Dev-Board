#  Dev Pad 

Hey! This is the **AD Dev Pad**, a custom 6-key mechanical macropad I designed and built from scratch to make my coding and streaming workflow way faster. I was getting tired of clicking through menus just to mute Discord or push my code, so I made this board to handle all my repetitive tasks. 

![3D Printed Case](cad.jpg)

## Features & Macros
I programmed this specifically for a Mac developer environment. It handles a lot more than just typing basic shortcuts!

* **Smart Discord Mute:** The top-left button hits `Cmd + Shift + M` to toggle mute. But the coolest part is that the Python code actually tracks the state, so when I'm muted, the entire board's underglow turns solid **RED** as a live warning. When I unmute, it goes back to my default "hacker green."
* **Zero-Mouse GitHub:** I have dedicated keys that launch Mac Spotlight, type "github desktop", wait for it to load, and hit enter. Another key runs a full sequence to auto-commit, and another instantly pushes the code.
* **Basic Utility:** Fast access to Copy, Paste, and Undo (`Cmd + Z`).

## Hardware & PCB Design
I designed the board myself using KiCad. I wanted it to be simple but look really clean, so I added some custom silkscreen graphics on the front and back that mix my initials (AD) with a GitHub commit graph.

![PCB Routing](pcb.png)

### Parts List
* **Microcontroller:** Seeed Studio XIAO. It is super tiny but has exactly enough pins for this project.
* **Switches:** 6 standard mechanical keyboard switches. 
* **Wiring:** I used a "direct-to-pin" setup. Every single switch gets its own dedicated pin on the XIAO and pulls straight to Ground. No complicated matrix or diodes needed!
* **RGB LEDs:** 6 `SK6812MINI-E` reverse-mount LEDs. They are soldered onto the bottom of the board and shine *up* through cutouts in the PCB directly into the bottom of the switches.

![Wiring Schematic](schematic.png)

## Firmware
I didn't want to mess with compiling complicated C code, so this board runs on **KMK** (CircuitPython). 

Because it's CircuitPython, the XIAO literally just shows up on my computer like a USB flash drive. If I want to change a macro, I just open `code.py` in a text editor, change the shortcut, and hit save. It updates instantly. 

*Note for anyone building this: The LEDs are powered directly from the XIAO's `3V3` pin. Because that pin can only handle about 200mA before the board gets too hot, I capped the RGB brightness (`val_limit=100`) in the code to keep everything safe!*