import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Migration(Base):

    __tablename__ = "migrations"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    migrated_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "<Migration(name={0})>".format(self.name)