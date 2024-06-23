#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City, Base
from relationship_state import State

# def main(username, password, dbname):
if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    # Create the tables if they don't exist
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Add a new state
    california = State(name="California")

    # Add a new city linked to the state
    # san_francisco = City(name="San Francisco", state_id=california.id)
    san_francisco = City(name="San Francisco")
    california.cities.append(san_francisco)

    session.add(california)
    session.add(san_francisco)

    session.commit()

    # print("State and City added successfully.")
    # except Exception as e:
    #     print(f"An error occurred: {e}")

    session.close()
    # if len(sys.argv) != 4:
    #     print("Usage: python 100-relationship_states_cities.py "
    #           "<mysql_username> <mysql_password> <database_name>")
    # else:
    # main(sys.argv[1], sys.argv[2], sys.argv[3])
