"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""


number = input("Введите целое положительное число: ")
length = len(number)
max_numb = 0

while length > 0:
    if int(number[length - 1]) > max_numb:
        max_numb = int(number[length - 1])
    length -= 1

print(max_numb)
