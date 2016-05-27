import RPi.GPIO as GPIO
import max7219.led as led
import time
from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT
from random import randrange

device = led.matrix(cascaded=4)
msg = 'www.1001000.io/area51'
try:
    while True:
        device.show_message(msg, font=proportional(CP437_FONT))
        device.flush()
except:
    device.flush()
    GPIO.cleanup()