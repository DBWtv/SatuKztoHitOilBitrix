from db.connection import session, Orders, NoResultFound

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