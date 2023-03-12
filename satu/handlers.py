from db.handlers import add_to_db
from bitrix.handlers import post_new_deal, save_exist_contact


def orders_dict_to_bitrix(item, i, is_message=False, bitrix_contact_id=None,):
    managers = [11, 19, 21]

    try:
        products = item['products']
        if len(products) == 1:
            title = products[0]['name']
            prod_url = products[0]['url']
        elif len(products) > 1:
            title = ''
            prod_url = ''
            for product in products:
                prod_url += products['url'] + '; '
                title += product + '; '
    except:
        products = None
        title = ''

    if is_message == True:
        title = item['subject']
        message = item['message']
        orders_dict = {
            'fields': {
                'TITLE': title,
                'NAME': item['client_full_name'],
                'HAS_PHONE': 'Y',
                'STATUS_ID': 'NEW',
                'OPENED': 'Y',
                'SOURCE_DESCRIPTION': message,
                'CONTACT_ID': bitrix_contact_id,
                'ASSIGNED_BY_ID': managers[i],
                'CREATED_BY_ID': 0,
            },
            'params': {'REGISTER_SONET_EVENT': 'Y'}
        }

    if is_message == False:
        orders_dict = {
            'fields': {
                'TITLE': title,
                'NAME': item['client_first_name'],
                'SECOND_NAME': item['client_second_name'],
                'LAST_NAME': item['client_last_name'],
                'WEB': prod_url,
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

    return post_new_deal(is_message, item['id'], orders_dict)


def orders_db_work(messages_list, orders_list, i=0):
    for order in orders_list['orders']:
        if i > 2:
            i = 0
        if add_to_db(order['id']):
            contact_id = save_exist_contact(order['phone'])
            if contact_id:
                orders_dict_to_bitrix(
                    order, i=i, bitrix_contact_id=contact_id)
            else:
                orders_dict_to_bitrix(order, i=i)
        i += 1

    for message in messages_list['messages']:
        if i > 2:
            i = 0
        if add_to_db(message['id']):
            contact_id = save_exist_contact(message['phone'])
            if contact_id:
                orders_dict_to_bitrix(
                    message, i=i, bitrix_contact_id=contact_id, is_message=True)
            else:
                orders_dict_to_bitrix(message, i=i, is_message=True)
        i += 1
