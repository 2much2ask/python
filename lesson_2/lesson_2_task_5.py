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
print(prices, id(prices))  # после сортировки
# сортировка по убыванию
prices_sorted = sorted(prices, reverse=True)
print(prices_sorted, id(prices_sorted))
# по возрастанию
print(prices[:5])
