#!/usr/bin/python3
"""Listing specific data"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(engine)
    session = Session()
    Results = session.query(State).order_by(State.id).first()
    if Results is None:
        print("Nothing")
    else:
        print(f"{Results.id}: {Results.name}")
    session.close()
