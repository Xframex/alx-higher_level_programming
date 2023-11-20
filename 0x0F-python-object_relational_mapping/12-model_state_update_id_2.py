#!/usr/bin/python3
"""Docstring goes here
"""

from sqlalchemy import create_engine
from sqlalchemy import MetaData
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    session = Session()
    state_to_update = session.query(State).filter(State.id == 2).first()
    state_to_update.name = "New Mexico"
    session.commit()
    session.close()
