#!/usr/bin/python3
"""
Module creates State "California" with City "San Francisco" in db
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    sess = Session()
    put_State = State(name='California')
    put_City = City(name='San Francisco')
    put_State.cities.append(put_City)

    sess.add(put_State)
    sess.add(put_City)

    sess.commit()
