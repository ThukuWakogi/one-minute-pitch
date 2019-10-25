from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, TextAreaField, HiddenField
from wtforms.validators import Required, Email, EqualTo
from ..models import User

class PitchForm(FlaskForm):
  title = StringField('Enter pitch title', validators=[Required()])
  body = TextAreaField('Pitch goes here...', validators=[Required()])
  category = HiddenField('Choose category', validators=[Required()])
  submit = SubmitField('add pitch')
