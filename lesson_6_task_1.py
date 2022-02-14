logs = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    for line in file:
        log = line.split()
        logs.append((log[0], log[5][1:], log[6]))
print(logs[0])
