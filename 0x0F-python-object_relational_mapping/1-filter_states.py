#!/usr/bin/python3
"""List the data Tables with specific Value Patterns"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], host='localhost')

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    db.close()
