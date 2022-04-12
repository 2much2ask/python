import re


def email_parse(email_address):
    pattern = re.compile(r'(?P<username>[a-z0-9_.+-]+)@(?P<domain>[a-z0-9_.-]+\.[a-z0-9-.]+)')
    result = pattern.match(email_address.lower())
    if not result:
        raise ValueError(f'wrong email: {email_address}')
    return result.groupdict()


print(email_parse('BELL_vin@y_a.ru'))
