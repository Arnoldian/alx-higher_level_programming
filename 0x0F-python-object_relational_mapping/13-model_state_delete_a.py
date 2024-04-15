#!/usr/bin/python3
"""
Module deletes all State objects with letter a in name from db
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    sess = Session()
    for obj in sess.query(State).filter(State.name.like('%a%')):
        sess.delete(obj)
    sess.commit()
