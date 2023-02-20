from bitrix.connection import request

def post_new_deal(my_dict=None):
    request.call('crm.lead.add', raw=True, items=my_dict)

print(request.get_all('crm.lead.list')[0])