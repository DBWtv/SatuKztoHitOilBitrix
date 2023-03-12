from .connection import session, Orders
from sqlalchemy.exc import NoResultFound
import logging



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
        logging.info(f'Add to DB id={id}')
    return stmt
