from base import parse
import datetime

date = datetime.datetime.today() + datetime.timedelta(days=1)
tomorrow = f'{date.year}-{date.month}-{date.day}'
url = 'https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%' \
      'D0%B8%D1%97%D0%B2' + f'/{tomorrow}'


tomorrow = parse(url)
print(tomorrow)
