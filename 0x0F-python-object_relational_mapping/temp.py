#!/usr/bin/python3

import MySQLdb
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                   .format(sys.argv[1], sys.argv[2], sys.argv[3]))
Base.metadata.create_all()

Session = sessionmaker(bind=db)
session= Session()

data = session.query(State).all()
for d in data:
    print(d)




# if __name__ == "__main__":
#     con = MySQLdb.connect(host="localhost",
#                           port=3306,
#                           user=sys.argv[1],
#                           passwd=sys.argv[2],
#                           db=sys.argv[3])
#     command = "SELECT cities.name from cities inner join states where states.id = cities.state_id and states.name = %s order by cities.id ASC"
#     cursor = con.cursor()
#     cursor.execute(command, (sys.argv[4],))
#     rows = cursor.fetchall()
#     l = len(rows)
#     for r in rows:
#         print(r[0], end="")
#         print(", " if l > 1 else "", end="")
#         l -=1
#     print()
#     con.close()
