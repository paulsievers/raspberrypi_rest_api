import RPi.GPIO as GPIO
from dataclasses import dataclass

ON = 1
OFF = 0


@dataclass
class LED:
    # __slots__ = ["id", "red_pin", "green_pin", "blue_pin", "color"]
    id: int
    red_pin: int
    green_pin: int
    blue_pin: int
    color: str = "off"
    state: str = "off"

    def __post_init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.red_pin, GPIO.OUT)
        GPIO.setup(self.green_pin, GPIO.OUT)
        GPIO.setup(self.blue_pin, GPIO.OUT)
        # print(f"initialized led {self.id}")
        # pass

    def set_color(self, data):
        color = data.get("color")
        self.reset_led(OFF)

        if color == "red":
            self.red(ON)

        if color == "green":
            self.green(ON)

        if color == "blue":
            self.blue(ON)

        if color == "cyan":
            self.cyan(ON)

        if color == "purple":
            self.purple(ON)

        if color == "yellow":
            self.yellow(ON)

        if color == "white":
            self.white(ON)

        self.color = color
        print(self.color)

    def red(self, status):
        GPIO.output(self.red_pin, status)
        # pass

    def green(self, status):
        GPIO.output(self.green_pin, status)
        # pass

    def blue(self, status):
        GPIO.output(self.blue_pin, status)
        # pass

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
        self.state = "off"
