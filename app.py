import time
from satu.handlers import orders_db_work
from satu.connection import satu_api
import logging
from datetime import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('runing_time.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def main():
    '''
        App takes new orders and messages on satu.kz API.
        Then made deals in bitrix24
    '''
    logger.info('App started')
    start_time = datetime.now()
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
        logger.info(f' --- Current running time: {datetime.now() - start_time}')
        time.sleep(60*10)
    

if __name__ == "__main__":
    main()
