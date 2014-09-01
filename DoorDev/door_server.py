"""
A Flask server to activate a motor
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

def clockwise(duration):
    """Turn the motor clockwise for the duration in seconds"""
    gp.output(13, False)
    gp.output(15, True)
    time.sleep(duration)

    gp.output(13, False)
    gp.output(15, False)

def counterclockwise(duration):
    """Turn the motor counterclockwise for the duration in seconds"""
    gp.output(13, True)
    gp.output(15, False)
    time.sleep(duration)

    gp.output(13, False)
    gp.output(15, False)


@app.route('/open')
def open():
    clockwise(5)
    time.sleep(2)
    counterclockwise(1.75)

@app.route('/close')
def close():
    counterclockwise(2)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
