from flask import Blueprint, json, request, jsonify
from restaurant_api.database.models import MenuItem, Order
from restaurant_api.database import db
from restaurant_api.exception import InvalidUsage
import datetime
import logging


bp = Blueprint("api_views", __name__, url_prefix="/api")


@bp.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@bp.errorhandler(Exception)
def handle_generic_error(error):
    return jsonify("unexpected behavior"), 500


@bp.route("/orders", methods=["GET"])
def get_orders():
    s = datetime.datetime.strftime(
        datetime.datetime.now() - datetime.timedelta(1), "%Y-%m-%d"
    )
    result = db.session.query(Order).filter(Order.order_time >= s).all()
    return jsonify(result)


@bp.route("/place-order", methods=["POST"])
def order():
    data = request.get_json(force=True)
    customer_name = data.get("customer_name")
    dish = data.get("dish")
    comments = data.get("comments")

    if not customer_name or not dish:
        raise InvalidUsage(
            "Failed order. Wrong order format",
            status_code=500,
            payload={"args": [customer_name, dish, comments]},
        )

    exists = db.session.query(MenuItem.dish).filter_by(dish=dish).first() is not None
    if not exists:
        raise InvalidUsage(
            "Failed order. dish not in menu",
            status_code=500,
            payload={"args": [customer_name, dish, comments]},
        )

    order = Order(customer_name=customer_name, dish=dish, comments=comments)
    db.session.add(order)
    db.session.commit()
    logging.getLogger("werkzeug").info(
        "Successful order. \targs:\t name: {}, dish: {}, comments: {}".format(
            customer_name, dish, comments
        )
    )

    return {
        "order status": "success",
        "order details": order,
    }
