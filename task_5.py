# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

user_number = int(input("Введите элемент рейтинга (число больше нуля): "))
my_list = [7, 5, 3, 3, 2]

count_all_el = my_list.count(user_number)  # кол-во чисел введенных юзером в списке

if user_number < 0 or user_number == 0:
    print("Введите число больше нуля!")
else:
    if count_all_el > 0:
        index_first_el = my_list.index(user_number)
        my_list.insert(index_first_el + count_all_el, user_number)
    elif count_all_el == 0:
        i = 0
        for el in range(int(len(my_list))):
            if user_number > my_list[i]:
                my_list.insert(i, user_number)
                break
            elif user_number < my_list[i]:
                if user_number > my_list[i +1]:
                    my_list.insert(i + 1, user_number)
                else:
                    if my_list[i + 1] == my_list[-1]:
                        my_list.append(user_number)
                    else:
                        i += 1
                        continue

    print(my_list)