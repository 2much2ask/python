from requests import get, utils
import datetime

def currency_rates(code):
    code = code.upper()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    date_on_server = (content.split('Date="'))[1].split('"')[0].split('.')
    date_on_server.reverse()

    if code not in content:
        return None
    else:
        for i in content.split(f'{code}')[1:]:
            for a in i.split('</Value')[:1]:
                result = round(float(a.split('<Value>')[1].replace(',', '.')), 2)
                return f'1 {code} равен {result} руб\nдата: {datetime.date(*map(int, date_on_server))}'

print(currency_rates('usd'))
# print(currency_rates(input('Введите код валюты на латинице: ')))




