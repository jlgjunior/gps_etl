from app import db
import City

class Location(db.Model):

  __tablename__ = 'Locations'
  __table_args__ = (db.UniqueConstraint('latitude', 'longitude', name='_latitude_longitude_uc'), {})

  id = db.Column(db.Integer, primary_key=True)
  latitude = db.Column(db.Float, nullable=False)
  longitude = db.Column(db.Float, nullable=False)
  address = db.Column(db.String(), nullable=False)
  number = db.Column(db.String())
  district = db.Column(db.String(), nullable=False)
  zipcode = db.Column(db.String(), nullable=False)
  city_id = db.Column(db.Integer, db.ForeignKey('Cities.id'), nullable=True)
  state_id = db.Column(db.Integer, db.ForeignKey('States.id'), nullable=False) 

  city = db.relationship('City')
  state = db.relationship('State')

  def __init__(self, latitude, longitude):
  
    self.latitude = latitude
    self.longitude = longitude
