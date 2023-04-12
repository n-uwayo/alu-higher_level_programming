#!/usr/bin/python3
"""
Script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches
the argument (safe from MySQL injection)
"""

import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == "__main__":
    # connect to MySQL database
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3],
                         host="localhost", port=3306)

    # create a cursor object to execute queries
    cursor = db.cursor()

    # execute a parameterized query to search for the state name
    cursor.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC",
                   (argv[4],))

    # fetch all rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # close cursor and database
    cursor.close()
    db.close()
