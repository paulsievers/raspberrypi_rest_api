from flask_restplus import reqparse

color_arguments = reqparse.RequestParser()
color_arguments.add_argument(
    "color", type=str, choices=["red", "green", "blue", "cyan", "purple", "yellow"]
)
