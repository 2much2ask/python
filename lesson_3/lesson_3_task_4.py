def thesaurus(*names):
    alphabet = ['AБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ']
    names_dict = {}
    for name in names:
        names_dict[name[0]] = name
    return names_dict



print(thesaurus("Иван", "Мария", "Петр", "Илья", "Павел", "Элина"))
