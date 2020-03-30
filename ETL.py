from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from os import listdir
from app import db
import os
from DataReader import DataReader
from DataProcessor import DataProcessor

def main():
  reader = DataReader('dataSrc')

  data = reader.readCoordinates()
  
  processor = DataProcessor(data)
  locations = processor.processDataPoints()
  try:
    for location in locations:
      location.state.country.addNew()
      location.state.country_id = location.state.country.id
      #location.state.country = None
      location.state.addNew()
      location.state_id = location.state.id
      #location.state = None
      location.addNew()
  except Exception as e:
    print(e)


if __name__ == "__main__":
  main() 
