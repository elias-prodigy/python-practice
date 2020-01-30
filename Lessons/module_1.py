# Task_1
# Число 197 называется круговым простым числом,
# потому что все перестановки его цифр с конца в начало являются простыми числами: 197, 719 и 971.
# Существует тринадцать таких простых чисел меньше 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79 и 97.
# Сколько существует круговых простых чисел меньше миллиона?

def in_set(asd):
    b = set(str(asd))
    return b

set_even = {'0', '2', '4', '5', '6', '8'}
n = input("Введите число до которого надо посчитать круговые простые числа: ")
lst = []
for i in range(2, int(n)+1):
    if is_round()
    if set_even.intersection(in_set(i)) == set():
        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)

with open('module_1.txt', 'w') as f:
    nums = '\n'.join(map(str, lst))
    f.write(nums)
