#!/usr/bin/python3
"""Printing the data of a given NAME"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(engine)
    Base.metadata.create_all(engine)
    session = Session()
    newState = State(name="Louisiana")
    session.add(newState)
    session.commit()
    results = session.query(State).filter(State.name == newState.name).all()
    for i in results:
        print(i.id)
    session.close()
