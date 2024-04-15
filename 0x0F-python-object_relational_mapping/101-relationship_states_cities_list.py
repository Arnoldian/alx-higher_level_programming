#!/usr/bin/python3
"""
Module lists all State objects with corresponding City objects
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sess = Session()
    
    for obj in sess.query(State).order_by(State.id):
        print(obj.id, obj.name, sep=": ")

        for city_table in obj.cities:
            print("    ", end="")
            print(city_table.id, city_table.name, sep=": ")
