#!/usr/bin/env python3
import blinkt
import time

def red_on():
    blinkt.clear()
    blinkt.set_all(255, 0, 0)
    blinkt.show()

def yellow_on():
    blinkt.clear()
    blinkt.set_all(150, 64, 0)
    blinkt.show()

def green_on():
    blinkt.clear()
    blinkt.set_all(0, 128, 0)
    blinkt.show()

def off():
    blinkt.clear()
    blinkt.show()

while True:
    option = input('Select (g)reen, (a)mber or (r)ed for lights or switch (o)ff lights or (e)xit\n')
    if option == 'g':
        green_on()
    elif option == 'a':
        yellow_on()
    elif option == 'r':
        red_on()
    elif option == 'o':
        off()
    elif option == 'e':
        break
