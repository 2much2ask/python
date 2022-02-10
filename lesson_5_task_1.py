def odd_nums(a):
    for i in range(1, a + 1, 2):
        yield i


odd_to_15 = odd_nums(15)
for el in odd_to_15:
    print(el)
