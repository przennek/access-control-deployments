#!/bin/bash

cd /home/pc/mjpg-streamer-experimental
./mjpg_streamer -i "input_uvc.so -d /dev/video0 -r 640x480 -f 12" -o "output_http.so -w ./www"&