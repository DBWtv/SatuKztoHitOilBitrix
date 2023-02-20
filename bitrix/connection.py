from environs import Env
from fast_bitrix24 import Bitrix

env = Env()
env.read_env()

WEBHOOK = env('webhook')

request = Bitrix(WEBHOOK)
