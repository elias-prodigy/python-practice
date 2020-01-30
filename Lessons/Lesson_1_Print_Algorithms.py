name = 'Elias'
day = 'Wednesday'
print('Good day ' + name + '! ' + day + ' is a perfect day to learn some python.')

name = 'Elias'
surname = 'Kolohoida'
print('Hello ' + name + ' ' + surname)

a = 8
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a ** b)

# Задание1
# Выполнить вычисления, записать в переменную и вывести в результате целую часть и дробную часть от деления

a = 15
b = 20
c = 2
d = 5.5
f = 6
e = (a ** c - b + d) // f
g = (a ** c - b + d) % f
print('Task_1:  ', e, g)

# Задание 2
# Записать процесс вычисления в функцию, вызвать эту функцию с параметрами
def calculation(a, b, c, d, f):
    e = (a ** c - b + d) // f
    g = (a ** c - b + d) % f
    print('Task_2:  ', e, g)

calculation(15, 20, 2, 5.5, 6)

# Задание 3
# Написать функцию, которая будет принимать номер телефона и выводить его в формате +38 (099) 123 - 12 - 12

string1 = "%s %s %s %s %s %s %s" % ('+38', '(099)', '123', '-', '12', '-', '12')
string2 = '{0} {1} {2} {3} {4} {5} {6}'.format('+38', '(099)', '123', '-', '12', '-', '12')

code1 = "+38"
string3 = f"{code1} {'(099)'} {123} - {12} - {12}"
print(string1)
print(string2)
print(string3)

# Задание 4
# Написать функцию, которая будет принимать параметры: ФИО, дата рождения и выводит информацию о возрасте в следующем формате: “Age for Фамилия Имя Отчество: 30 years”

def phrase(arg_1, arg_2):
    result = 'Age for ' + arg_1 + ' : ' + arg_2
    print('Task_4:  ', result)

phrase('Kolohoida Elias', '29 years')

# Задание 5
# Найти в тексте https://ru.lipsum.com/feed/html подстроку “Sed”

sed_full_text = """Sed nec iaculis augue. Nunc vel sodales sem. Nam ut lacinia nunc, vitae scelerisque quam. 
 Donec viverra lorem eget imperdiet sollicitudin. Ut posuere lacus at ante consequat bibendum. Morbi malesuada 
 convallis est, id viverra risus laoreet sed. Sed magna purus, lacinia at ullamcorper vitae, malesuada tincidunt augue.

Sed fermentum tortor sit amet mattis imperdiet. Nam varius mi id faucibus facilisis. In laoreet aliquet porta. 
Praesent faucibus risus eget lacus euismod, sit amet ultrices purus ultrices. Suspendisse sed sagittis tellus. 
Morbi tempor venenatis nulla at ornare. Nunc sodales, eros a sodales placerat, justo ipsum commodo lacus,
 eu viverra libero mauris nec diam. Nunc pellentesque placerat vestibulum. Sed sed ligula nec purus gravida 
 lobortis non sed leo. Sed et nibh fringilla, imperdiet orci sit amet, venenatis dui. Morbi tempor nisi dui,
  non cursus enim euismod et. Sed commodo varius leo, nec tincidunt odio pellentesque sit amet.
   Aenean euismod eros vel diam tincidunt ornare."""
print('Task_5:  ',sed_full_text.find('sed'))

# Задание 6
# Вывести первые 10 символов в строке

string = 'I love pineapples'
print('Task_6:  ', string[0:10])

# Задание 7
# Вывести последние 25 символов в строке

string = 'I love pineapples very much'
print('Task_7:  ', string[-25:len(string)])

# Задание 8
# Вывести строку “HELLO WORLD” в нижнем регистре

string = 'HELLO WORLD'
print('Task_8:  ', string.lower())

# Задание 9
# Вставить слова: ”I like {fruit} and {vegetables}”

string = 'I love {0} and {1}'.format('fruits', 'vegetables')
print('Task_9:  ', string)

# Задание 10
# "length - {}, width - {}, height - {}"

string = 'length - {0}, width - {1}, height - {2}'.format('12', '13', '14')
print('Task_10:  ', string)

# Задание 11
# Заменить слова Yes на No в строке: “Do you like summer? - Yes”

string = 'Do you like summer? - {Yes}'.format(Yes='No')
print('Task_11:  ', string)

# Задание 12
# "This is a {subj}. It's {prop}."

string = "This is a {0}. It's {1}.".format('subj', 'prop')
print('Task_12:  ', string)

# Задание 13
# Убрать пробелы в строке “    Hello world!    ”

string = "    Hello world!    "
print('Task_13:  ', string[4:-4])

# Задание 14
# Заменить в строке строчные буквы прописными, а прописные – строчными: “gOOD nIghT EVEryoNE!”

string = 'gOOD nIghT EVEryoNE!'
print('Task_14:  ', string.swapcase())

# Задание 15
# Есть две строки “Yes” и “No” преобразовать их в одну: “NoNoYesYesYes”

string1 = 'Yes'
string2 = 'No'

print('Task_15:  ', string2 * 2 + string1 * 3)

# Задание 16
# Вывести количество символов ‘a’ в строке “Abracadabra” в нижнем регистре

string = 'Abracadabra'
print('Task_16:  ', string.count('a'))