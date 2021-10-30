from . import api_views
from flask import Flask


def create_app(config_object='config.settings.DevConfig'):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config_object)

    from restaurant_api.database import db
    db.app = app
    db.init_app(app)
    db.create_all()
    app.register_blueprint(api_views.bp)

    return app