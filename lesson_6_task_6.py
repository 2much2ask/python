# файл add_sale.py
import sys


def add_sales(number):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(number + '\n')


if __name__ == '__main__':
    num = sys.argv[1]
    add_sales(num)

# файл show_sales.py
import sys


with open('bakery.csv', 'r', encoding='utf-8') as a:
    content = a.read()
    if len(sys.argv) == 1:
        print(content)
    elif len(sys.argv) == 3:
        index = int(sys.argv[1])
        index_2 = int(sys.argv[2])
        print(content[(index - 1):(index_2+1)])
    else:
        index = int(sys.argv[1])
        print(content[(index - 1):])
