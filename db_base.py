from sqlalchemy import (create_engine,
                        Integer,
                        Column,
                        )
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

engine = create_engine('sqlite:///orders.sqlite3')

Base = declarative_base()

class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer,primary_key=True)
    
Base.metadata.create_all(engine)

session = Session(engine)

def add_to_db(id):
    try:
        stmt = session.query(Orders).filter(Orders.id == id).one()
        stmt = False
    except NoResultFound:
        new = Orders(id=id)
        session.add(new)
        session.commit()
        stmt = True     

    return print(stmt)

def check_sttm_db(id):
    try:
        stmt = session.query(Orders).filter(Orders.id == id).one().id
        stmt  = False
    except NoResultFound:
        stmt = True

    return stmt
