#!/usr/bin/python3
"""
Module changes name of a State obj from db
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

    ch_obj = sess.query(State).filter_by(id=2).first()
    ch_obj.name = 'New Mexico'
    sess.commit()
