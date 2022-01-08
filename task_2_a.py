#Решение 1

list_of_numbers = []
for i in range(1001):
    if i % 2:
        list_of_numbers.append(i**3)

sum_of_numbers = 0 #сумма чисел, сумма цифр которых делится на 7
sum_of_numbers_2 = 0 #сумма чисел+17, сумма цифр которых делится на 7

for i in list_of_numbers:
    j = i
    sum_number = 0
    while j % 10:
        a = j % 10
        sum_number = sum_number + a
        j = j // 10
    if not sum_number % 7:
        sum_of_numbers += i

print(sum_of_numbers)

new_list = []
for i in list_of_numbers:
    new_list.append(i + 17)

for i in new_list:
    j = i
    sum_number = 0
    while j % 10:
        a = j % 10
        sum_number += a
        j = j // 10
    if not sum_number % 7:
        sum_of_numbers_2 += i

print(sum_of_numbers_2)


#Решение 2

list_of_cubes = []
all_sum = 0

for i in range(1,1001):
    if i % 2 != 0:
        list_of_cubes.append(i**3)

for ind, val in enumerate(list_of_cubes):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10
        val = val // 10
        if sum_digits % 7 == 0:
            all_sum += list_of_cubes[ind]

print(all_sum)

list_of_cubes_add17 = []
all_sum = 0
for i in list_of_cubes:
    list_of_cubes_add17.append(i + 17)

for ind, val in enumerate(list_of_cubes_add17):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10
        val = val // 10
        if sum_digits % 7 == 0:
            all_sum += list_of_cubes_add17[ind]

print(all_sum)








        
