from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required, Email, EqualTo
from ..models import User


class RegistrationForm(FlaskForm):
  classes={ 'class':  '' }
  username = StringField('Enter your username', validators=[Required()])
  email = StringField('Your Email Address', validators=[Required()])
  password = PasswordField('Password', validators=[Required(), EqualTo('password_confirm', message='passwords must match')])
  password_confirm = PasswordField('Confirm passwords', validators=[Required()])
  submit = SubmitField('Sign up')
