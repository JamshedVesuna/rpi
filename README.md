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
* Here is a video of this in action: http://youtu.be/I6o5dRw-dn8

DropboxDev
-------
* dropbox_clean.py: A script to clean my `Camera Uploads/` directory and archive pictures older than 3 days.
    1. This works with a Dropbox Datastore App API. I have given my app permission to only media files.
