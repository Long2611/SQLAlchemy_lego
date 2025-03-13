from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from typing import List, Dict, Any

Base = declarative_base()

class LegoSet(Base):
    __tablename__ = 'lego_sets'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    year = Column(Integer)
    num_parts = Column(Integer)

