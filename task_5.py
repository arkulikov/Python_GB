"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти чётные числа от 100 до 1000 (включая границы).
Нужно получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce


def sum_func(el_1, el_2):
    return el_1 * el_2


print(reduce(sum_func, [el for el in range(100, 1001, 2)]))

print(reduce(lambda a, b: a * b, [el for el in range(100, 1001, 2)]))
