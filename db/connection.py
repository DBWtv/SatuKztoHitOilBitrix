from sqlalchemy import (create_engine,
                        Integer,
                        Column,
                        )
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


engine = create_engine('sqlite:///writen.sqlite3')

Base = declarative_base()


class Orders(Base):
    '''
        Stores id of messages and deals from satu.kz
    '''
    __tablename__ = 'writen'
    id = Column(Integer, primary_key=True)


Base.metadata.create_all(engine)

session = Session(engine)
