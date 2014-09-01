rpi
===

A collection of Raspberry Pi projects

DoorDev
-------
* door_server.py: A [Flask](http://flask.pocoo.org/) server that opens my door.
    1. I have an NFC tag on the outside of my door. When read, hits this server in the background.
    2. When I hold my phone up to my door, it automatically opens.
* start_server.sh: Starts up the door server in the background.
* lights.py: Simple controls for LED lights.
    1. On
    2. Off
    3. Strobe
