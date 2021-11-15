import parse

url = 'https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%' \
      'D0%B8%D1%97%D0%B2'


today = 'Погода сьогодні:\n' + parse.text(url)
