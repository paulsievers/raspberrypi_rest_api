from flask_restplus import fields
from marshmallow import Schema
from marshmallow import fields as mm_fields

from flask_app.api.raspberry_pi.pi_gpio import LED
from flask_app.api.restplus import api


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
