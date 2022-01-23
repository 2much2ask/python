prices = [22.5, 15.87, 120, 10.03, 19.99, 18.98, 5, 0.15, 17, 13.5]
price_list = []
for i in prices:
    roubles = int(i)
    kop = int((i - int(i)) * 100)
    item = f"{roubles} руб. {kop:02d} коп"
    price_list.append(item)
print(', '.join(price_list))

# сортировка по возрастанию
print(id(prices))  # до сортировки
prices.sort()
price_list = []
for i in prices:
    roubles = int(i)
    kop = int((i - int(i)) * 100)
    item = f"{roubles} руб. {kop:02d} коп"
    price_list.append(item)
print(', '.join(price_list))
print(id(prices))  # id после сортировки

# сортировка по убыванию
prices_sorted = sorted(prices, reverse=True)
price_list = []
for i in prices_sorted:
    roubles = int(i)
    kop = int((i - int(i)) * 100)
    item = f"{roubles} руб. {kop:02d} коп"
    price_list.append(item)
print(', '.join(price_list))
print(id(prices_sorted))  # это новый список
# 5 самых дорогих товаров в списке
print(', '.join(price_list[:5]))
