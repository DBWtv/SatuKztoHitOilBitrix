from environs import Env
import json
import http.client
import logging

env = Env()
env.read_env()

# API Settigs
AUTH_TOKEN = env('api_token')  # Your authorization token
HOST = 'my.satu.kz'  # e.g.: my.prom.ua, my.tiu.ru, my.satu.kz, my.deal.by, my.prom.md

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%y-%m-%d %H:%M:%S',
    filename='status.log',
)


class HTTPError(Exception):
    pass


class EvoClientExample(object):
    '''
        Class wich takes auth token of satu.kz and made requests to satu api
    '''

    def __init__(self, token):
        self.token = token

    def make_request(self, method, url, body=None):
        '''Function make requests'''
        connection = http.client.HTTPSConnection(HOST)

        headers = {'Authorization': 'Bearer {}'.format(self.token),
                   'Content-type': 'application/json'}
        if body:
            body = json.dumps(body)

        connection.request(method, url, body=body, headers=headers)
        response = connection.getresponse()
        if response.status != 200:
            logging.warning(f'{response.status}')
            pass

        logging.info(f'{response.status}')
        response_data = response.read()
        return json.loads(response_data.decode())

    def get_order_list(self, params=None):
        '''Function get all orders'''
        url = f'/api/v1/orders/list?{params}'
        method = 'GET'

        return self.make_request(method, url)

    def get_messages_list(self, params=None):
        '''Function get all messages'''
        url = f'/api/v1/messages/list?{params}'
        method = 'GET'

        return self.make_request(method, url)

    def change_message_status(self, id):
        '''Function changes status of message'''
        url = '/api/v1/messages/set_status'
        data = {
            'status': 'read',
            'ids': [id],
        }
        method = 'POST'

        return self.make_request(method, url, body=data)

    def change_order_status(self, id):
        '''Function changes status of order'''
        url = f'/api/v1/orders/set_status'
        data = {
            'status': 'received',
            'ids': [id],
        }
        method = 'POST'

        return self.make_request(method, url, body=data)

    def reply_to_message(self, id):
        '''Function send reply to message'''
        url = '/api/v1/messages/reply'
        data = {
            'id': id,
            'message': 'Мы получили ваше сообщение и скоро вам перезвоним!',
        }

        method = 'POST'

        self.change_message_status(id)

        return self.make_request(method, url, body=data)


satu_api = EvoClientExample(AUTH_TOKEN)
