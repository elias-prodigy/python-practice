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

list_3 = random.sample(range(50), 39)
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

list_6 = set()
b = 0
while b < len(list_4):
    if list_4[b] in list_6:
        print('Yes')
    else:
        print('No')
    list_6.add(list_4[b])
    b += 1

# Task_4
# Написать функцию, которая будет принимать пароль.
# Если в пароле есть 1 большая буква и хотя бы 5 цифр, и его длина не менее 10 символов вывести: “Your password is strong.”
# в противном случае “Your password is not strong enough.”

l = input('Please enter the password (not less than 10 characters): ')
counter_char = 0
counter_number = 0
if len(l) < 10:
    print('Your password is not strong enough.')
else:
    for char in l:
        if char.isupper():
            counter_char += 1
        elif char.isdigit():
            counter_number += 1
    if counter_char > 0 and counter_number >= 5:
        print('Your password is strong.')
    else:
        print('Your password is not strong enough.')



# Task_5
# Посчитать факториал для введенного пользователем числа.

x = int(input('Введите число: '))
a = 1
while x > 0:
    a = a * x
    x = x - 1
print(a)

# Task_6
# С помощью random сгенерировать 2 целых числа и спросить у пользователя ответ суммы этих чисел.
# Если пользователь посчитал верно то засчитать ему одно очко. Повторять пока пользователь не введет ‘q’.

import random
r = list(random.sample(range(10), 2))
print(r)
l = input('Введите сумму этих чисел: ')
a = 0
b = sum(r)
for l  q:
    if l == b:
        a += 1


