from sqlalchemy import Column, Integer, String
from sqlalchemy import JSON
from src.data import Base

class PokeDB(Base):
    __tablename__ = "pokemon"
    name = Column(String, index=True)
    id = Column(Integer, primary_key=True, index=True)
    height = Column(Integer)
    weight = Column(Integer)
    types = Column(JSON)
    sprites = Column(JSON)
