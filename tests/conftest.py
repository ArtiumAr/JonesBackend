import os

from restaurant_api import create_app
from restaurant_api.database.models import Order
from restaurant_api.database import db

import pytest


@pytest.fixture
def client():
    app = create_app("config.settings.TestConfig")

    with app.test_client() as client:
        yield client
