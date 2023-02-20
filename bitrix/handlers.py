from .connection import request
from db.handlers import add_numbers_to_db
from datetime import datetime

def post_new_deal(my_dict=None):
    response = request.call('crm.lead.add', raw=True, items=my_dict)
    with open('log', 'r+') as log:
        log.seek(0, 2)
        log.write(f'{datetime.now()}  {response} \n')

def save_exist_contact():
    contact_list = request.get_all('crm.contact.list', params={'select': ['ID', 'PHONE']})

    chars = ' -()+'

    for contact in contact_list:
        try:
            phone_number_raw = contact['PHONE'][0]['VALUE'].strip()
            phone_number = phone_number_raw.translate(str.maketrans('', '', chars))
            if len(phone_number) == 11:
                add_numbers_to_db(id = int(contact['ID']), number = phone_number[1:])
            if len(phone_number) == 12:
                add_numbers_to_db(id = int(contact['ID']), number = phone_number[2:])
            with open('log', 'r+') as log:
                log.seek(0, 2)
                log.write(f'{datetime.now()} {contact} add to DB \n')
        except:
            with open('log', 'r+') as log:
                log.seek(0, 2)
                log.write(f'{datetime.now()}  contact not fit: {contact} \n')
            next

