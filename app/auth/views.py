from flask import render_template
from . import auth
from .forms import RegistrationForm
from ..models import User
from .. import db

@auth.route('/login', methods=['GET', 'SET'])
def login():
  pass

@auth.route('/register', methods = ['GET', 'SET'])
def register():
  form = RegistrationForm()

  if form.validate_on_submit():
    user = User(username=form.username.data, email=form.email.data, password_secure=form.password.data)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('auth.login'))
  
  return render_template('auth/register.html', form=form)
