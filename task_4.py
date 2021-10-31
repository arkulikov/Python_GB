"""
Реализуйте базовый класс Car.
- у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда);
- опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
- добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
"""
import random


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} поехала!")

    def stop(self):
        print(f"{self.name} остановилась!")

    def turn(self):
        direction = ["повернула налево", "повернула направо", "развернулась"]
        return print(f"{self.name} {random.choice(direction)}")

    def show_speed(self):
        print(f"Скорость автомобиля {self.name}: {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Автомобиль движется с недопустимой скоростью!")
        else:
            print(f"Скорость автомобиля {self.name}: {self.speed}")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Автомобиль движется с недопустимой скоростью!")
        else:
            print(f"Скорость автомобиля {self.name}: {self.speed}")


class PoliceCar(Car):
    pass


car_one = TownCar(75, "green", "Zil")
car_two = SportCar(100, "red", "Ferrari")
car_three = WorkCar(35, "yellow", "Maz")
car_four = PoliceCar(100, "yellow", "Renault", True)

car_one.go()
car_two.go()
car_three.go()
car_four.go()

car_one.show_speed()
car_two.show_speed()
car_three.show_speed()
car_four.show_speed()

car_one.turn()
car_two.turn()
car_three.turn()
car_four.turn()

car_one.stop()
car_two.stop()
car_three.stop()
car_four.stop()
