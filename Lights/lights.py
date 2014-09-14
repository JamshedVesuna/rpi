"""
Turn LEDs on, off, and strobe
git@github.com:JamshedVesuna/rpi.git
"""

import RPi.GPIO as gp
import time
from flask import Flask


app = Flask(__name__)

gp.setwarnings(False)
gp.setmode(gp.BOARD)
gp.setup(7, gp.OUT)
gp.setup(11, gp.OUT)
gp.setup(13, gp.OUT)
gp.setup(15, gp.OUT)

gp.output(7, True)
gp.output(11, True)


@app.route('/on')
def on():
    gp.output(13, False)
    gp.output(15, True)

@app.route('/off')
def off():
    gp.output(13, False)
    gp.output(15, False)

@app.route('/strobe')
def strobe():
    while True:
        time.sleep(0.1)
        on()
        time.sleep(0.1)
        off()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
