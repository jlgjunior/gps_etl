from app import db
from GenericModel import GenericModel
import State

class Location(GenericModel):

  __tablename__ = 'locations'
  __table_args__ = (db.UniqueConstraint('latitude', 'longitude', name='_latitude_longitude_uc'), {})

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  latitude = db.Column(db.Float, nullable=False)
  longitude = db.Column(db.Float, nullable=False)
  address = db.Column(db.String())
  number = db.Column(db.String())
  district = db.Column(db.String())
  zipcode = db.Column(db.String())
  city = db.Column(db.String())
  state_id = db.Column(db.Integer, db.ForeignKey('states.id'), nullable=False) 


  def __init__(self, latitude, longitude):
    self.latitude = latitude
    self.longitude = longitude

  def addNew(self):
    super().addNew()

  def retrieveModel(self):
    model = db.session.query(Location).filter(Location.latitude==self.latitude, Location.longitude==self.longitude).one_or_none()
    if model is None:
      return False
    else:
      self.id = model.id
      return True
