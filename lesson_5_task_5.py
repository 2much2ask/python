src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [i for i in src if src.count(i) == 1]

print(result)

#  быстрый вариант из методички
unique_nums = set()
tmp = set()
for i in src:
    if i not in tmp:
        unique_nums.add(i)
    else:
        unique_nums.discard(i)
    tmp.add(i)
result = [i for i in src if i in unique_nums]
print(result)
