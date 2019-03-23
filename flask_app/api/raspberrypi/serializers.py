from flask_restplus import fields
from flask_app.api.restplus import api

set_color = api.model(
    "Set LED Color", {"color": fields.String(required=True, description="LED Color")}
)
