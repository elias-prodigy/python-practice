import random
# Task_1
# Создать файл nums.txt с рандомными цифрами и нужно среди
# них найти самую большую цифру и написать его уже в новый
# max_num.txt файл
# import random

f = open('nums.txt', 'w+')
a = ','.join(map(str, random.sample(range(50), 10)))
f.write(a)
f.close()

f = open('nums.txt', 'r')
nums = f.read()
l = str(max(map(int, nums.split(','))))
f.close()

f1 = open('max_nums.txt', 'w+')
f1.write(l)
f1.close()

# Task_2
# Создайте файл nums.txt, содержащий несколько чисел,
# записанных через пробел. Напишите программу, которая
# подсчитывает и выводит на экран общую сумму чисел,
# хранящихся в этом файле.

with open('nums.txt', 'w+') as f:
    nums = ' '.join(map(str, random.sample(range(50), 3)))
    f.write(nums)
    print(nums)

with open('nums.txt', 'r') as f:
    a = f.read()
    s = str(sum(map(int, a.split())))
    print(s)

# Task_3
# Посчитать количество строк в файле и количество слов и
# символов в каждой строке https://ru.lipsum.com/feed/html

with open('nums.txt', 'w+') as f:
    line = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n" \
           "Duis nec dictum elit. Morbi mollis, sapien ac maximus aliquam, libero ex iaculis diam, id accumsan turpis ligula in ipsum.\n" \
           "Curabitur eget ligula feugiat dolor congue tristique. Aliquam in tellus quis ipsum varius tincidunt id finibus ex.\n" \
           "Pellentesque tincidunt vitae tellus nec ornare. Quisque ex nunc, mollis quis massa at, malesuada accumsan sem.\n" \
           "Aliquam nec velit consequat tortor facilisis imperdiet sit amet ac eros. Proin non mauris turpis.\n" \
           "Aenean ut mi at velit lobortis laoreet ut id sapien. Nam risus magna, blandit non libero at, malesuada dapibus turpis.\n" \
           "Nunc fringilla, dui eu placerat luctus, ante nulla cursus ante, eget volutpat ex ex id diam. Integer mattis nunc nec nunc imperdiet,\n" \
           "ac semper nisi facilisis. Aenean vitae sagittis dolor. Mauris at enim accumsan, cursus tortor eu, sagittis risus. Etiam urna justo,\n" \
           "eleifend vitae massa vel, egestas malesuada ligula."
    f.write(line)
#
# # один из способов вывести кол-во строк в файле
num_of_lines = sum(1 for line in open('nums.txt'))
#
# # решение задачи
with open('nums.txt') as f:
    lines = 0
    words = 0
    characters = 0
    for line in f:
        wordslist = line.split()
        lines += 1
        words = words + len(wordslist)
        characters += sum(len(word) for word in wordslist)
print('Кол-во строк: ', lines)
print('Кол-во слов: ', words)
print('Кол-во символов: ', characters)

# Task_4
# Создать текстовый файл, записать в него построчно данные,
# которые вводит пользователь. Окончанием ввода пусть
# служит пустая строка.

# with open('textfile.txt', 'w+') as f:
#     lines = []
#     while True:
#         line = input('Введите данные построчно: ')
#         if line.strip() == "":
#             break
#         b = lines.append(line)
#         a = ','.join(map(str, ))
#         print(a)
#         f.write(a)
