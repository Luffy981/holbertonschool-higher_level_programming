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
    list = session.query(State).join(City).order_by(State.id, City.id).\
        filter(City.state_id == State.id).all()
    for a in list:
        print("{}: {}".format(a.id, a.name))
        for j in a.cities:
            print("    {}: {}".format(j.id, j.name))
    session.close()
