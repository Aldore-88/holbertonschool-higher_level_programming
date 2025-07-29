#!/usr/bin/python3
"""11.Add a new state"""
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

    """adding Louisiana"""
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)

    """close session"""
    session.close()
