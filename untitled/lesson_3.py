# Task_1

def sum(a, b):
    c = a + b
    print (c)
    if c > 10:
        print(f"This sum is greater than 10. It’s {c}")
    elif c < 10:
        print(f"This sum is less than 10. It’s {c}")
sum(12, 7)

# Task_2

def password(a):
    b = len(a)
    if b > 10:
        print("Your password is strong.")
    elif b < 10:
        print("Your password is not strong enough.")
password('abracada')

# Task_3

def squirrels(a, is_summer):
    if (a >= 60 and a <= 100) and is_summer:
        print("playing")
    elif (a >= 60 and a <= 90) and not is_summer:
        print("playing")
    else:
        print('not playing')
squirrels(89, False)