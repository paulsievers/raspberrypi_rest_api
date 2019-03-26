import logging
import json
from flask import request
from flask_restplus import Resource
from flask_app.api.raspberry_pi.pi_gpio import LED, LEDSchema
from flask_app.api.raspberry_pi.parsers import led_arguments
from flask_app.api.raspberry_pi.serializers import validate_color, led_attributes
from flask_app.api.restplus import api

led1 = LED(1)
led2 = LED(2)
led3 = LED(3)
led1.color = "red"
led2.color = "green"
led3.color = "blue"
leds = [led1, led2, led3]

log = logging.getLogger(__name__)

ns = api.namespace("raspberry-pi/led", description="LED Operations")


def set_led(id):
    for led_obj in leds:
        if led_obj.id == id:
            led = led_obj
            return led


@ns.route("/")
class LedList(Resource):
    def get(self):
        """
         List LEDs
         """
        schema = LEDSchema(many=True)
        print(type(leds))
        return schema.dump(leds)


@ns.route("/<int:id>")
class LedColor(Resource):
    # @api.expect(led_arguments)
    def get(self, id):
        """
         Get current LED color
         """
        schema = LEDSchema()
        led = set_led(id)
        return schema.dump(led)

    # @api.marshal_with(led_arguments)
    @api.expect(validate_color)
    def put(self, id):
        """
         Set LED color
         """
        schema = LEDSchema()
        new_color = schema.load(api.payload)
        led = set_led(id)
        led.set_color(api.payload)
        return None, 201
