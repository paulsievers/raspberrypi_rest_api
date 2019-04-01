import pytest
from flask import url_for

import flask_restplus as restplus


# class TestApp:
#     def test_app(self, app):
#         assert app.get("/").status_code == 200


class APITest(object):
    def test_root_endpoint(self, app):
        api = restplus.Api(app, version="1.0")

        with app.test_request_context():
            url = url_for("root")
            assert url == "/"
            assert api.base_url == "http://localhost/"

    def test_root_endpoint_lazy(self, app):
        api = restplus.Api(version="1.0")
        api.init_app(app)

        with app.test_request_context():
            url = url_for("root")
            assert url == "/"
            assert api.base_url == "http://localhost/"


# def test_root_url(client):
#     # rv = app.get('/')
#     assert client.get("/").status_code == 200
