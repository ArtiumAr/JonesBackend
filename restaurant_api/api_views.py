from flask import Blueprint, request, jsonify
from restaurant_api.database.models import MenuItem, Order
from flask_sqlalchemy import SQLAlchemy
import datetime
from restaurant_api.database import db
bp = Blueprint('api_views', __name__, url_prefix='/api')

sql = SQLAlchemy()


@bp.route('/place-order', methods=['POST'])
def order():
    json = request.get_json(force=True)

    customer_name=json['customer_name']
    dish=json['dish']
    comments=json['comments']

    if customer_name and dish:
        exists = db.session.query(MenuItem.dish).filter_by(dish=dish).first() is not None
        if exists:
            order = Order(customer_name=customer_name, dish=dish, comments=comments)
            db.session.add(order)
            db.session.commit()
            my_json = {"order status": "success", "order details": {"id":order.id, "customer_name":customer_name, "dish":dish, "comments":comments}}
            http_code = 200
        else:
            my_json = {"order status": "failure", "error":"dish not on menu"}
            http_code = 500
    else:
        my_json = {"order status": "failure", "error":"bad order format"}
        http_code = 500
    return my_json, http_code

@bp.route('/orders', methods=['GET'])
def get_orders():
    s = datetime.datetime.strftime(datetime.datetime.now()-datetime.timedelta(1),'%Y-%m-%d')
    result = db.session.query(Order)\
    .filter(Order.order_time>= s).all()
    return jsonify(result)