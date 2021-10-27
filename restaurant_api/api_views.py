from flask import Blueprint

bp = Blueprint('api_views', __name__, url_prefix='/api')

@bp.route('/place_order', methods=['POST'])
def order():
    # order_confirmation = {}
    # return order_confirmation
    pass

@bp.route('/get_orders', methods=['GET'])
def get_orders():
    return {}
