import RPi.GPIO as GPIO


class LED:
    def __init__(self):
        self.led_color = None
        self.red = 11
        self.green = 13
        self.blue = 12

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        GPIO.setup(self.red, GPIO.OUT)
        GPIO.setup(self.green, GPIO.OUT)
        GPIO.setup(self.blue, GPIO.OUT)

        self.reset_led()

    def setcolor(self, data):
        color = data.get("color")
        self.reset_led()

        if color in ("red", "green", "blue"):
            GPIO.output(color, 1)

        if color == "cyan":
            self.cyan()

        if color == "purple":
            self.purple()

        if color == "yellow":
            self.yellow()

        if color == "white":
            self.white()

        self.led_color = color

    def getcolor(self):
        return self.led_color

    @staticmethod
    def yellow(self):
        GPIO.output(self.red, 1)
        GPIO.output(self.green, 1)

    @staticmethod
    def purple(self):
        GPIO.output(self.red, 1)
        GPIO.output(self.blue, 1)

    @staticmethod
    def cyan(self):
        GPIO.output(self.green, 1)
        GPIO.output(self.blue, 1)

    @staticmethod
    def white(self):
        GPIO.output(self.red, 1)
        GPIO.output(self.green, 1)
        GPIO.output(self.blue, 1)

    @staticmethod
    def reset_led(self):
        GPIO.output(self.red, 0)
        GPIO.output(self.green, 0)
        GPIO.output(self.blue, 0)
