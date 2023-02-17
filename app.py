from setup import EvoClientExample, AUTH_TOKEN
from db_base import add_to_db, check_sttm_db
from bitrix_setup import post_new_deal
import time


while True:
    api_class = EvoClientExample(AUTH_TOKEN)

    order_list = api_class.get_order_list('status=pending')

    for order in order_list['orders']:
        if check_sttm_db(order['id']):
            if add_to_db(order['id']):
                email = order['email']
                products = order['products'][0]
                product_title = products['name']
                title = f'Заявка с сайта satu.kz "{product_title}"'
                post_dict = {
                    'fields': {
                        'TITLE': title,
                        'NAME': order['client_first_name'],
                        'SECOND_NAME': order['client_second_name'],
                        'LAST_NAME': order['client_last_name'],
                        'SOURCE_DESCRIPTION': products['url'],
                        'HAS_PHONE': 'Y',
                        'STATUS_ID': 'NEW',
                        'OPENED': 'Y',
                        'PHONE': [{'VALUE': order['phone']}],
                        },
                        'params': { 'REGISTER_SONET_EVENT': 'Y'}
                    }
                post_new_deal(post_dict)

    time.sleep(60*5)
    