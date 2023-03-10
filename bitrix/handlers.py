from .connection import request
from satu.connection import satu_api
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('http_connection.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def post_new_deal(is_message: bool, item_id, my_dict=None):
    '''
        Post a dictionary to "crm.lead.add" bitrix24 method
        If deal posted - send back to satu.kz answer to message or change status of satu.kz deal
    '''

    try:
        request.call('crm.lead.add', raw=True, items=my_dict)
    except:
        logger.exception(' --- Connection to Bitrix get HTTPError')
    else:
        if is_message:
            satu_api.reply_to_message(item_id)
        else:
            satu_api.change_order_status(item_id)
            logger.info(' --- Connection to Bitrix is OK')

def get_contact_id(phone_number):
    try:
        response = request.get_all(
                'crm.contact.list',
                params={
                    'select': ['ID'],
                    'filter': {'PHONE': phone_number}})
    except:
        logger.exception(' --- Connection to Bitrix get HTTPError')
    else:
        contact_id = response[0]['ID']
        logger.info(' --- Connection to Bitrix is OK')
    return(contact_id)


def save_exist_contact(phone_number):
    '''
        Request "crm.contact.list" bitrix method, with search field PHONE
        Check with given number format = +79999999999. Is not exist check with format = 89999999999
        Then return id f contact, takes only first. If contact dose not exist = return False
    '''
    if len(phone_number) == 11:
        phone_number = '+7' + phone_number[1:]    
    try:
        '''+7'''
        contact_id = get_contact_id(phone_number)
    except:
        try:
            '''8'''
            phone_number = '8' + phone_number[2:]
            contact_id = get_contact_id(phone_number)
        except:
            contact_id = False

    return contact_id

if __name__=='__main__':
    pass