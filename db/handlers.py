from .connection import session, Orders, NoResultFound, PhoneNumbers
from datetime import datetime

def add_to_db(id):
    '''
        Searching satu.kz order id in PJ DB. If not existt - wright it to DB
    '''
    try:
        stmt = session.query(Orders).filter(Orders.id == id).one()
        stmt = False
    except NoResultFound:
        new = Orders(id=id)
        session.add(new)
        session.commit()
        stmt = True     
        with open('log', 'r+') as log:
                    log.seek(0, 2)
                    log.write(f'{datetime.now()}  {new} write to DB \n')
    return stmt

def check_sttm_db(id):
    '''
        Check that we got new order wich is not in PJ DB
    '''
    try:
        stmt = session.query(Orders).filter(Orders.id == id).one().id
        stmt  = False
    except NoResultFound:
        stmt = True

    return stmt

    '''Some mess up there gonna fix this later'''

def add_numbers_to_db(id, number):
    '''Add a new phone number to DB'''
    try:
        session.query(PhoneNumbers).filter(PhoneNumbers.id == id).one()
    except NoResultFound:
        new = PhoneNumbers(id=id, number=number)
        session.add(new)
        session.commit()
        with open('log', 'r+') as log:
                    log.seek(0, 2)
                    log.write(f'{datetime.now()}  {new} write to DB \n')
    
def check_number_exist(number):
    '''Check is number exist'''
    try:
        ph = session.query(PhoneNumbers).filter(PhoneNumbers.number == number[2:]).one()
        return(ph.id)
    except NoResultFound:
        return False
    