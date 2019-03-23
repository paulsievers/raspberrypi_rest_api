import logging

from flask import request
from flask_app.api.raspberrypi.pi_gpio import LED
from flask_restplus import Resource

from flask_app.api.raspberrypi.serializers import set_color
from flask_app.api.raspberrypi.parsers import color_arguments
from flask_app.api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace("raspberrypi/led", description="LED Operations")


@ns.route("/")
class LedColor(Resource):
    def __init__(self):
        self.led_a = LED()

    # @api.marshal_with(set_color)
    @api.expect(color_arguments)
    def get(self):
        """
         Get current LED color
         """
        # args = pagination_arguments.parse_args(request)
        # page = args.get("page", 1)
        # per_page = args.get("per_page", 10)

        color = self.led_a.getcolor()
        return color

    @api.expect(set_color)
    # @api.marshal_with(set_color)
    def post(self):
        """
         Set LED color
         """
        data = request.get_json()
        print(data)
        self.led_a.setcolor(data)
        return None, 201
