job_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
            'директор аэлита']

for i in job_list:
    item = i.split(" ")
    name = item[-1]
    print(f"Привет, {name.capitalize()}!")


# еще решение
for i in range(len(job_list)):
    name = job_list[i]
    a = name.rfind(' ')
    name_new = name[a+1:]   # добавляю 1 чтобы не было пробела в начале имени
    print(f"Привет, {name_new.capitalize()}!")
