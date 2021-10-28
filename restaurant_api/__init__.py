from . import api_views
from flask import Flask


def create_app(settings_override=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')

    if settings_override:
        app.config.update(settings_override)
    
    from restaurant_api.database import db
    db.app = app
    db.init_app(app)
    db.create_all()
    app.register_blueprint(api_views.bp)

    return app