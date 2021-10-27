import os
from . import api_views
from flask import Flask


def create_app(passed_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='temp',
        # DATABASE=os.path.join(app.instance_path, 'restaurant_api.sqlite'),
    )

    if passed_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(passed_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(api_views.bp)

    return app