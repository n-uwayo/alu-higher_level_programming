#!/usr/bin/python3
"""
This script takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

# The code will not be executed when imported
if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

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
                LIKE BINARY '{}' ORDER BY id ASC".format(state_name))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    # process of clean up
    cur.close()

    db.close()
