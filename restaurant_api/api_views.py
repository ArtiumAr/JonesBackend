from flask import Blueprint
from restaurant_api.database.models import Order

from restaurant_api.database import db
bp = Blueprint('api_views', __name__, url_prefix='/api')

@bp.route('/place-order', methods=['POST'])
def order():
    json = request.get_json(force=True)
    order = Order(id=json['id'], customer_name=json['name'], dish=json['dish'], comments=json['comments'])
    # order_confirmation = {}
    # return order_confirmation
    pass

@bp.route('/orders', methods=['GET'])
def get_orders():
    return {}