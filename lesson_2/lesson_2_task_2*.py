sentence = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i in range(len(sentence)):
    if sentence[i].isdigit():
        sentence.insert(i, f'"{sentence[i].zfill(2)}"')
        sentence.remove(sentence[i+1])
    elif sentence[i][1:].isdigit() or sentence[i][0] == '+' or sentence[i][0] == '-':
        sentence.insert(i, f'"{sentence[i][0] + sentence[i][1:].zfill(2)}"')
        sentence.remove(sentence[i + 1])
    else:
        continue
    i += 1

print(' '.join(sentence))
