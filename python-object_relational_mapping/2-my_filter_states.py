#!/usr/bin/python3
"""
This script takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Get the command-line arguments
    # for username, password, database name, and state name
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

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

    # Execute a SELECT statement to retrieve all
    # rows where the name matches the state name argument
    cur.execute("SELECT * FROM states WHERE name
                LIKE BINARY '{}' ORDER BY id ASC".format(state_name))

    # Fetch all rows returned by the SELECT statement
    rows = cur.fetchall()

    # Print each row to the console
    for row in rows:
        print(row)

    # Clean up resources
    cur.close()
    db.close()
