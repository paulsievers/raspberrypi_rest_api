import logging

from flask import request
from flask_app.api.raspberrypi.pi_gpio import LED
from flask_restplus import Resource

from flask_app.api.raspberrypi.serializers import set_color
from flask_app.api.raspberrypi.parsers import color_arguments
from flask_app.api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace("raspberrypi/led", description="LED Operations")

led1 = LED()


@ns.route("/")
class LedColor(Resource):
    @api.expect(color_arguments)
    # @api.marshal_with(set_color)
    def get(self):
        """
         Get current LED color
         """
        # args = pagination_arguments.parse_args(request)
        # page = args.get("page", 1)
        # per_page = args.get("per_page", 10)

        color = led1.getcolor()
        return color

    @api.expect(color_arguments)
    # @api.marshal_with(set_color)
    def post(self):
        """
         Set LED color
         """
        led1.setcolor(request.json)
        return None, 201
