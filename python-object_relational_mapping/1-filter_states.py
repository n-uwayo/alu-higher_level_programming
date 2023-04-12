#!/usr/bin/python3
"""
This script lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Get the command-line arguments for username, password, and database name
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor object to execute SQL statements
    cur = db.cursor()

    # execute a parameterized query to search for the state name
    cur.execute("SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY id ASC")

    # Fetch all rows returned by the SELECT statement
    rows = cur.fetchall()

    # Print each row to the console
    for row in rows:
        print(row)

    # Clean up resources
    cur.close()
    db.close()
