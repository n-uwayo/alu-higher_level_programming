#!/usr/bin/python3
"""
Script that changes the name of a
State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # Get the command-line arguments for username, password, and database name
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create an engine that connects to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, db_name))

    # Create a session factory bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a session object
    session = Session()

    # Query the database for the state with id = 2
    state = session.query(State).filter_by(id=2).first()

    # Update the state name
    state.name = "New Mexico"

    # Commit the transaction
    session.commit()

    # Close the session
    session.close()
