#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)  # database connection creator
from sqlalchemy.orm import sessionmaker  # session factory creator
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    """creates tables if it doesnt exist from Base"""
    Base.metadata.create_all(engine)
    """creates session factory"""
    """not a session itself"""
    Session = sessionmaker(bind=engine)
    """creates actual session?? why??"""
    session = Session()
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    """close session"""
    session.close()
