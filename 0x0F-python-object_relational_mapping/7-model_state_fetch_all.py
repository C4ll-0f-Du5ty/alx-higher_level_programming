#!/usr/bin/python3
"""Listing All objects of a given DB"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(engine)
    Base.metadata.create_all(engine)
    session = Session()

    results = session.query(State).order_by(State.id).all()

    for r in results:
        print("{}: {}".format(r.id, r.name))
    session.close()
