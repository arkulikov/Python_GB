"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""


number = input("Введите целое число: ")
number_two = int(number + number)
number_three = int(number + number + number)

final_number = int(number) + number_two + number_three
print(final_number)
