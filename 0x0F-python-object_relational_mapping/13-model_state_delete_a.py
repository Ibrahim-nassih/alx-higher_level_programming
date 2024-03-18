#!/usr/bin/python3
"""
This script removes from the database hbtn_0e_6_usa all State objects whose names begin with the letter "a."
"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(State.name.like('%a%')):
        session.delete(state)

    session.commit()
