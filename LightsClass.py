import blinkt

class Lights:
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