#!/usr/bin/python3
"""Manipulating between 2 Tables"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(engine)
    Base.metadata.create_all(engine)
    session = Session()
    results = session.query(State, City)\
                     .filter(State.id == City.state_id)\
                     .order_by(City.id.asc())
    for r in results:
        print(f"{r.State.name}: ({r.City.id}) {r.City.name}")
    session.close()
