import board
import time
import usb_hid

from adafruit_apds9960.apds9960 import APDS9960
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

i2c = board.STEMMA_I2C()
apds = APDS9960(i2c)
apds.enable_color = True
apds.color_integration_time = 37
# pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

# The keyboard object!
time.sleep(1)
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

while True:

    r, g, b, m = apds.color_data
    # ensure that the sleep time is longer than the color_integration_time
    time.sleep(0.05)
    r, g, b, n = apds.color_data

    # set up the variable to detect the change of the light intensity
    dif = n - m

    # an 'escape hatch', if the light intensity is too weak, the program breaks out of the loop
    if  r < 15 and g < 15 and b < 15:
        break

    # disregard the slight change between two color detections
    elif dif > 10:
        keyboard_layout.write("Crazy Thursday !!!")
        keyboard.press(Keycode.RETURN)
        keyboard.release_all()
    elif dif < -10:
        keyboard_layout.write("V me 50")
        keyboard.press(Keycode.RETURN)
        keyboard.release_all()
