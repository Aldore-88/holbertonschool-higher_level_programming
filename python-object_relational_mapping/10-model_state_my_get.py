#!/usr/bin/python3
"""10.Get state"""
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

    """searches state for the input name"""
    state_search = sys.argv[4]
    state = session.query(State).order_by(State.id).filter(
        State.name == state_search).first()
    if state is None:
        print("Not found")
    else:
        print(state.id)

    """close session"""
    session.close()
