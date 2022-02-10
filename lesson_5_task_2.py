n = int(input('введите последнее число в последовательности: '))
odd_nums = (num for num in range(1, n+1, 2))
print(*odd_nums)
