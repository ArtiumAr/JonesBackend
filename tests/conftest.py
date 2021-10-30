import os

from restaurant_api import create_app
from restaurant_api.database.models import Order
from restaurant_api.database import db

import pytest


@pytest.fixture
def client():
    app = create_app('config.settings.TestConfig')
    db.app = app
    db.init_app(app)
    db.create_all()

    with app.test_client() as client:
        yield client