# AD Dev Pad

This is the **AD Dev Pad**, a custom 6-key mechanical macropad I designed and built from scratch to make my coding workflow way faster. I was getting tired of clicking through menus just to mute Discord or push my code, so I made this board to handle all my repetitive tasks. 

<img width="852" height="615" alt="cad" src="https://github.com/user-attachments/assets/1cfe9879-109c-42e7-9c82-ce4c78b9ec70" />


## Features
I programmed this specifically for a Mac developer environment. It handles a lot more than just typing basic shortcuts!

* **Smart Discord Mute:** The top-left button does the `Cmd + Shift + M` shortcut to toggle mute. But the coolest part is that the Python code actually tracks the state, so when I'm muted, the entire board's underglow turns **RED** as a indicator. When I unmute, it goes back to my default which is **GREEN**.
* **No Mouse Github Commands:** I have dedicated keys that launch Mac Spotlight, type "github desktop", wait for it to load, and hit enter. Another key runs a full sequence to auto-commit, and another instantly pushes the code.
  
* **Basic Necessity stuff:** Easy keys to Copy (`Cmd + C`), Paste (`Cmd + V`), and Undo (`Cmd + Z`).

## Hardware and PCB
I designed the board myself using KiCad. I wanted it to be simple but look really clean, so I added some custom silkscreen graphics on the front and back that mix my initials (AD) with a GitHub cat because it's cool.

<img width="559" height="550" alt="pcb" src="https://github.com/user-attachments/assets/1cb1e0b9-0b96-4480-92fe-142a5bb47080" />


### Parts List
* **Microcontroller:** Seeed Studio XIAO. It is super tiny but has exactly enough pins for this project.
* **Switches:** 6 standard mechanical keyboard switches. 
* **Wiring:** I used a "direct-to-pin" setup. Every single switch gets its own dedicated pin on the XIAO and pulls straight to Ground. No complicated matrix or diodes needed!
* **RGB LEDs:** 6 `SK6812MINI-E` reverse-mount LEDs. They are soldered onto the bottom of the board and shine *up* through cutouts in the PCB directly into the bottom of the switches.

<img width="896" height="707" alt="schematic" src="https://github.com/user-attachments/assets/0f8abd7a-2cff-4dc3-ba84-738db7ec1a29" />


## Firmware
I didn't want to mess with compiling complicated C code, so this board runs on **KMK**. 

The XIAO literally just shows up on my computer like a USB flash drive. If I want to change a macro, I just open `code.py` in a text editor, change the shortcut, and hit save. Then It updates instantly. 

*Note for anyone building this: The LEDs are powered directly from the XIAO's `3V3` pin. Because that pin can only handle about 200mA before the board gets too hot, I capped the RGB brightness (`val_limit=100`) in the code to keep everything safe!*
