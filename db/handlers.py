from .connection import session, Orders
from sqlalchemy.exc import NoResultFound
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
