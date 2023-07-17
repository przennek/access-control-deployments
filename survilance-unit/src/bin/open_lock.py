#!/usr/bin/python

import RPi.GPIO as GPIO
from common import setup_gpio
from buzzer import setup_buzzer, beep

if __name__ == "__main__":
    setup_gpio()
    setup_buzzer()

    beep()

    # open lock
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17, True)
