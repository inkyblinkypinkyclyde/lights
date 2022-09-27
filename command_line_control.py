#!/usr/bin/env python3
from LightsClass import Lights

while True:
    option = input('Select (g)reen, (a)mber or (r)ed for lights or switch (o)ff lights or (e)xit\n')
    if option == 'g':
        Lights.green_on()
    elif option == 'a':
        Lights.yellow_on()
    elif option == 'r':
        Lights.red_on()
    elif option == 'o':
        Lights.off()
    elif option == 'e':
        break
