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
    results = session.query(State).filter(State.name == sys.argv[4]).all()
    if results == []:
        print("Not found")
    else:
        for i in results:
            print(i.id)
    session.close()
