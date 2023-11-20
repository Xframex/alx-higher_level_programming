#!/usr/bin/python3
"""create a class state
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """build a constructor"""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
