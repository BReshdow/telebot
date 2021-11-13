import requests
from bs4 import BeautifulSoup


def parse(url) -> str or None:
    # Getting html code
    html = requests.get(url).content
    # Creating BeautifulSoup object
    bs = BeautifulSoup(html, 'lxml')
    # Getting information
    tmp = bs.find('div', class_='tabsContent')\
        .find('tr', class_='temperature').findAll()
    if tmp:
        temp_list = [el.text[:2] for el in tmp]
        print(temp_list)
    return None
