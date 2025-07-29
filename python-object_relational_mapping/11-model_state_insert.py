#!/usr/bin/python3
"""12.Update a state"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)  # database connection creator
from sqlalchemy.orm import sessionmaker  # session factory creator
from sqlalchemy import (create_engine, update)


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

    """update state of id:2"""
    state = session.query(State).filter(State.id == 2)
    state.update({State.name: "New Mexico"})
    """need to commit changes"""
    session.commit()

    """close session"""
    session.close()
