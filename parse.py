import requests
from bs4 import BeautifulSoup


def text(url):
    w_tuple = parse(url)
    description = f'{w_tuple[0]}\n' + f'{w_tuple[1]}\n' if w_tuple[1] \
        else f'{w_tuple[0]}\n'
    return description + f'8:00:  {w_tuple[2][0]} {w_tuple[3][0]}м/с\n'\
                         f'11:00: {w_tuple[2][1]} {w_tuple[3][1]}м/с\n'\
                         f'14:00: {w_tuple[2][2]} {w_tuple[3][2]}м/с\n'\
                         f'17:00: {w_tuple[2][3]} {w_tuple[3][3]}м/с\n'\
                         f'20:00: {w_tuple[2][4]} {w_tuple[3][4]}м/с\n'\
                         f'23:00: {w_tuple[2][5]} {w_tuple[3][5]}м/с\n'


def parse(url) -> str or None:
    # Getting html code
    html = requests.get(url).content
    # Creating BeautifulSoup object
    bs = BeautifulSoup(html, 'lxml')
    # Main for tmp and rain
    main_ = bs.find('div', class_='tabsContent')
    # Getting temperature
    tmp = main_.find('tr', class_='temperature').find_all()
    temp_list = [el.text for el in tmp] if tmp else None
    # Getting probability of precipitation
    rain = main_.find('tr', class_='temperatureSens')\
        .find_next('tr', class_='gray').find_next('tr', class_='gray')\
        .find_next('tr').find_all()
    rain_list = [el.text for el in rain] if rain else None
    # Getting description for a day
    weather = bs.find('div', class_='wDescription clearfix')\
        .find('div', class_='rSide').find('div')
    weather_text = weather.text.strip() if weather else None
    # Getting warnings
    warnings = bs.find('div', class_='oWarnings clearfix')
    warnings = warnings.find('div', class_='rSide').find('div').find('span') \
        if warnings else None
    warning_text = warnings.text if warnings else None
    # Returning result
    return weather_text, warning_text, temp_list[2:], rain_list[2:]
