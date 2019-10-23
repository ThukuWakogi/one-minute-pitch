from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import Required, Email, EqualTo
from ..models import User


class RegistrationForm(FlaskForm):
  username = StringField('Enter your username', validators=[Required()])
  email = StringField('Your Email Address', validators=[Required()])
  password = PasswordField('Password', validators=[Required(), EqualTo('password_confirm', message='passwords must match')])
  password_confirm = PasswordField('Confirm passwords', validators=[Required()])
  submit = SubmitField('Sign up')

  def validate_email(self, data_field):
    if User.query.filter_by(email=data_field.data).first():
      raise ValidationError('This email is already used')

class LoginForm(FlaskForm):
  email = StringField('Your Email Address', validators=[Required()])
  password = PasswordField('Password', validators=[Required()])
  submit = SubmitField('Log in')
