#!/usr/bin/python3
"""first state fetching
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

    states = session.query(State).order_by(State.id)
    if states.first():
        first_one = states[0]
        print("{}: {}".format(first_one.id, first_one.name))
    else:
        print("Nothing")
    session.close()
