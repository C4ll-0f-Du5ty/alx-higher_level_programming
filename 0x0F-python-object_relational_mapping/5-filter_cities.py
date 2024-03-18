#!/usr/bin/python3
"""Listing specific data on a specific condition"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')\
                    FROM cities INNER JOIN states ON \
                    states.id = cities.state_id \
                    WHERE states.name = %s", (sys.argv[4], ))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    db.close()
