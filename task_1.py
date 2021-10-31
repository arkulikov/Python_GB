"""
- Реализовать класс Matrix (матрица).
- Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
- Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
- Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""
import random


def generetion_list():
    target_list = []

    i = 3
    while i != 0:
        res = [random.randrange(1, 50, 1) for i in range(3)]
        target_list.append(res)
        i -= 1
    return target_list


class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __add__(self, other):
        return Matrix([[self.my_list[i][j] + other.my_list[i][j] for j in range(len(self.my_list[0]))]
                       for i in range(len(self.my_list))])

    def __str__(self):
        return '\n'.join('\t'.join([str(i) for i in line]) for line in self.my_list)


mat_1 = Matrix(generetion_list())
mat_2 = Matrix(generetion_list())

print(f"{mat_1}\n")
print(f"{mat_2}\n")
print(mat_1 + mat_2)
