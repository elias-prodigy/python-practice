# Task_1
# Сгенерировать случайное число с помощью randint и вывести его на экран

import random
a = random.randint(12,56)
print(a)

# Task_2
# Дан список чисел [1,2,3,4,5,6]. Перемешать список с помощью функции random.shuffle и вывести случайное число с помощью random.choice

a = [1, 2, 3, 4, 5, 6]
random.shuffle(a)
print(a)
print(random.choice(a))

# Task_3
# Сгенерировать случайное число с плавающей точкой с помощью random.random() и вывести его на экран

print(random.random())

# Task_3
# Сгенерировать случайное число с плавающей точкой в диапазоне от 0 до 25 с помощью random.uniform и вывести его на экран

print(random.uniform(0, 25))