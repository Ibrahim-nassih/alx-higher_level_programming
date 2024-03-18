#!/usr/bin/python3
"""
The class definition of a State and an instance are contained in this module. Declarative_base() is Base.
"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from relationship_city import Base


class State(Base):
    """establishes a state table"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
