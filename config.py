import os

class Config:
  '''
  general configurations parent class
  '''

  SECRET_KEY = os.environ.get('SECRET_KEY')
  UPLOADED_PHOTOS_DEST = 'app.static/photos'
  MAIL_SERVER = 'stmp.gmail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
  MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
  SIMPLE_JS_IIFE = True
  SIMPLE_USE_CDN = True

class ProdConfig(Config):
  '''
  production configuration child class

  args:
    config: parent configuration class with general configuration settings
  '''

  SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

class TestConfig(Config):
  '''
  test configuration child class

  args:
    config: parent configuration class with general configuration settings
  '''

  SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')

class DevConfig(Config):
  '''
  development configuration child class

  args:
    config: parent configuration class with general configuration settings
  '''

  SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

  DEBUG =  True

config_options = {
  'development': DevConfig,
  'production': ProdConfig,
  'test': TestConfig
}
