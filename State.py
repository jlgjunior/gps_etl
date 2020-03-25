from app import db
import Country

class State(db.Model):
  __tablename__ = 'States'

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(), nullable=False, unique=True)
  abbreviation = db.Column(db.String(2))
  country_id = db.Column(db.Integer, db.ForeignKey('Countries.id'), nullable=False)

  country = db.relationship('Country')

  def __init__(self, name, abbreviation):
    self.name = name
    self.abbreviation = abbrevtiation

  def __repr__(self):
    return self.abbreviation

