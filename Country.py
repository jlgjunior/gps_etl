from app import db

class Country(db.Model):

  __tablename__ = 'Countries'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False, unique=True)

  def __init__(self, name):
    self.name = name
