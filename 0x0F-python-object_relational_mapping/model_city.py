#!/usr/bin/python3
"""Docstring goes here
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base
from model_state import State


class City(Base):
    """Docstring goes here"""
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
