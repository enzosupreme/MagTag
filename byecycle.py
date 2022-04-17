# Write your code here :-)
# Write your code here :-)
import board
import random
import time
import terminalio
from colorpallette import colors
from adafruit_magtag.magtag import MagTag

magtag = MagTag()

magtag.add_text(
    text_font=terminalio.FONT,
    text_position=(
        50,
        (magtag.graphics.display.height // 2) -1,
    ),
    text_scale=3,
)

plaintext = [
    "  Goodbye",
    " Take Care",
    " Au Revoir",
    " Sayonara",
    "   Adios",
    "  See ya",
    "Wiedersehen",
    " Annyeong",
    "   Aloha",
]
a = 50
b = 4
color_range = random.randrange(a,255,1)

light_color = [
    colors.RED,
    colors.ORANGE,
    colors.YELLOW,
    colors.NEON,
    colors.GREEN,
    colors.MINT,
    colors.BLUE,
    colors.MAGENTA,
    colors.CYBER,

]

buttons = magtag.peripherals.buttons

button_colors = (0,0,0,0)
color_select = 0
color_rand2 = 0

pressed = 0;

click = False
def color_correct(col_pal):
    color_temp = (9 % col_pal) + 4
    if color_temp >= 9:
        color_rand2 = (color_temp - 9) + (9-5)
        return color_rand2
    else:
        color_rand2 = color_temp
        return color_rand2

def color_press(pressed):
        for i in range(0,9,1):
            color_select = random.randrange(1,9,1)
            color_correct(color_select)
            button_colors = (light_color[i],light_color[color_select],
            light_color[color_select],light_color[color_correct(color_select)])
            if pressed is 2:
                magtag.set_text(plaintext[color_select])
            magtag.set_text(plaintext[i])
            magtag.peripherals.neopixels.fill(button_colors[pressed])
            time.sleep(1)


while True:
    magtag.peripherals.neopixel_disable = True
    time.sleep(1)
    if magtag.peripherals.button_a_pressed:
            magtag.peripherals.play_tone(10,0.15)
            time.sleep(.02)
            color_press(0)
    if magtag.peripherals.button_b_pressed:
            magtag.peripherals.play_tone(10,0.15)
            time.sleep(0.2)
            color_press(1)
    if magtag.peripherals.button_c_pressed:
            magtag.peripherals.play_tone(10,0.15)
            time.sleep(0.2)
            color_press(2)
    if magtag.peripherals.button_d_pressed:
            magtag.peripherals.play_tone(10, 0.15)
            time.sleep(0.2)
            color_press(3)
    # Write your code here :-)
# Write your code here :-)

