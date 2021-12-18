#!/usr/bin/python3

"""
Models State inherits from base
"""

from relationship_city import City
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String 

Base = declarative_base()


class State(Base):
    """
    Class inherits from base
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City')