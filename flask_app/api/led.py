import logging

from flask_restplus import Namespace, Resource, fields, reqparse
from marshmallow import Schema
from marshmallow import fields as mm_fields

from flask_app.core.pi_gpio import LED

led1 = LED(1, red_pin=3, green_pin=5, blue_pin=7)
led2 = LED(2, red_pin=8, green_pin=10, blue_pin=12)
led3 = LED(3, red_pin=11, green_pin=13, blue_pin=15)
leds = [led1, led2, led3]

log = logging.getLogger(__name__)

api = Namespace("raspberry-pi/led", description="LED Operations")


class LEDSchema(Schema):
    id = mm_fields.Integer()
    color = mm_fields.String()
    state = mm_fields.String()
    # gpio_pins = mm_fields.List(mm_fields.Dict())


validate_color = api.model(
    "LED",
    {
        "color": fields.String(required=True, example="red", description="LED Color"),
        "state": fields.String(example="solid", description="['solid', 'blink']"),
    },
)

led_attributes = api.inherit(
    "LED attributes",
    validate_color,
    {"id": fields.Integer(readOnly=True, description="LED Number")},
)


led_arguments = reqparse.RequestParser()
led_arguments.add_argument("id", type=int, choices=[1, 2, 3])


def set_led(id):
    for led_obj in leds:
        if led_obj.id == id:
            led = led_obj
            return led


@api.route("/")
class LedList(Resource):
    def get(self):
        """
         List LEDs
         """
        schema = LEDSchema(many=True)
        return schema.dump(leds)


@api.route("/<int:id>")
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
    @api.expect(LEDSchema)
    def put(self, id):
        """
         Set LED color
         """
        schema = LEDSchema()
        new_color = schema.load(api.payload)
        led = set_led(id)
        led.set_color(api.payload)
        return None, 201
