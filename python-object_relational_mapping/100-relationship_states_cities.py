#!/usr/bin/python3
"""adds the State object “California”
with the City “San Francisco”
to the database hbtn_0e_100_usa"""

if __name__ == "__main__":

    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.schema import Table

    # Create the engine and connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                           sys.argv[3]), pool_pre_ping=True)
    # Create all tables in the engine
    Base.metadata.create_all(engine)

    session = Session(engine)
   # Create a new City object with name "San Francisco"
   new_city = City(name='San Francisco')
   # Create a new State object with name "California"
    new = State(name='California')
    # Add the new City object to the new State object's cities list
    new.cities.append(new_city)
    # Add the new State and City objects to the session
    session.add_all([new, new_city])
    # Commit the changes to the database
    session.commit()
    # Close the session
    session.close()
