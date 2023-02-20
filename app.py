import time
from satu.handlers import orders_db_work
from satu.connection import order_list, message_list



                    

def main():
    while True:

        orders_db_work(orders_list=order_list, messages_list=message_list)

        time.sleep(60)

if __name__=="__main__":
    main()
    