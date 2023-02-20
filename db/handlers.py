from .connection import session, Orders, NoResultFound, PhoneNumbers

def add_to_db(id):
    try:
        stmt = session.query(Orders).filter(Orders.id == id).one()
        stmt = False
    except NoResultFound:
        new = Orders(id=id)
        session.add(new)
        session.commit()
        stmt = True     

    return stmt

def check_sttm_db(id):
    try:
        stmt = session.query(Orders).filter(Orders.id == id).one().id
        stmt  = False
    except NoResultFound:
        stmt = True

    return stmt

def add_numbers_to_db(id, number):
    try:
        session.query(PhoneNumbers).filter(PhoneNumbers.id == id).one()
    except NoResultFound:
        new = PhoneNumbers(id=id, number=number)
        session.add(new)
        session.commit()
    
def check_number_exist(number):
    try:
        ph = session.query(PhoneNumbers).filter(PhoneNumbers.number == number[2:]).one()
        return(ph.id)
    except NoResultFound:
        return False
    