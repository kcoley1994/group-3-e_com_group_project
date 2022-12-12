from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from .forms import Productform
from app.models import Product


christmas = Blueprint('christmas', __name__, template_folder='christmas_templates')

@christmas.route('/post/create', methods= ['GET','POST'])
@login_required
def create_post():
    form = Productform

    return render_template('products.html')


# @christmas.route('/posts')
# def view_post():
#     post = Product.query.all()

#     return render_template('')
