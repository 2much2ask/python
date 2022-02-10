import json
import sys
from itertools import zip_longest


hobby_list = {}
with open('users.csv', 'r', encoding='UTF-8') as file_1:
    names = []
    for name in file_1:
        names.append(name.strip())

with open('hobby.csv', 'r', encoding='UTF-8') as file_2:
    hobbies = []
    for hobby in file_2:
        hobbies.append(hobby.strip())

for i in range(len(names)):
    if len(names) < len(hobbies):
        sys.exit(1)
    else:
        for name, hobby in zip_longest(names, hobbies, fillvalue=None):
            hobby_list[name] = hobby
print(hobby_list)

with open('hobby_list.json', 'w', encoding='UTF-8') as a:
    json.dump(hobby_list, a)
with open('hobby_list.json', 'r', encoding='UTF-8') as b:
    hobby_list = json.load(b)
print(hobby_list, type(hobby_list))
