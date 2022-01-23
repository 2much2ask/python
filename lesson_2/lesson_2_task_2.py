sentence = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

new_sentence = []
for el in sentence:
    if el.isdigit():
        new_sentence.append(f'"{el.zfill(2)}"')
    elif el[1:].isdigit() or el[0] == '+' or el[0] == '-':
        new_sentence.append(f'"{el[0] + el[1:].zfill(2)}"')
    else:
        new_sentence.append(el)
print(' '.join(new_sentence))
