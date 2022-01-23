def thesaurus(*names):
    names_dict = {}
    for name in names:
        if names_dict.get(name[0]) is None:
            names_dict[name[0]] = [name]
        else:
            names_dict[name[0]].append(name)
    return names_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Павел", "Элина"))
