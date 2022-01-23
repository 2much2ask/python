def thesaurus_adv(*names):
    names_dict = {}
    for name in names:
        name_first_letter, surname_first_letter = name[0], name[name.find(' ')+1]
        if surname_first_letter not in names_dict:
            names_dict[surname_first_letter] = {name_first_letter: [name]}
        elif name_first_letter in names_dict[surname_first_letter]:
            names_dict[surname_first_letter][name_first_letter].append(name)
        else:
            names_dict[surname_first_letter][name_first_letter] = [name]
    return names_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
