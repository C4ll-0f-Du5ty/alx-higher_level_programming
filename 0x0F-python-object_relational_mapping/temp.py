#!/usr/bin/python3

import MySQLdb
import sys
if __name__ == "__main__":
    con = MySQLdb.connect(host="localhost",
                          port=3306,
                          user=sys.argv[1],
                          passwd=sys.argv[2],
                          db=sys.argv[3])
    command = "SELECT * FROM states WHERE name = %s order by id ASC"
    cursor = con.cursor()
    cursor.execute(command, (sys.argv[4], ))
    rows = cursor.fetchall()
    for r in rows:
        print(r)
    con.close()
