from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.dialects import postgresql
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(UserMixin, db.Model):
  '''
  maps to users table in database

  Args:
    db.Model: class from which sqlAlchemy properties are inherited
  '''

  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), index=True, nullable=False)
  email  = db.Column(db.String(255), index=True, nullable=False)
  password_secure = db.Column(db.String(255), nullable=False)
  votes = db.relationship('PitchVote', backref='pitch_votes', lazy='dynamic')
  comments = db.relationship('PitchComment', backref='pitch_comments', lazy='dynamic')
  
  def __repr__(self):
    return f'User{self.password_secure}'

class PitchCategory(db.Model):
  '''
  map to pitch_categories table in database

  Args:
    db.Model: class from which sqlAlchemy properties are inherited
  '''
  __tablename__ = 'pitch_categories'
  id = db.Column(db.Integer, primary_key=True)
  category = db.Column(db.String(255), nullable=False)
  pitches = db.relationship('Pitch', backref='pitch_collection', lazy='dynamic')

class Pitch(db.Model):
  '''
  maps to  pitch_collection table in database

  Args:
    db.Model: class from which sqlAlchemy properties are inherited
  '''

  __tablename__ = 'pitch_collection'
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(255), nullable=False)
  body = db.Column(db.String(), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  category_id = db.Column(db.Integer, db.ForeignKey('pitch_categories.id'), nullable=False)

  def is_body_more_than_150(self):
    return len(self.body) >= 150 if self.body is not None else False

class PitchVote(db.Model):
  '''
  maps to pitch_votes table in database

  Args:
    db.Model: class from which sqlAlchemy properties are inherited
  '''

  __tablename__ = 'pitch_votes'
  id = db.Column(db.Integer, primary_key=True)
  pitch_id = db.Column(db.Integer, db.ForeignKey('pitch_collection.id'), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  vote_type = db.Column(postgresql.ENUM('upvote', 'downvote', name='vote_type', create_type='false'), nullable=False)

class PitchComment(db.Model):
  '''
  maps to pitch_comments table in database

  Args:
    db.Model: class from which sqlAlchemy properties are inherited
  '''

  __tablename__ = 'pitch_comments'
  id = db.Column(db.Integer, primary_key=True)
  pitch_id = db.Column(db.Integer, db.ForeignKey('pitch_collection.id'), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  comment = db.Column(db.String(), nullable=False)
