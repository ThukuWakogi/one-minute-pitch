from flask import render_template, request, flash, redirect, url_for
from . import main
from ..models import PitchCategory, Pitch, User, PitchComment
from .. import db
from flask_login import login_required, current_user
from .forms import PitchForm, PitchCommentForm

@main.route('/')
def index():
  '''
  view root page functions that returns the index page and its data
  '''

  pitch_categories = PitchCategory.query.all()

  if len(pitch_categories) == 0:
    db.session.add_all([
      PitchCategory(category='Pickup lines'),
      PitchCategory(category='Interview pitch'),
      PitchCategory(category='Product pitch'),
      PitchCategory(category='Promotion pitch')
    ])
    db.session.commit()
    pitch_categories == PitchCategory.query.all()

  return render_template(
    'index.html',
    number_of_pitch_categories=len(pitch_categories),
    pitch_categories=pitch_categories
  )

@main.route('/pitches/<int:pitch_category_id>')
def load_pitch_by_category(pitch_category_id):
  '''
  fetches pitches by category from database and loads pitches-by-category.html

  Args:
    pitch_category_id: url parameter for fetching pitches
  '''

  pitch_category =  PitchCategory.query.filter_by(id=pitch_category_id).first()
  pitches = Pitch.query.filter_by(category_id=pitch_category_id).all()

  return render_template('pitches-by-category.html', pitch_category=pitch_category, pitches=pitches, number_of_pitches=len(pitches))

@main.route('/pitchform/<action>/<category_id>', defaults={ 'pitch_id': None })
@main.route('/pitchform/<action>/<category_id>/<int:pitch_id>')
@login_required
def load_pitchform(action, category_id, pitch_id):
  '''
  loads pitch form for adding or editing
  '''

  pitch_categories = PitchCategory.query.all()
  form = PitchForm()

  return render_template('pitch-form.html', form=form, pitch_categories=pitch_categories, category_id=category_id)

@main.route('/pitchform/<action>/<category_id>', defaults={ 'pitch_id': None }, methods=['POST'])
@main.route('/pitchform/<action>/<category_id>/<int:pitch_id>', methods=['POST'])
@login_required
def pitchform_load(action, category_id, pitch_id):
  '''
  gets form data and pushed it to database
  '''
  
  pitch_categories = PitchCategory.query.all()
  form = PitchForm()

  title = request.form.get('title')
  body = request.form.get('body')
  category = request.form.get('category')
  
  try:
    int(category)
  except ValueError:
    flash('category is required too!')

    return render_template('pitch-form.html', form=form, pitch_categories=pitch_categories)
    
  new_pitch = Pitch(title=title, body=body, category_id=category, user_id=current_user.id)
  db.session.add(new_pitch)
  db.session.commit()

  pitch_category =  PitchCategory.query.filter_by(id=category).first()
  pitches = Pitch.query.filter_by(category_id=category).all()

  return render_template('pitches-by-category.html', pitch_category=pitch_category, pitches=pitches, number_of_pitches=len(pitches))

@main.route('/pitch/<int:pitch_id>')
def load_pitch(pitch_id):
  '''
  gets pitch and displays it to pitch.html
  '''

  form = PitchCommentForm()
  pitch = Pitch.query.filter_by(id=pitch_id).first()
  pitch_category = PitchCategory.query.filter_by(id=pitch.category_id).first()
  pitch_owner = User.query.filter_by(id=pitch.user_id).first()
  pitch_comments = PitchComment.query.filter_by(pitch_id=pitch_id).all()
  users = User.query.all()
  comments_and_users = []
  
  for comment in pitch_comments:
    comments_and_users.append({
      'comment': comment,
      'user': get_user(comment.user_id, users)
    })
  
  print('*' * 111)

  return render_template(
    'pitch.html',
    form=form,
    pitch=pitch,
    pitch_category=pitch_category,
    pitch_owner=pitch_owner,
    number_of_pitch_comments=len(pitch_comments),
    comments_and_users=comments_and_users
  )

@main.route('/comment/<int:pitch_id>', methods=['POST'])
@login_required
def post_comment(pitch_id):
  '''
  takes comment and posts it to database
  '''

  comment = request.form.get('comment')

  new_comment = PitchComment(pitch_id=pitch_id, user_id=current_user.id, comment=comment)
  db.session.add(new_comment)
  db.session.commit()

  return redirect(url_for('main.load_pitch', pitch_id=pitch_id))

def get_user(_id, users):
  user_to_return = None

  for user in users:
    if user.id == _id:
      user_to_return = user
  
  return user_to_return
