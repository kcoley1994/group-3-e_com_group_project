from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from .forms import Productform
from app.models import Product


christmas = Blueprint('christmas', __name__, template_folder='christmas_templates')

@christmas.route('/post')
@login_required
def view_post():
    posts = Product.query.all()
    
   

    return render_template('products.html', posts =posts)


# @christmas.route('//<int:post_id>')
# def view_post():
#     post = Product.query.all()

#     return render_template('')
