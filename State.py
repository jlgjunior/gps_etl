from app import db
from GenericModel import GenericModel
import Country
import State

class State(GenericModel):
  __tablename__ = 'states'

  id = db.Column(db.Integer, primary_key = True, autoincrement=True)
  name = db.Column(db.String(), nullable=False, unique=True)
  abbreviation = db.Column(db.String(2), nullable=False, unique=True)
  country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)

  locations = db.relationship('Location', backref = 'state', cascade='save-update')

  def __init__(self, name, abbreviation):
    self.name = name
    self.abbreviation = abbreviation

  def addNew(self):
    super().addNew()

  def retrieveModel(self):
    model =  db.session.query(State).filter(State.abbreviation==self.abbreviation).one_or_none()
    if model is None:
      return False
    else:
      self.id = model.id
      return True

  def __repr__(self):
    return self.abbreviation
