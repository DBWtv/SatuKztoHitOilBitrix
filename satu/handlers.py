from db.handlers import check_sttm_db, add_to_db, check_number_exist
from bitrix.handlers import post_new_deal, save_exist_contact
from .connection import satu_api



def orders_dict_to_bitrix(item, i, bitrix_contact_id=None):
    managers = [11, 19, 21]
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
            'ASSIGNED_BY_ID': managers[i],
            'CREATED_BY_ID': 0,
        },
        'params': {'REGISTER_SONET_EVENT': 'Y'}
    }

    if bitrix_contact_id == None:
        orders_dict['fields']['PHONE'] = [{'VALUE': item['phone']}]

    return post_new_deal(orders_dict)


def messages_dict_to_bitrix(item, i, bitrix_contact_id=None):
    managers = [11, 19, 21]
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
            'ASSIGNED_BY_ID': managers[i],
            'CREATED_BY_ID': 0,
        },
        'params': {'REGISTER_SONET_EVENT': 'Y'}
    }

    if bitrix_contact_id == None:
        messages_dict['fields']['PHONE'] = [{'VALUE': item['phone']}]

    return post_new_deal(messages_dict)


def orders_db_work(messages_list, orders_list, i=0):
    for order in orders_list['orders']:
        i += 1
        if i > 2:
            i = 0
        if check_sttm_db(order['id']):
            if add_to_db(order['id']):
                save_exist_contact()
                satu_api.change_order_status(order['id'])
                if check_number_exist(order['phone']):
                    orders_dict_to_bitrix(
                        order, i=i, bitrix_contact_id=check_number_exist(order['phone']))
                else:
                    orders_dict_to_bitrix(order, i=i)

    for message in messages_list['messages']:
        i += 1
        if i > 2:
            i = 0
        if check_sttm_db(message['id']):
            if add_to_db(message['id']):
                save_exist_contact()
                satu_api.reply_to_message(message['id'])
                if check_number_exist(message['phone']):
                    messages_dict_to_bitrix(
                        message, i=i, bitrix_contact_id=check_number_exist(message['phone']))
                else:
                    messages_dict_to_bitrix(message, i=i)
