from requests import get, utils


def currency_rates(code):
    code = code.upper()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    if code not in content:
        return None
    else:
        for i in content.split(f'{code}')[1:]:
            for a in i.split('</Value')[:1]:
                result = round(float(a.split('<Value>')[1].replace(',', '.')), 2)
            return (f'1 {code} равен {result} руб')


print(currency_rates('usd'))
#print(currency_rates(input('Введите код валюты на латинице: ')))
