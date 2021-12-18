#!/usr/bin/python3
"""
Models State inherits from base
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """
    Class inherits from base
    """
    __tablename__ = 'states'
    id = Column(Integer(11), primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
