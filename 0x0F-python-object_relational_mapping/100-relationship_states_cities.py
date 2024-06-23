#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City, Base
from relationship_state import State


def main(username, password, dbname):
    engine = create_engine(f'mysql+pymysql://\
        {username}:{password}@localhost:3306/{dbname}')
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Create the tables if they don't exist
        Base.metadata.create_all(engine)

        # Add a new state
        california = State(name="California")
        session.add(california)
        session.commit()

        # Add a new city linked to the state
        san_francisco = City(name="San Francisco", state_id=california.id)
        session.add(san_francisco)
        session.commit()

        print("State and City added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python 100-relationship_states_cities.py "
              "<mysql_username> <mysql_password> <database_name>")
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
