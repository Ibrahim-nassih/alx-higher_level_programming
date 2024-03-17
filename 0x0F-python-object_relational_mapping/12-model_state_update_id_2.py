#!/usr/bin/python3
"""
The name of a State object from the database hbtn_0e_6_usa is modified by this script.
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

    for state in session.query(State).filter(State.id == 2):
        state.name = 'New Mexico'
        session.commit()
