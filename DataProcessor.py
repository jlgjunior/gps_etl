import googlemaps
import multiprocessing as mp
from Location import Location
from State import State
from Country import Country

class DataProcessor:

  def __init__(self, dataPoints):
    self._dataPoints = dataPoints
    self._gmaps = googlemaps.Client(key='AIzaSyD824zYRjcgNrFW0XO5TzwCUkKDfWmAneo')
   
  def processDataPoints(self):
    resultSet = []
    pool = mp.Pool(mp.cpu_count())
    resultSet =  pool.starmap(self.processSingleDataPoint, [(point[0], point[1]) for point in self._dataPoints])
    pool.close()
   
    return resultSet

  def processSingleDataPoint(self, latitude, longitude):
    location = Location(latitude, longitude)
    try:
      data = self._gmaps.reverse_geocode((location.latitude, location.longitude))
      for addressItem in data[0]['address_components']:
        if 'street_number' in addressItem['types']:
          location.number = addressItem['long_name']
        elif 'sublocality_level_1' in addressItem['types']:
          location.district = addressItem['long_name']
        elif 'administrative_area_level_2' in addressItem['types']:
          location.city = addressItem['long_name']
        elif 'country' in addressItem['types']:
          country = Country(addressItem['long_name'])
        elif 'administrative_area_level_1' in addressItem['types']:
          state = State(addressItem['long_name'], addressItem['short_name'])
        elif 'postal_code' in addressItem['types']:
          location.zipcode = addressItem['long_name']
        elif 'route' in addressItem['types']:
          location.address = addressItem['long_name']
      state.country = country
      location.state = state
      return location
    except Exception as e:
      print(e)
      return []
