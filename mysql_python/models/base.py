import sqlalchemy.orm import declarative_base
from main import session

Model = declarative_base()
Model.query = session.query_property()

class TimeStampModel(Model):
    __abstract__ = True
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, onupdate=datetime.utcnow())
