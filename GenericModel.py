from app import db
from abc import abstractmethod

class GenericModel(db.Model):
  __abstract__ = True

  @abstractmethod
  def retrieveModel(self):
    raise NotImplementedError("retrieveModel")

  def addNew(self):
    retrieved = self.retrieveModel()
    if not retrieved:
      try:
        with db.session.no_autoflush:
          db.session.merge(self)
          db.session.commit()
      except Exception as e:
       db.session.rollback()
       print(e)
    
