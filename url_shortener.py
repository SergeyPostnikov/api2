import requests
import os

from urllib.parse import urlparse
from dotenv import load_dotenv


def count_clicks(token, bitlink):
    headers = {'Authorization': token}
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json().get("total_clicks")


def shorten_link(token, url):
    headers = {'Authorization': token}
    url = 'https://api-ssl.bitly.com/v4/shorten'
    response = requests.post(url, headers=headers, json={'long_url': url})
    response.raise_for_status()
    return response.json().get('link') 


def long_link(token, bitlink):
    headers = {'Authorization': token}
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json().get('long_url')


def is_bitlink(link):
    headers = {'Authorization': token}
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json().get('long_url')


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('TOKEN')  
    url = input('Введите ссылку: ')

    parsed_link = urlparse(url) 
    if parsed_link.hostname == 'bit.ly':
        print(long_link(
            token=token, 
            bitlink=f'{parsed_link.hostname}{parsed_link.path}'
            ))
    else:
        print('Битлинк', shorten_link(token, url))
