"""
Реализовать программу работы с органическими клетками.
Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
- сложение (add()),
- вычитание (sub()),
- умножение (mul()),
- деление (truediv()).
Данные методы должны применяться только к клеткам и выполнять
- увеличение,
- уменьшение,
- умножение
- и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
--Сложение. Объединение двух клеток.
При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
--Вычитание. Участвуют две клетки.
Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.
--Умножение. Создается общая клетка из двух.
Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
--Деление. Создается общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""
import random


def random_of_cells():
    return random.randrange(1, 20)


class Cell:
    def __init__(self, number_of_cells):
        self.number_of_cells = number_of_cells

    def __add__(self, other):
        return Cell(self.number_of_cells + other.number_of_cells)

    def __sub__(self, other):
        if self.number_of_cells - other.number_of_cells > 0:
            return Cell(self.number_of_cells - other.number_of_cells)
        elif other.number_of_cells - self.number_of_cells > 0:
            return Cell(other.number_of_cells - self.number_of_cells)
        else:
            return f"Эти клетки не подходят!!!"

    def __mul__(self, other):
        return Cell(self.number_of_cells * other.number_of_cells)

    def __truediv__(self, other):
        return Cell(self.number_of_cells // other.number_of_cells)

    def __str__(self):
        return f"Новая клетка {self.number_of_cells}"

    def make_order(self, number_in_row):
        return '/n'.join(['*' * number_in_row for _ in range(self.number_of_cells // number_in_row)]) + '/n' + '*' * (self.number_of_cells % number_in_row)


cell_one = Cell(random_of_cells())
cell_two = Cell(random_of_cells())

print(cell_one)
print(cell_two)

print(cell_one + cell_two)
print(cell_one - cell_two)
print(cell_one * cell_two)
print(cell_one / cell_two)
print(cell_two.make_order(2))
