from flask import render_template, redirect, url_for, flash, request
from . import auth
from .forms import RegistrationForm, LoginForm
from ..models import User
from .. import db
from flask_login import login_user

@auth.route('/login', methods=['GET', 'SET'])
def login():
  form = LoginForm()

  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()

    if user is not None and user.verify_password(form.password.data):
      login_user(user, form.remember.data)
      return redirect(request.args.get('next')) or url_for('index.html')

    flash('Invalid username or Password')

  return render_template('auth/login.html', form=form)

@auth.route('/register', methods = ['GET', 'SET'])
def register():
  form = RegistrationForm()

  if form.validate_on_submit():
    user = User(username=form.username.data, email=form.email.data, password_secure=form.password.data)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('auth.login'))
  
  return render_template('auth/register.html', form=form)
