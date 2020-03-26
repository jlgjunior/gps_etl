from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from os import listdir
import os
from DataReader import DataReader
from DataProcessor import DataProcessor

def main():
  engine = create_engine("postgresql://application:application@localhost/gps_etl_dev")
  session = sessionmaker(bind=engine)

  reader = DataReader('dataSrc')

  data = reader.readCoordinates()
  
  processor = DataProcessor(data)
  processor.processDataPoints()

if __name__ == "__main__":
  main() 
