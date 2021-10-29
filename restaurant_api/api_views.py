from flask import Blueprint, request, jsonify
from restaurant_api.database.models import Order
from flask_sqlalchemy import SQLAlchemy
import datetime
from restaurant_api.database import db
bp = Blueprint('api_views', __name__, url_prefix='/api')

sql = SQLAlchemy()

@bp.route('/place-order', methods=['POST'])
def order():
    json = request.get_json(force=True)
    id = json['id']
    customer_name=json['customer_name']
    dish=json['dish']
    comments=json['comments']
    order = Order(id=id, customer_name=customer_name, dish=dish, comments=comments)
    db.session.add(order)
    db.session.commit()
    my_json = {"order status": "success", "order details": {"id":id, "customer_name":customer_name, "dish":dish, "comments":comments}}
    http_code = 200
    return my_json, http_code

@bp.route('/orders', methods=['GET'])
def get_orders():
    s = datetime.datetime.strftime(datetime.datetime.now()-datetime.timedelta(1),'%Y-%m-%d')
    result = db.session.query(Order)\
    .filter(Order.order_time>= s).all()
    return jsonify(result)