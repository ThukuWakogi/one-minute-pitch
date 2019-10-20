from flask import Flask
from flask_scss import Scss
from config import config_options
from flask_sqlalchemy import SQLAlchemy
import sass

db = SQLAlchemy()

def create_app(config_name):
  app = Flask(__name__)

  # create app configurations
  app.config.from_object(config_options[config_name])

  # register blueprints
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  # TODO: auth blueprint registration

  # initialize app extensions
  sass.compile(dirname=(f'{app.root_path}\\static\\sass', f'{app.root_path}\\static\\css'), output_style='compressed')
  db.init_app(app)

  return app
