from app import db
import googlemaps
import City

class Location(db.Model):

  __tablename__ = 'Locations'
  __table_args__ = (db.UniqueConstraint('latitude', 'longitude', name='_latitude_longitude_uc'), {})

  id = db.Column(db.Integer, primary_key=True)
  latitude = db.Column(db.Float, nullable=False)
  longitude = db.Column(db.Float, nullable=False)
  address = db.Column(db.String(), nullable=False)
  number = db.Column(db.Integer)
  district = db.Column(db.String(), nullable=False)
  zipcode = db.Column(db.String(), nullable=False)
  city_id = db.Column(db.Integer, db.ForeignKey('Cities.id'), nullable=False)
   

  city = db.relationship('City')

  def __init__(self, latitude, longitude):#, address, number, district, zipcode):
    self._gmaps = googlemaps.Client(key='AIzaSyD824zYRjcgNrFW0XO5TzwCUkKDfWmAneo')
   
    self.latitude = latitude
    self.longitude = longitude
    #self.address = address
    #self.number = number
    #self.district = district
    #self.zipcode = zipcode

  def getLocationData(self):
    data = self._gmaps.reverse_geocode((self.latitude, self.longitude))
    print(data)
