# я не поняла как делать данное задание, в попытке разобраться
# перепечатала решение с урока, но оно не работает,
# рыдаю и не понимаю что такое матрица и как она формируется

class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        sum_matrix = []
        for i in range(len(self.lists)):
            sum_matrix.append([])
            for j in range(len(self.lists[0])):
                sum_matrix[i].append(self.lists[i][j] + other[i][j])
        return Matrix.sum_matrix()


a = [11,12,15]
b = [13,15,16]
matrix_1 = Matrix(a)
matrix_2 = Matrix(b)
print(f'Matrix 1\n{matrix_1}\n{"-" * 20}')
print(f'Matrix 2\n{matrix_2}\n{"-" * 20}')
print(f'matrix_1+matrix_2\n{matrix_1 + matrix_2}')
