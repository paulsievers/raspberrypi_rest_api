from time import sleep

from celery import Celery

import RPi.GPIO as GPIO
from dataclasses import dataclass

celery_app = Celery("tasks", broker="pyamqp://guest@localhost//")

ON = 1
OFF = 0


@dataclass
class LED:
    id: int
    red_pin: int
    green_pin: int
    blue_pin: int
    color: str = "off"
    mode: str = "off"

    def __post_init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.red_pin, GPIO.OUT)
        GPIO.setup(self.green_pin, GPIO.OUT)
        GPIO.setup(self.blue_pin, GPIO.OUT)

    @celery_app.task()
    def blink(self):
        while True:
            self.color_func(ON)
            sleep(1)
            self.color_func(OFF)
            sleep(1)

    def set_mode(self, mode):
        if mode == "solid":
            self.color_func(ON)
        if mode == "blink":
            self.blink.delay()

    def set_color(self, data):
        color = data.get("color")
        mode = data.get("mode")
        self.reset_led(OFF)
        self.color = color

        if color == "red":
            self.color_func = self.red
            self.set_mode(mode)

        if color == "green":
            self.color_func = self.green
            self.set_mode(mode)

        if color == "blue":
            self.color_func = self.blue
            self.set_mode(mode)

        if color == "cyan":
            self.color_func = self.cyan
            self.set_mode(mode)

        if color == "purple":
            self.color_func = self.purple
            self.set_mode(mode)

        if color == "yellow":
            self.color_func = self.yellow
            self.set_mode(mode)

        if color == "white":
            self.color_func = self.white
            self.set_mode(mode)

    def red(self, status):
        GPIO.output(self.red_pin, status)

    def green(self, status):
        GPIO.output(self.green_pin, status)

    def blue(self, status):
        GPIO.output(self.blue_pin, status)

    def yellow(self, status):
        self.red(status)
        self.green(status)

    def purple(self, status):
        self.red(status)
        self.blue(status)

    def cyan(self, status):
        self.green(status)
        self.blue(status)

    def white(self, status):
        self.red(status)
        self.green(status)
        self.blue(status)

    def reset_led(self, status):
        self.red(status)
        self.green(status)
        self.blue(status)
        self.color = "off"
        self.mode = "solid"
