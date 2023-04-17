#!/usr/bin/python3
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
import sys

"""
    Module that performs MySQL query through MySQLAlchemy.
"""

if __name__ == "__main__":
    # Set up the database URI from the command line arguments.
    db_uri = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
                                                            sys.argv[1],
                                                            sys.argv[2],
                                                            sys.argv[3])

    # Create the database engine.
    engine = create_engine(db_uri, pool_pre_ping=True)

    # Create the tables in the database if they don't exist.
    Base.metadata.create_all(engine)

    # Create a sessionmaker object and bind it to the database engine.
    Session = sessionmaker(bind=engine)

    # Create a session object.
    session = Session()

    # Query the database for all cities, ordered by ID, and print out the
    # city's ID, name, and the name of the state it's in.
    for a_city in session.query(City).order_by(City.id):
            print("{}: {} -> {}".format(a_city.id, a_city.name,
                  a_city.state.name))

    # Close the session.
    session.close()
