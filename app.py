import time
from satu.handlers import orders_db_work
from satu.connection import satu_api
import logging


def main():
    '''
        App takes new orders and messages on satu.kz API.
        Then made deals in bitrix24
    '''
    logging.info('App started')
    
    while True:
        order_list = satu_api.get_order_list('status=pending')
        message_list = satu_api.get_messages_list('status=unread')
        
        orders_db_work(
            orders_list=order_list,
            messages_list=message_list,
            )

        time.sleep(60*10)


if __name__ == "__main__":
    main()
