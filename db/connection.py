from sqlalchemy import (create_engine,
                        Integer,
                        Column,
                        String,
                        )
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

engine = create_engine('sqlite:///writen.sqlite3')

Base = declarative_base()


class Orders(Base):
    __tablename__ = 'writen'
    id = Column(Integer, primary_key=True)


class PhoneNumbers(Base):
    __tablename__ = 'phone'
    id = Column(Integer, primary_key=True)
    number = Column(String)


Base.metadata.create_all(engine)

session = Session(engine)

