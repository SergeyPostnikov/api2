import requests
import os

from urllib.parse import urlparse
from dotenv import load_dotenv


def count_clicks(authorization_token, bitlink):
    headers = {'Authorization': authorization_token}
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json().get('total_clicks')


def shorten_link(authorization_token, link):
    headers = {'Authorization': authorization_token}
    url = 'https://api-ssl.bitly.com/v4/shorten'
    response = requests.post(url, headers=headers, json={'long_url': link})
    response.raise_for_status()
    return response.json().get('link')



def is_bitlink(link, authorization_token):
    headers = {'Authorization': authorization_token}
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json().get('long_url')


if __name__ == '__main__':  
    load_dotenv()
    authorization_token = os.getenv('BITLY_TOKEN')  
    url = input('Введите ссылку: ')
    parsed_link = urlparse(url) 
    if parsed_link.hostname == 'bit.ly':
        cilcks = count_clicks(
            authorization_token, 
            f'{parsed_link.hostname}{parsed_link.path}')
        print(f"По вашей ссылке перешли {cilcks} раз(а)")
    else:
        print('Битлинк', shorten_link(authorization_token, url))
