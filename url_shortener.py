import requests
import os

from urllib.parse import urlparse
from dotenv import load_dotenv


def auth(f):
    def wrapper(*args, **kwargs):
        load_dotenv()
        authorization_token = os.getenv('BITLY_TOKEN')
        return f(authorization_token, *args, **kwargs)
    return wrapper


@auth
def count_clicks(authorization_token, bitlink):
    headers = {'Authorization': authorization_token}
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json().get('total_clicks')


@auth
def shorten_link(authorization_token, link):
    headers = {'Authorization': authorization_token}
    url = 'https://api-ssl.bitly.com/v4/shorten'
    response = requests.post(url, headers=headers, json={'long_url': link})
    response.raise_for_status()
    return response.json().get('link')


@auth
def is_bitlink(authorization_token, bitlink):
    headers = {'Authorization': authorization_token}
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.ok


if __name__ == '__main__':    
    url = input('Введите ссылку: ')
    parsed_link = urlparse(url)
    link = f'{parsed_link.hostname}{parsed_link.path}'

    if is_bitlink(link):
        cilcks = count_clicks(link)
        print(f"По вашей ссылке перешли {cilcks} раз(а)")
    else:
        print('Битлинк', shorten_link(url))
