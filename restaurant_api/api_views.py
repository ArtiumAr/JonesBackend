from flask import Blueprint, request, jsonify
from restaurant_api.database.models import MenuItem, Order
from flask_sqlalchemy import SQLAlchemy
import datetime
from restaurant_api.database import db
from flask import current_app
import logging
from restaurant_api.exception import InvalidUsage

bp = Blueprint("api_views", __name__, url_prefix="/api")


@bp.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@bp.route("/place-order", methods=["POST"])
def order():
    json = request.get_json(force=True)

    customer_name = json.get("customer_name")
    dish = json.get("dish")
    comments = json.get("comments")

    if not customer_name or not dish:
        raise InvalidUsage(
            "failed order. Wrong order format",
            status_code=500,
            payload={"args": [customer_name, dish, comments]},
        )

    exists = db.session.query(MenuItem.dish).filter_by(dish=dish).first() is not None
    if not exists:
        raise InvalidUsage(
            "failed order. dish not in menu",
            status_code=500,
            payload={"args": [customer_name, dish, comments]},
        )

    order = Order(customer_name=customer_name, dish=dish, comments=comments)
    db.session.add(order)
    db.session.commit()
    my_json = {
        "order status": "success",
        "order details": {
            "id": order.id,
            "customer_name": customer_name,
            "dish": dish,
            "comments": comments,
        },
    }
    http_code = 200
    logging.getLogger("werkzeug").info(
        "successful order. \targs:\t name: {}, dish: {}, comments: {}".format(
            customer_name, dish, comments
        )
    )

    return my_json, http_code


@bp.route("/orders", methods=["GET"])
def get_orders():
    s = datetime.datetime.strftime(
        datetime.datetime.now() - datetime.timedelta(1), "%Y-%m-%d"
    )
    result = db.session.query(Order).filter(Order.order_time >= s).all()
    return jsonify(result)
