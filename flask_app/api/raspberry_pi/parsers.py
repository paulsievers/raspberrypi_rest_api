from flask_restplus import reqparse

led_arguments = reqparse.RequestParser()
led_arguments.add_argument("id", type=int, choices=[1, 2, 3])
# led_arguments.add_argument(
#     "color",
#     type=str,
#     choices=["red", "green", "blue", "cyan", "purple", "yellow", "white"],
# )
