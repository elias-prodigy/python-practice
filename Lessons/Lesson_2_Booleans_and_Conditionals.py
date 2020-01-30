# Task_1
# Написать функцию, которая будет считать и возвращать сумму
# двух чисел. Если сумма больше 10 - вывести на экран “This
# sum is greater than 10. It’s {sum}”, если меньше - “This sum
# is less than 10. It’s {sum}”

def sum(a, b):
    c = a + b
    print (c)
    if c > 10:
        print(f"This sum is greater than 10. It’s {c}")
    elif c < 10:
        print(f"This sum is less than 10. It’s {c}")
sum(12, 7)

# Task_2
# Написать функцию, которая будет принимать пароль. Если его
# длина не менее 10 символов вывести: “Your password is
# strong.” в противном случае “Your password is not strong
# enough.”

def password(a):
    b = len(a)
    if b > 10:
        print("Your password is strong.")
    elif b < 10:
        print("Your password is not strong enough.")
password('abracada')

# Task_3
# Белки проводят большую часть дня, играя. В частности, они
# играют, если температура составляет от 60 до 90
# (включительно). Если лето, то верхний предел температуры
# равен 100 вместо 90. Напишите функцию, которая принимает
# температуру int и логическое значение is_summer, верните...

def squirrels(a, is_summer):
    if (a >= 60 and a <= 100) and is_summer:
        print("playing")
    elif (a >= 60 and a <= 90) and not is_summer:
        print("playing")
    else:
        print('not playing')
squirrels(89, False)