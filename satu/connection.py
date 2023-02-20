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

    def get_messages_list(self, params=None):
        url = f'/api/v1/messages/list?{params}'
        method = 'GET'

        return self.make_request(method, url)

    def change_message_status(self, id):
        url = '/api/v1/messages/set_status'
        data = {
            'status': 'read',
            'ids': [id],
        }
        method = 'POST'

        return self.make_request(method, url, body=data)

    def change_order_status(self, id):
        url = f'/api/v1/orders/set_status'
        data = {
            'status': 'received',
            'ids': [id],
        }
        method = 'POST'

        return self.make_request(method, url, body=data)

    def reply_to_message(self, id):
        url = '/api/v1/messages/reply'
        data = {
            'id': id,
            'message': 'Мы получили ваше сообщение и скоро вам перезвоним',
        }

        method = 'POST'

        return self.make_request(method, url, body=data)


satu_api = EvoClientExample(AUTH_TOKEN)

order_list = satu_api.get_order_list('status=pending')

message_list = satu_api.get_messages_list('status=unread')

