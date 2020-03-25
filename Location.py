from app import db
import City

class Location(db.Model):

  __tablename__ = 'Locations'

  id = db.Column(db.Integer, primary_key=True)
  latitude = db.Column(db.Real, nullable=False)
  longitude = db.Column(db.Real, nullable=False)
  address = db.Column(db.String())
  number = db.Column(Integer)
  district = db.Column(db.String())
  zipcode = db.Column(db.String())

  city = relationship('City')

  def __init__(self, latitude, longitude, address, number, district, zipcode):
    self.latitude = latitude
    self.longitude = longitude
    self.address = address
    self.number = number
    self.district = district
    self.zipcode = zipcode
