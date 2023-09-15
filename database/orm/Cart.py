from sqlalchemy import Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cart(Base):
    __tablename__ = "cart"
    id = Column("id", Integer, primary_key=True)
    at1 = Column("at1", String)

    def __init__(self, id, at1):
        self.id = id
        self.at1 = at1
