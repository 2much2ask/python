from itertools import zip_longest


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


if len(tutors) >= len(klasses):
    tutor_klass = (i for i in zip_longest(tutors, klasses, fillvalue=None))
else:
    tutor_klass = (i for i in zip(tutors, klasses))


print(type(tutor_klass))
print(*tutor_klass, sep='\n')
