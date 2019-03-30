import logging.config
import os

from flask import Flask

from raspberrypi_rest_api import settings
from raspberrypi_rest_api.api import blueprint as api

app = Flask(__name__)
app.config["SERVER_NAME"] = settings.FLASK_SERVER_NAME
app.config["SWAGGER_UI_DOC_EXPANSION"] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
app.config["RESTPLUS_VALIDATE"] = settings.RESTPLUS_VALIDATE
app.config["RESTPLUS_MASK_SWAGGER"] = settings.RESTPLUS_MASK_SWAGGER
app.config["ERROR_404_HELP"] = settings.RESTPLUS_ERROR_404_HELP
app.register_blueprint(api, url_prefix="/api")

logging_conf_path = os.path.normpath(
    os.path.join(os.path.dirname(__file__), "../logging.conf")
)
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)


def configure_app(flask_app):
    flask_app.config["SERVER_NAME"] = settings.FLASK_SERVER_NAME
    flask_app.config[
        "SWAGGER_UI_DOC_EXPANSION"
    ] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config["RESTPLUS_VALIDATE"] = settings.RESTPLUS_VALIDATE
    flask_app.config["RESTPLUS_MASK_SWAGGER"] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config["ERROR_404_HELP"] = settings.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)

    # blueprint = Blueprint("api", __name__, url_prefix="/api")
    # api.init_app(blueprint)
    # api.add_namespace(raspberrypi_led_namespace)
    # flask_app.register_blueprint(blueprint)


def main():
    initialize_app(app)
    log.info(
        ">>>>> Starting development server at http://{}/api/ <<<<<".format(
            app.config["SERVER_NAME"]
        )
    )
    app.run(debug=settings.FLASK_DEBUG)


if __name__ == "__main__":
    main()
