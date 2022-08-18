import requests
import os

from urllib.parse import urlparse
from dotenv import load_dotenv
load_dotenv()


def count_clicks(token, bitlink):
    headers = {'Authorization': token}
    host = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    response = requests.get(host, headers=headers)
    response.raise_for_status()
    return response.json().get("total_clicks")


def shorten_link(token, url):
    headers = {'Authorization': token}
    host = 'https://api-ssl.bitly.com/v4/shorten'
    response = requests.post(host, headers=headers, json={'long_url': url})
    response.raise_for_status()
    return response.json().get('link') 


def long_link(token, bitlink):
    headers = {'Authorization': token}
    host = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    response = requests.get(host, headers=headers)
    response.raise_for_status()
    return response.json().get('long_url')


def is_bitlink(link):
    return urlparse(link).hostname == 'bit.ly' 


if __name__ == '__main__':
    token = os.getenv('TOKEN')  
    url = input('Введите ссылку: ')

    parse_result = urlparse(url) 
    if parse_result.hostname == 'bit.ly':
        print(long_link(
            token=token, 
            bitlink=f'{parse_result.hostname}{parse_result.path}'
            ))
    else:
        print('Битлинк', shorten_link(token, url))
