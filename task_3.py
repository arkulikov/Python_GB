"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    try:
        return sum((a, b, c)) - min((a, b, c))
    except TypeError:
        return "Введите числа!"


print(my_func(4, 2, 'r'))