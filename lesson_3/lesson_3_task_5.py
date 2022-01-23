from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n):
    """Returns n jokes with random words from the lists"""
    joke_list = []
    a = 1
    while a <= n:
        joke = choice(nouns) + ' ' + choice(adverbs) + ' ' + choice(adjectives)
        joke_list.append(joke)
        a += 1
    return joke_list


print(get_jokes(4))

# print(get_jokes(input('введите число шуток, которые вам нужны ')))
