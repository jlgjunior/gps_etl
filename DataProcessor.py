from Location import Location

class DataProcessor:

  def __init__(self, dataPoints):
    self._dataPoints = dataPoints

  def processDataPoints(self):
    resultSet = []
    location = Location(self._dataPoints[0][0], self._dataPoints[0][1])
    location.getLocationData()
    return resultSet
