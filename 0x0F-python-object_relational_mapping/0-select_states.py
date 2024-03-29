#!/usr/bin/python3
"""A script to list the Data from a given Database Using A given user"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cursor = db.cursor()
    cursor.execute("select * from states order by id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    db.close()
