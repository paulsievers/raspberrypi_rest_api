import RPi.GPIO as GPIO
from dataclasses import dataclass

ON = 1
OFF = 0


@dataclass
class GpioPins:
    red: int
    green: int
    blue: int


@dataclass
class LED:
    # __slots__ = ["id", "red_pin", "green_pin", "blue_pin", "color"]
    id: int
    gpio_pins: list = GpioPins
    color: str = "off"
    state: str = "off"

    def __post_init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.gpio_pins.red, GPIO.OUT)
        GPIO.setup(self.gpio_pins.green, GPIO.OUT)
        GPIO.setup(self.gpio_pins.blue, GPIO.OUT)
        print(f"initialized led {self.id}")
        pass

    def set_color(self, data):
        color = data.get("color")
        state = data.get("state")
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
        self.state = state
        print(self.color)

    def red(self, status):
        GPIO.output(self.gpio_pins.red, status)

    def green(self, status):
        GPIO.output(self.gpio_pins.green, status)

    def blue(self, status):
        GPIO.output(self.gpio_pins.blue, status)

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
