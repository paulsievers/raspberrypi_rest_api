from flask_restplus import fields

from flask_app.api.restplus import api
from flask_app.api.raspberry_pi.pi_gpio import LED


validate_color = api.model(
    "LED", {"color": fields.String(requ1ired=True, description="LED Color")}
)

led_attributes = api.inherit(
    "LED attributes",
    validate_color,
    {"id": fields.Integer(readOnly=True, description="LED Number")},
)
