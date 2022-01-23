def num_translate_adv(num_dictionary):
    numbers_dic = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
    }
    if num_dictionary.istitle():
        return numbers_dic.get(num_dictionary.lower()).capitalize()
    else:
        return numbers_dic.get(num_dictionary)


print(num_translate_adv(input('введите число на английском для перевода ')))
