import os
from os import listdir

class DataReader():

  def __init__(self, coordinateFilesPath):
    self._coordinateFilesPath = coordinateFilesPath

  def readCoordinates(self):
    coordinates = []
    for fileName in listdir(self._coordinateFilesPath):
      file = open(os.path.join(self._coordinateFilesPath, fileName))
      for line in file: 
        value = line.strip().split(' ')[4]
        if line.startswith('La'):
          coordinate = (float(value), 0)
        elif line.startswith('Lo'):
          coordinate = (coordinate[0], float(value))
          coordinates.append(coordinate)
    return coordinates
      
