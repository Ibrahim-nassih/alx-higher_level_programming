#!/usr/bin/python3
"""
All City objects from the database hbtn_0e_101_usa are scanned by this script.
"""
from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import create_engine
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for city in session.query(City).order_by(City.id):
        print(f"{city.id}: {city.name} -> {city.state.name}")
