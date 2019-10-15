# Task_1
# Написать функцию, которая будет принимать температуру по
# цельсию и возвращать ее перевод в температуру по
# фаренгейту по формуле: (temp - 32) * (5/9)

# def f(a): return (a * 9 / 5) + 32
# print(f(60))

# Task_2
#  Написать функцию поиска минимума в произвольном
# количестве элементов переданных в функцию

# def f(*args):
#     minimum = args[0]
#     for item in args:
#         if item < minimum:
#             minimum = item
#
#     return minimum
#
# print(f(2,2,3,4,5,6,1))

# Task_3
# Написать функцию которая принимает два аргумента: первый
# аргумент отвечает за выбор пользователя: минимум или
# максимум, второй аргумент - список элементов в котором
# нужно найти минимум или максимум

# def min_func(l):
#     minimum = l[0]
#     for item in l:
#         if item < minimum:
#             minimum = item
#     return minimum
#
# def max_func(l):
#     maximum = l[0]
#     for item in l:
#         if item > maximum:
#             maximum = item
#     return maximum
#
# actions = {
#     "min": min_func,
#     "max": max_func
# }
#
# user = input('Choose min or max: ')
#
# print(actions[user]([1, 2, 0, 5, -2, -1, 25]))

# Task_4
# Написать функцию пересечения и функцию объединения
# неограниченного количества последовательностей

