from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from sassutils.wsgi import SassMiddleware

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
  app.wsgi_app = SassMiddleware(app.wsgi_app, {
    'app': ('static/sass', 'static/css', '/static/css')
  })
  db.init_app(app)

  return app
