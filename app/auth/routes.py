from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.auth.forms import UserCreationForm, UserLoginForm
# from app.models import User


auth =Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods=['GET','POST'])
def signup():
    form = UserCreationForm()
    if request.method == 'POST':
        if form.validate():
            first_name = form.first_name.data
            last_name = form.last_name.data
            username = form.username.data
            email = form.email.data
            password = form.password.data

            flash('Sign up Complete', 'success')
            user = User(first_name, last_name, username, email, password)
            
            user.save_to_db()
            return redirect(url_for('auth.login'))

    return render_template('signup.html',form=form)

@auth.route('/login')
def login():
    return render_template('login.html')