from environs import Env
import json
import http.client

env = Env()
env.read_env()

# API Settigs
AUTH_TOKEN = env('api_token')  # Your authorization token
HOST = 'my.satu.kz'  # e.g.: my.prom.ua, my.tiu.ru, my.satu.kz, my.deal.by, my.prom.md

class HTTPError(Exception):
    pass

class EvoClientExample(object):

    def __init__(self, token):
        self.token = token

    def make_request(self, method, url, body=None):
        connection = http.client.HTTPSConnection(HOST)

        headers = {'Authorization': 'Bearer {}'.format(self.token),
                   'Content-type': 'application/json'}
        if body:
            body = json.dumps(body)

        connection.request(method, url, body=body, headers=headers)
        response = connection.getresponse()
        if response.status != 200:
            pass

        response_data = response.read()
        return json.loads(response_data.decode())

    def get_order_list(self, params=None):
        url = f'/api/v1/orders/list?{params}'
        method = 'GET'

        return self.make_request(method, url)
    
    def get_messages_list(self):
        url = f'/api/v1/messages/list'
        method = 'GET'

        return self.make_request(method, url)


print(EvoClientExample(AUTH_TOKEN).get_messages_list())
    