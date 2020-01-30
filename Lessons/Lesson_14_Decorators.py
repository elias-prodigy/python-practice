# Task_1
# Написать декоратор, который будет валидировать входные
# данные (параметры декорируемой функции, например
# разрешить только числа).
# Применить декоратор к функции, которая принимает
# несколько чисел.
# Вызвать декорируемую функцию. (И реализовать как класс)


class Validation:

    def __init__(self, func):
        self.func = func

    def __call__(self, arg):
        if isinstance(arg, int):
            print('Valid')
        else:
            print("Not Valid")
        self.func(arg)


@Validation
def function(num):
    print(num)
