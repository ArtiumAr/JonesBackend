from flask import jsonify
import logging


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload
        logging.getLogger("werkzeug").info("{}".format(self.to_dict()))

    def to_dict(self):
        rv = dict(self.payload or ())
        rv["message"] = self.message
        rv["order status"] = "failure"
        return rv
