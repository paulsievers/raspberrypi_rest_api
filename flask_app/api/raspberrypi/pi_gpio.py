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

        GPIO.output(self.red, 0)
        GPIO.output(self.green, 0)
        GPIO.output(self.blue, 0)

    def setcolor(self, data):
        color = data.get("color")
        GPIO.cleanup()

        if color in ("red", "green", "blue"):
            GPIO.output(self.color, 1)

        if color == "cyan":
            GPIO.output(self.green, 1)
            GPIO.output(self.blue, 1)

        if color == "purple":
            GPIO.output(self.red, 1)
            GPIO.output(self.blue, 1)

        if color == "yellow":
            GPIO.output(self.red, 1)
            GPIO.output(self.green, 1)

        self.led_color = color

    def getcolor(self):
        return self.led_color
