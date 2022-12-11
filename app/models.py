from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash


db = SQLAlchemy()

# create models based off our ERD
class User(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True)
        first_name = db.Column(db.String(50), nullable=False)
        last_name = db.Column(db.String(50), nullable=False)
        username = db.Column(db.String(50), nullable=False, unique=True)
        email = db.Column(db.String(50), nullable=False, unique=True)
        password = db.Column(db.String(250), nullable=False)
        cart =db.relationship('Cart',backref='author', lazy=True)

        def __init__(self, first_name, last_name, username, email, password):
            self.first_name = first_name
            self.last_name = last_name
            self.username = username
            self.email = email
            self.password = generate_password_hash(password)
            
        def save_to_db(self):
            db.session.add(self)
            db.session.commit()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    img_url = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    cart =db.relationship('Cart',backref='item', lazy=True)

    def __init__(self, name, img_url, price, quantity, description):
        self.name = name
        self.img_url = img_url
        self.price=price
        self.quantity=quantity
        self.description=description

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = (db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False))
    product_id =(db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False))

    def __init__(self, user_id, product_id):
        self.user_id = user_id
        self.product_id = product_id