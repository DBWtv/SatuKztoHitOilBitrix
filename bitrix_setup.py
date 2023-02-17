from environs import Env
from fast_bitrix24 import Bitrix

env = Env()
env.read_env()

WEBHOOK = env('webhook')

b = Bitrix(WEBHOOK)

def post_new_deal(my_dict):
    b.call('crm.lead.add', raw=True, items=my_dict)
