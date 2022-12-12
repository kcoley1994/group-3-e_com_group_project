from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required

cart = Blueprint('cart', __name__, template_folder='cart_templates')

# @cart.route()
# @login_required
# def my_cart():


#     return render_template('cart.html')


@cart.route('/check')
@login_required
def checkout():

    return render_template('checkout.html')



