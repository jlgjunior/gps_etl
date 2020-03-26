from app import db
import State

class City(db.Model):
  __tablename__ = 'Cities'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False, unique=True)
  state_id = db.Column(db.Integer, db.ForeignKey('States.id'), nullable=False)

  state = db.relationship('State')

  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return self.name
