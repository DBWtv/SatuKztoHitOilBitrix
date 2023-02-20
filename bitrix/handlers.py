import sys
sys.path.append('/home/dmitry/dev/SatuKz')
from .connection import request
from db.handlers import add_numbers_to_db

def post_new_deal(my_dict=None):
    request.call('crm.lead.add', raw=True, items=my_dict)

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
        except:
            next
