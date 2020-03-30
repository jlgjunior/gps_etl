from app import db
from GenericModel import GenericModel

class Country(GenericModel):

  __tablename__ = 'countries'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(), nullable=False, unique=True)

  states = db.relationship('State', backref='country', cascade='save-update')

  def __init__(self, name):
    self.name = name

  def addNew(self):
    super().addNew()

  def retrieveModel(self):
    model = db.session.query(Country).filter(Country.name==self.name).one_or_none() 
    if model is None:
      return False
    else:
      self.id = model.id
      return True

  def __repr__(self):
    return self.name
