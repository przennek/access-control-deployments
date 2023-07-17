#!/usr/bin/python

import RPi.GPIO as GPIO


def setup_gpio():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
