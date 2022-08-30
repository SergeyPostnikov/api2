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


def is_bitlink(authorization_token, bitlink):
    headers = {'Authorization': authorization_token}
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    response = requests.get(url, headers=headers)
    return response.ok


def main(link):    
    if is_bitlink(authorization_token, link):
        cilcks = count_clicks(authorization_token, link)
        return f"По вашей ссылке перешли {cilcks} раз(а)"
    return 'Битлинк', shorten_link(authorization_token, url)


if __name__ == '__main__':  
    load_dotenv()
    authorization_token = os.getenv('BITLY_TOKEN')  
    url = input('Введите ссылку: ')
    parsed_link = urlparse(url)
    link = f'{parsed_link.hostname}{parsed_link.path}'
    print(main(link))
