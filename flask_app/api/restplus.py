import logging

from flask_restplus import Api
from flask_app import settings

log = logging.getLogger(__name__)

api = Api(
    version="1.0",
    title="Raspberry Pi API",
    description="Flask RestPlus powered API for Raspberry Pi GPIO Pins",
)


@api.errorhandler
def default_error_handler(e):
    message = "An unhandled exception occurred."
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {"message": message}, 500
