# Task_1
# Объявить словарь, в котором ключом будет permission
# (admin, loggedin, unknown etc) а значениями будут ссылки
# на функции, которые отображают доступный функционал
# данного пользователя. Объявить класс Person, у которого
# есть атрибут (свойство) permission. Создать экземпляры
# класса Person с различными permission и отобразить
# доступный функционал по словарю.


def admin():
    print("You logged in as an admin")
    # return a


def loggedin():
    print("You logged in as a user")
    # return b


def unknown():
    print("You logged in as an unknown user")
    # return c


dictionary = {
    'admin': admin,
    'loggedin': loggedin,
    'unknown': unknown
}


class Person:

    def __init__(self, permission):
        self.permission = permission


abc = input("Who you are: ")
class_object = Person(abc)
b = dictionary[class_object.permission]()

# Task_2
# Пользователь вводить возраст. Написать функцию, если
# возраст больше 16 то объявить внутри функции функцию
# show_available_content, которая будет показывать
# доступные фильмы, вызвать show_available_content которая
# показывает скрытые данные. Если возраст меньше 16,
# вернуть сообщение что пользователю информация недоступна.

def age(a):

    if a > 16:
        def show_available():
            print("You are old")
        show_available()
    else:
        print("You are too young")

b = int(input("How old are you: "))
age(b)
