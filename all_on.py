#!/usr/bin/env python
import blinkt
import time

blinkt.set_brightness(0.1)


while True:
    for i in range(8):
        blinkt.set_pixel(i, 255, 255, 255)
        blinkt.show()
