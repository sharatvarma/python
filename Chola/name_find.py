import requests
from bs4 import BeautifulSoup


def print_cholakings():
    url = 'https://en.wikipedia.org/wiki/Chola_dynasty'
    src_code = requests.get(url)
    plain_code = src_code.text
    soup = BeautifulSoup(plain_code, 'html.parser')
    for name in soup.find_all('a', {'id': 'mw-content-text'}):
        title = name.get('title')
        print(title)

print_cholakings()
