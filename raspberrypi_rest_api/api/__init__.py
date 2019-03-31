from flask import Blueprint
from flask_restplus import Api

from .led import api as raspberrypi_led

blueprint = Blueprint("api", __name__)

api = Api(
    blueprint,
    title="Raspberry Pi API",
    version="1.0",
    description="Flask RestPlus powered API for Raspberry Pi GPIO Pins",
)

api.add_namespace(raspberrypi_led)
