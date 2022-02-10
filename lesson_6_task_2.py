logs = []
d = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    for line in file:
        log = line.split()
        ip = log[0]
        if ip not in d:
            d[ip] = 1
        else:
            d[ip] += 1

v = 0
k = ''
for key, value in d.items():
    if value > v:
        v = value
        k = key
print(f'c адреса {k} было максимальное число запросов: {v}')
