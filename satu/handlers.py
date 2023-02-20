from db.handlers import check_sttm_db, add_to_db, check_number_exist
from bitrix.handlers import post_new_deal, save_exist_contact



def orders_dict_to_bitrix(item, bitrix_contact_id=None):
    products = item['products'][0]
    product_title = products['name']
    title = f'Заявка с сайта satu.kz "{product_title}"'
    orders_dict = {
        'fields': {
            'TITLE': title,
            'NAME': item['client_first_name'],
            'SECOND_NAME': item['client_second_name'],
            'LAST_NAME': item['client_last_name'],
            'SOURCE_DESCRIPTION': products['url'],
            'HAS_PHONE': 'Y',
            'STATUS_ID': 'NEW',
            'OPENED': 'Y',
            'CONTACT_ID': bitrix_contact_id,
        },
        'params': {'REGISTER_SONET_EVENT': 'Y'}
    }

    if bitrix_contact_id == None:
        orders_dict['fields']['PHONE'] = [{'VALUE': item['phone']}]

    return post_new_deal(orders_dict)


def messages_dict_to_bitrix(item, bitrix_contact_id=None):
    subject = item['subject']
    message = item['message']
    messages_dict = {
        'fields': {
            'TITLE': f'Заявка с сайта satu.kz "{subject}"',
            'NAME': item['client_full_name'],
            'HAS_PHONE': 'Y',
            'STATUS_ID': 'NEW',
            'OPENED': 'Y',
            'CONTACT_ID': bitrix_contact_id,
        },
        'params': {'REGISTER_SONET_EVENT': 'Y'}
    }

    if bitrix_contact_id == None:
        messages_dict['fields']['PHONE'] = [{'VALUE': item['phone']}]

    return post_new_deal(messages_dict)


def orders_db_work(messages_list, orders_list):
    for order in orders_list['orders']:
        if check_sttm_db(order['id']):
            if add_to_db(order['id']):
                save_exist_contact()
                if check_number_exist(order['phone']):
                    orders_dict_to_bitrix(order, bitrix_contact_id=check_number_exist(order['phone']))
                else:
                    orders_dict_to_bitrix(order)

    for message in messages_list['messages']:
        if check_sttm_db(message['id']):
            if add_to_db(message['id']):
                save_exist_contact()
                if check_number_exist(message['phone']):
                    messages_dict_to_bitrix(message, bitrix_contact_id=check_number_exist(message['phone']))
                else:
                    messages_dict_to_bitrix(message)
    
