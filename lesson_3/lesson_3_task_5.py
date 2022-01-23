import random
from random import choice, sample

def get_jokes(n, repeat=True):
    """Returns n jokes with random words from the lists"""

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    joke_list = []
    a = 0
    if repeat:
        while a < n:
            joke = choice(nouns) + ' ' + choice(adverbs) + ' ' + choice(adjectives)
            joke_list.append(joke)
            a += 1
    else:
        noun = random.sample(nouns, n)
        adverb = random.sample(adverbs, n)
        adjective = random.sample(adjectives, n)
        while a < n:
            joke = noun[a] + ' ' + adverb[a] + ' ' + adjective[a]
            joke_list.append(joke)
            a += 1
    return joke_list


print(get_jokes(4))
#print(get_jokes(int(input('введите число шуток, которые вам нужны '))))
