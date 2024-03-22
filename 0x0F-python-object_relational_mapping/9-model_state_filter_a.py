#!/usr/bin/python3
"""Printing the Data with Specific Letter"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    results = session.query(State).filter(State.name.ilike("%a%"))\
                     .order_by(State.id).all()
    for i in results:
        print(f"{i.id}: {i.name}")
    session.close()
