"""
Turn LEDs on, off, and strobe
git@github.com:JamshedVesuna/rpi.git
"""

import RPi.GPIO as gp
import time


gp.setwarnings(False)
gp.setmode(gp.BOARD)
gp.setup(7, gp.OUT)
gp.setup(11, gp.OUT)
gp.setup(13, gp.OUT)
gp.setup(15, gp.OUT)

gp.output(7, True)
gp.output(11, True)


def on(self):
    gp.output(13, False)
    gp.output(15, True)

def off(self):
    gp.output(13, False)
    gp.output(15, False)

def strobe(self):
    while True:
        time.sleep(0.1)
        self.on()
        time.sleep(0.1)
        self.off()
