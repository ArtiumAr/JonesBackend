from . import api_views
from flask import Flask
from restaurant_api.database.models import MenuItem
import csv
import logging
import logging.handlers

def create_app(config_object='config.settings.DevConfig'):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config_object)

    from restaurant_api.database import db
    db.app = app
    db.init_app(app)
    db.create_all()
    app.register_blueprint(api_views.bp)
    
    if not MenuItem.query.all():
        load_menu(db, "restaurant_api/menu_v1.csv")

    logger = logging.getLogger('werkzeug')
    handler = logging.FileHandler('access.log')
    logger.addHandler(handler)
    
    return app

def load_menu(db, menu_file_name):
    with open(menu_file_name, 'r', encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        db.session.bulk_insert_mappings(MenuItem, [{'dish': row[0]} for row in csv_reader])
        db.session.commit()