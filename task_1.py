duration = int(input("введите количество секунд: "))

seconds = duration % 60
minutes = duration // 60
hours = minutes // 60
days = hours // 24


if duration < 60:
    print(seconds, "сек")
elif 1 <= minutes < 60:
    print(minutes, "мин", seconds, "сек")
elif 1 <= hours < 24:
    print(hours, "час", minutes % 60, "мин", seconds, "сек")
else:
    print(days, "дн", hours % 24, "час", minutes % 60, "мин", seconds, "сек")

