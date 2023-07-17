from threading import Thread
from time import sleep

import RPi.GPIO as GPIO


def beep():
    def _beep():
        GPIO.output(27, True)
        sleep(0.5)
        GPIO.output(27, False)

    Thread(target=_beep()).start()


def setup_buzzer():
    # buzzer off
    GPIO.setup(27, GPIO.OUT)
    GPIO.output(27, True)
