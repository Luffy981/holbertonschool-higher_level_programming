#!/usr/bin/python3
"""
Start database
"""

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    """
    Conect and quering database
    """
    sql = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(sql.format(argv[1],
                                      argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    save = ""
    for s, c in session.query(State, City).\
            order_by(State.id, City.id).\
            filter(City.state_id == State.id).all():
        if s.name != save:
            print("{}: {}".format(s.id, s.name))
            save = s.name
        print(" {}: {}".format(c.id, c.name))
        save = s.name
    session.close()
