from setup import EvoClientExample, AUTH_TOKEN
from db_base import add_to_db, check_sttm_db


api_class = EvoClientExample(AUTH_TOKEN)

order_list = api_class.get_order_list('status=pending')

for order in order_list['orders']:
    if check_sttm_db(order['id']):
        add_to_db(order['id'])