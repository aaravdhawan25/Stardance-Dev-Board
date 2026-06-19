import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.extensions.rgb import RGB
from kmk.modules.macros import Macros
from kmk.keys import KC, make_key

keyboard = KMKKeyboard()

keyboard.matrix = KeysScanner(
    pins=[
        board.D0, board.D1, board.D2,
        board.D3, board.D4, board.D5
    ],
    value_when_pressed=False,  
    pull=True                  
)

rgb = RGB(
    pixel_pin=board.D10,       
    num_pixels=6,
    val_limit=100,      
    hue_default=85,
    sat_default=255,
    val_default=100,
    rgbw=False
)

keyboard.extensions.append(rgb)

macros = Macros()
keyboard.modules.append(macros)

OPEN_GIT_DESK = KC.MACRO(
    KC.LGUI(KC.SPC),
    KC.MACRO_SLEEP_MS(200),
    "github desktop",
    KC.MACRO_SLEEP_MS(200),
    KC.ENTER

)

OPEN_ANDROID_STUDIO = KC.MACRO(
    KC.LGUI(KC.SPC),
    KC.MACRO_SLEEP_MS(200),
    "android studio",
    KC.MACRO_SLEEP_MS(200),
    KC.ENTER

)

OPEN_DICSORD = KC.MACRO(
    KC.LGUI(KC.SPC),
    KC.MACRO_SLEEP_MS(200),
    "discord",
    KC.MACRO_SLEEP_MS(200),
    KC.ENTER

)

QUICK_COMMIT = KC.MACRO(
    KC.LGUI(KC.G),
    KC.MACRO_SLEEP_MS(100),
    KC.TAB,
    KC.MACRO_SLEEP_MS(100),
    KC.TAB,
    KC.MACRO_SLEEP_MS(100),
    KC.TAB,
    KC.MACRO_SLEEP_MS(100),
    KC.ENTER
)

discord_muted = False

def toggle_mute(key, keyboard, *args, **kwargs):
    global discord_muted
    discord_muted = not discord_muted 
    
    
    keyboard.tap_key(KC.LGUI(KC.LSFT(KC.M)))
    
    
    if discord_muted:
        rgb.set_hsv_fill(0, 255, 100)
    else:
        rgb.set_hsv_fill(85, 255, 100)


MUTE_BTN = make_key(on_press=toggle_mute)

keyboard.keymap = [
    [
        # Top Row
        OPEN_ANDROID_STUDIO,
        MUTE_BTN,     
        KC.LGUI(KC.V),
            

        # Bottom Row
        OPEN_GIT_DESK,     
        QUICK_COMMIT, 
        KC.LGUI(KC.P)      
    ]
]

if __name__ == '__main__':
    keyboard.go()