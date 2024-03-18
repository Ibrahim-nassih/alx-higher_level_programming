#!/usr/bin/python3
"""
The class definition of a State and an instance are contained in this module. Declarative_base() is Base.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class State(Base):
    """
    Creates user table
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
