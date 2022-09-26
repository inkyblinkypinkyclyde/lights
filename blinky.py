#!/usr/bin/env python
import blinkt
import time

blinkt.set_brightness(0.1)


while True:
    for i in range(8):
        blinkt.clear()
        blinkt.set_pixel(i, 255, 0, 0)
        blinkt.show()
    time.sleep(0.05)