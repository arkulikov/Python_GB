"""
Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым
и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f"Имя сотрудника: {self.name}, Фамилия сотрудника: {self.surname}")

    def get_total_income(self):
        income_position = self._income
        try:
            income = int(income_position.get("wage")) + int(income_position.get("bonus"))
            return income
        except ValueError:
            print("Вы ввели неверные значения!")


position = Position("Имя", "Фамилия", "manager", "вчера", "среда")
position.get_full_name()
print(f"Общий доход сотрудника: {position.get_total_income()} руб.")
