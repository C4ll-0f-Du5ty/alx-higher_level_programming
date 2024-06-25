#!/usr/bin/python3

import MySQLdb
import sys
if __name__ == "__main__":
    con = MySQLdb.connect(host="localhost",
                          port=3306,
                          user=sys.argv[1],
                          passwd=sys.argv[2],
                          db=sys.argv[3])
    command = "SELECT cities.name from cities inner join states where states.id = cities.state_id and states.name = %s order by cities.id ASC"
    cursor = con.cursor()
    cursor.execute(command, (sys.argv[4],))
    rows = cursor.fetchall()
    for r in rows:
        print(r)
    con.close()
