#!/usr/bin/python3
"""
Module adds State obj "Louisiana to db
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
    new_state = State(name='Louisiana')
    sess.add(new_state)
    new_obj = sess.query(State).filter_by(name='Louisiana').first()
    print(new_obj.id)
    sess.commit()
