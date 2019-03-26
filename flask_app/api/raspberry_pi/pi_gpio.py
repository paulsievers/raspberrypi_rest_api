# import RPi.GPIO as GPIO
from marshmallow import Schema, fields as mm_fields, post_load


class LEDSchema(Schema):
    id = mm_fields.Integer()
    color = mm_fields.String()

    @post_load
    def create_led_instance(self, id):
        return LED(id)


class LED:
    def __init__(self, id):
        self.id = id
        self.color = None
        self.set_gpio_pins()

        self.on = 1
        self.off = 0

        # GPIO.setmode(GPIO.BOARD)
        # GPIO.setwarnings(False)

        # GPIO.setup(self.red_pin, GPIO.OUT)
        # GPIO.setup(self.green_pin, GPIO.OUT)
        # GPIO.setup(self.blue_pin, GPIO.OUT)

        self.reset_led(self.off)

    def __getitem__(self, index):
        return self.id[index]

    def set_gpio_pins(self):
        if self.id == 1:
            self.red_pin = 11
            self.green_pin = 13
            self.blue_pin = 12

    def set_color(self, data):
        color = data.get("color")
        self.reset_led(self.off)

        if color == "red":
            self.red(self.on)
            self.color = "red"

        if color == "green":
            self.green(self.on)
            self.color = "green"

        if color == "blue":
            self.blue(self.on)
            self.color = "blue"

        if color == "cyan":
            self.cyan(self.on)
            self.color = "cyan"

        if color == "purple":
            self.purple(self.on)

        if color == "yellow":
            self.yellow(self.on)

        if color == "white":
            self.white(self.on)

        self.color = color
        print(self.color)

    def red(self, status):
        # GPIO.output(self.red_pin, status)
        pass

    def green(self, status):
        # GPIO.output(self.green_pin, status)
        pass

    def blue(self, status):
        # GPIO.output(self.blue_pin, status)
        pass

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
