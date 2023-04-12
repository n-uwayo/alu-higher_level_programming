#!/usr/bin/python3
"""
This script lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

# The code will not be executed when imported
if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # It gives us the ability to have multiple seperate working environments
    # through the same connection to the database.
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    # procss of clean up
    cur.close()

    db.close()
