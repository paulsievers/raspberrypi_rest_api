import pytest
from flask import url_for


class TestApp:
    def test_app(self, client):
        assert client.get("/").status_code == 200
