import sys
sys.path.append('/home/dmitry/dev/SatuKz')
from db.handlers import check_sttm_db, add_to_db
from satu.connection import order_list, message_list

def orders_dict_to_bitrix(item):
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
            'PHONE': [{'VALUE': item['phone']}],
        },
        'params': {'REGISTER_SONET_EVENT': 'Y'}
    }
    return print(orders_dict)


def messages_dict_to_bitrix(item):
    subject = item['subject']
    message = item['message']
    messages_dict = {
        'fields': {
            'TITLE': f'Заявка с сайта satu.kz "{subject}"',
            'NAME': item['client_full_name'],
            'HAS_PHONE': 'Y',
            'STATUS_ID': 'NEW',
            'OPENED': 'Y',
            'PHONE': [{'VALUE': item['phone']}],
        },
        'params': {'REGISTER_SONET_EVENT': 'Y'}
    }
    return print(messages_dict)


def orders_db_work(messages_list, orders_list):
    for order in orders_list['orders']:
        if check_sttm_db(order['id']):
            if add_to_db(order['id']):
                print('new order')
                orders_dict_to_bitrix(order)
    for message in messages_list['messages']:
        if check_sttm_db(message['id']):
            if add_to_db(message['id']):
                print('new message')
                messages_dict_to_bitrix(message)
    


print(orders_db_work(orders_list=order_list, messages_list=message_list))