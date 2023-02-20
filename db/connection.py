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
    '''
        Stores id of messages and deals from satu.kz
    '''
    __tablename__ = 'writen'
    id = Column(Integer, primary_key=True)


class PhoneNumbers(Base):
    '''
        Stores id and phone numbers of bitrix DB
        (Maby better would be just searching the phone number in bitrix DB. I think i'm gonna cahnge this later)
    '''
    __tablename__ = 'phone'
    id = Column(Integer, primary_key=True)
    number = Column(String)


Base.metadata.create_all(engine)

session = Session(engine)

