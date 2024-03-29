#!/usr/bin/python3
"""Call Specific Value"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cursor = db.cursor()
    cursor.execute("select * from states where name like binary %s\
                   ORDER BY id ASC", (sys.argv[4],))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    db.close()
