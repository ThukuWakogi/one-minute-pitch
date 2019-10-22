from flask import render_template
from . import main
from ..models import PitchCategory, Pitch
from .. import db

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

  return render_template('index.html', number_of_pitch_categories=len(pitch_categories), pitch_categories=pitch_categories)

@main.route('/pitches/<int:pitch_category_id>')
def load_pitch_by_category(pitch_category_id):
  '''
  fetches pitches by category from database and loads pitches-by-category.html
  '''

  pitch_category =  PitchCategory.query.filter_by(id=pitch_category_id).first()
  pitches = Pitch.query.filter_by(category_id=pitch_category_id).all()

  return render_template('pitches-by-category.html', pitch_category=pitch_category, pitches=pitches)
