import time
from satu.handlers import orders_db_work
from satu.connection import satu_api
import logging

test_message = {'messages': [{'id': 2066403, 'date_created': '2023-03-01T00:50:59.476129+00:00', 'subject': 'Перезвоните мне: Многокомпонентный противогололедный материал Бионорд в мешках по 23 кг.', 'message': '', 'client_full_name': '', 'status': 'read', 'phone': '+77762282264', 'product_id': 106526401}]}

def main():
    '''
        App takes new orders and messages on satu.kz API.
        Then made deals in bitrix24
    '''
    logging.info('App started')
    i = 0
    while True:
        i += 1

        if i > 2:
            i = 0
        
        order_list = satu_api.get_order_list('status=pending')
        message_list = satu_api.get_messages_list('status=unread')
        
        orders_db_work(
            orders_list=order_list,
            messages_list=message_list,
            i=i,
            )

        time.sleep(60*5)


if __name__ == "__main__":
    main()
