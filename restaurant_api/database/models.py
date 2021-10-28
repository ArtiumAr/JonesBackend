from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    dish = db.Column(db.String(120), unique=True, nullable=False)
    comments = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return "Order: {}:\n\tcustomer : {}\n\tdish:{}\n\tcomments:{}".format(self.id, self.username, self.dish, self.comments)