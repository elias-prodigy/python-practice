list_1 = list(range(1, 7, 6)) + list(range(7, 101, 7))
list_2 = list(range(1, 5, 4)) + list(range(5, 101, 5))
list_3 = list(set(list_1) - set(list_2))
print(sorted(list_3))

# Practice
# Task 1
#Дан список чисел L. Написать функцию, которая вернет True если сумма первых 4 элементов списка равны 9.
# При этом функция должна вызываться только если длина списка больше 4.

List = list(input("Введите список: ").split())
L = sum(map(int, List))
L1 = len(List)
if L == 9 and L1 > 4:
    print(True)
else:
    print(False)
