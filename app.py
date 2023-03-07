import time
from satu.handlers import orders_db_work
from satu.connection import satu_api
from datetime import datetime


def main():
    '''
        App takes new orders and messages on satu.kz API.
        Then made deals in bitrix24
    '''
    start_time = time.time()

    if time.time() - start_time >= 10:
        start_time = time.time()
        file_name = f'log_{datetime.now().year}-{datetime.now().month}-{datetime.now().day}.txt'
        with open(file_name, 'w') as log:
            log.seek(0, 2)
            log.write(f'{datetime.now()} ... Starting app \n')
    while True:
        order_list = satu_api.get_order_list('status=pending')
        message_list = satu_api.get_messages_list('status=unread')

        orders_db_work(orders_list=order_list, messages_list=message_list)

        time.sleep(60*15)


if __name__ == "__main__":
    main()
