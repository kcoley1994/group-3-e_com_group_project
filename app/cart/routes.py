from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required

from app.models import Product, User

cart = Blueprint('cart', __name__, template_folder='cart_templates')

@cart.route('/cart/<int:product_id>')
@login_required
def my_cart(product_id):
    product = Product.query.get(product_id)
    current_user.add_to_cart(product)

    return render_template('cart.html', product = product)


@cart.route('/check')
@login_required
def checkout():

    return render_template('checkout.html')



