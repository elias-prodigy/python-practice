# Task_1
# Создать класс Фигура. Наследовать от него классы Треугольник, Прямоугольник, Квадрат.
# У каждого класса создать метод для подсчета периметра и площади.
#
# class Figure:
#
#     def __init__(self, l):
#         self.length = 1
#
#     def calc_perimeter(self):
#         pass
#
#     def cals_square(self):
#         pass
#
# class Triangle(Figure):
#
#     def __init__(self, a, b, c, h):
#         self.first_side = a
#         self.second_side = b
#         self.third_side = c
#         self.height = h
#
#     def calc_perimeter(self):
#         return self.first_side + self.second_side + self.third_side
#
#     def cal_square(self):
#         return self.third_side * self.height / 2
#
# class Rectangle(Figure):
#
#     def __init__(self, a, b):
#         self.first_side = a
#         self.second_side = b
#
#     def calc_perimeter(self):
#         return self.first_side * 2 + self.second_side * 2
#
#     def calc_square(self):
#         return self.first_side * self.second_side
#
# class Squre(Figure):
#
#     def __init__(self, a):
#         self.first_side = a
#
#     def calc_perimeter(self):
#         return self.first_side * 4
#
#     def calc_square(self):
#         return self.first_side ** 2
#
# triangle = Triangle(2, 2, 3, 2)
# print(triangle.calc_perimeter())


#  Task_1
#  Создать класс Person с атрибутами имя, фамилия, дата
# рождения. Добавить методы get_age, displayInfo.

class Person:

    def __init__(self, name, surname, birth_year):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year

    def get_age(self):
        from datetime import date
        year = date.today().year
        from _datetime import datetime
        b = datetime.strptime(self.birth_year, '%Y')
        return year - b.year

    def displayinfo(self):
        return self.name + self.surname

person = Person('Ilya', 'Kolohoida', '1990')
print(person.displayinfo())
print(person.get_age())

# Создать класс Ученик наследуя от Person. Создать экземпляры
# этого класса и добавить в ClassRoom. Переопределить метод
# displayInfo.
#
# class Student(Person):

