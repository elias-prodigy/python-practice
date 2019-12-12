# Task_1
# Создать классы с методами __str__, __repr__ и собственными методами
# классов, построить правильную иерархию классов. Перечень классов:
# Студент, Преподаватель Персона, Зав. кафедрой.

from datetime import datetime


class Person:

    def __init__(self, name, surname, date_of_birth):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __repr__(self):
        return f"Person({self.name} {self.surname} {self.date_of_birth})"


person1 = Person("Ivan", "Ivanov", datetime.now(),)
print(str(person1))
print(repr(person1))


class Zavkaf(Person):

    def __init__(self, name, surname, date_of_birth, kaf_name, position):
        super().__init__(name, surname, date_of_birth)
        self.kaf_name = kaf_name
        self.position = position

    def __str__(self):
        return f"{self.kaf_name} {self.position}"

    def __repr__(self):
        person_repr = super().__repr__()
        return f"Zavkaf({person_repr} {self.kaf_name} {self.position})"


person2 = Zavkaf("Ilya", "Kolohoida", datetime.now(), "Electric apparatuses", "ZavKaf")
print(str(person2))
print(repr(person2))


class Teacher(Zavkaf):

    def __init__(self, name, surname, position, money, kaf_name):
        super(Zavkaf, self).__init__(name, surname, datetime.now())
        super(Teacher, self).__init__(kaf_name, position)
        self.money = money

    def __str__(self):
        return f"{self.name} {self.surname} {self.position} {self.money}"

    def __repr__(self):
        return f"Teacher({self.name} {self.surname} {self.position} {self.money})"


person3 = Teacher("Вася", "Пупкин", "работает преподом", "и получает копейки", "")
print(str(person3))
print(repr(person3))


class Student(Person):

    def __init__(self, **kwargs):
        self.position = kwargs.pop("position")
        self.money = kwargs.pop("money")
        super().__init__(**kwargs)

    def __str__(self):
        person_str = super().__str__()
        return f"{person_str}, {self.position} {self.money}"


person4 = Student(name = "Кульбит", surname = "Пробит", date_of_birth = datetime.now(), position = "не работает - но учится", money = "и не получает ничего")
print(str(person4))

# Автомобиль, Поезд, Транспортное средство, Мотоцикл

# class Vehicle:
#
#     def __init__(self, manufacture_year, speed, cost):
#         self.manufacture_year = manufacture_year
#         self.speed = speed
#         self.cost = cost
#
#     def __str__(self):
#         return f"{self.manufacture_year} {self.speed} {self.cost}"
#
#
# vehicle1 = Vehicle(1990, 32, 12)
# print(vehicle1)
#
#
# class Train(Vehicle)
