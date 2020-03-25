from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config
import os

app = Flask(__name__)
app.config.from_object(config.StagingConfig)
app.config['SQL_ALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

if __name__ == '__main__':
  app.run()
