from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from dataclasses import dataclass

db = SQLAlchemy()

@dataclass
class Order(db.Model):
    id:int
    customer_name:str
    dish:str
    comments:str
    order_time:datetime

    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(80), unique=True, nullable=False)
    dish = db.Column(db.String(120), unique=True, nullable=False)
    comments = db.Column(db.String(120), unique=True, nullable=False)
    order_time = db.Column(db.DateTime(), index=True, default=datetime.now())

    def __repr__(self):
        return "Order {}:\n\tcustomer : {}\n\tdish:{}\n\tcomments:{}\n\torder time:{}".format(self.id, self.customer_name, self.dish, self.comments, self.order_time)