# Task_1
# Посчитать количество 9 в списке.

list_1 = [1, 2, 9, 4, 9, 5, 7, 9]
i = 0
count = 0
while i < len(list_1):
    if list_1[i] == 9:
        count += 1
    i += 1
print('Task_1 with while: ', count)

list_2 = [1, 2, 9, 4, 9, 5, 7, 9]
b = 0
for a in list_2:
    if a == 9:
        b += 1
print('Task_1 with for: ', b)

# Task_2
# Вывести количество четный и нечетных елементов в рандомной последовательности.

import random

list_3 = random.sample(range(50), 40)
Chet = 0
Nechet = 0
for x in list_3:
    if x % 2 == 0:
        Chet += 1
    else:
        Nechet += 1
print('Task_2 Нечетные: ', Nechet)
print('Task_2 Четные: ', Chet)

# Task_3
# Пользователь должен ввести последовательность чисел через пробел.
# Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.

list_4 = list(input('Введите последовательность чисел через пробел: ').split())
list_5 = set()
a = 0
for a in list_4:
    if a in list_5:
        print('Yes')
    else:
        print('No')
    list_5.add(a)

# while a < len(list_4):
#     if a in list_4:
#         print('Yes')
#
#     else:
# # while b < len(list_4):
# #     if list_4[b] != list_4[b]:
#         print('No')
#     a += 1
#


