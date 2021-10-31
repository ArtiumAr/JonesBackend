from flask import Blueprint, request, jsonify
from restaurant_api.database.models import MenuItem, Order
from flask_sqlalchemy import SQLAlchemy
import datetime
from restaurant_api.database import db
from flask import current_app
import logging

bp = Blueprint("api_views", __name__, url_prefix="/api")


@bp.route("/place-order", methods=["POST"])
def order():
    json = request.get_json(force=True)

    customer_name = json.get("customer_name")
    dish = json.get("dish")
    comments = json.get("comments")

    if not customer_name or not dish:
        my_json = {"order status": "failure", "error": "wrong order format"}
        http_code = 500
        logging.getLogger("werkzeug").info(
            "failed order.\t wrong order format. \targs:\t name: {}, dish: {}, comments: {}".format(
                customer_name, dish, comments
            )
        )
        return my_json, http_code

    exists = db.session.query(MenuItem.dish).filter_by(dish=dish).first() is not None
    if not exists:
        my_json = {"order status": "failure", "error": "dish not in menu"}
        http_code = 500
        logging.getLogger("werkzeug").info(
            "failed order.\t dish not in menu. \targs:\t name: {}, dish: {}, comments: {}".format(
                customer_name, dish, comments
            )
        )
        return my_json, http_code

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
