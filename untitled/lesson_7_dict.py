# Task_1
# Подсчитать количество каждого элемента в списке. Результат в виде словаря

# l = [1, 1, 2, 3, 3, 4]
# addict = {}
# for element in l:
#     if element in addict:
#         addict[element] = addict[element] + 1
#     else:
#         addict[element] = 1
# print(dict)

# Task_2
# Вывести количество четных и нечетных елементов в рандомной последовательности.Результат в виде словаря

# import random
#
# l = random.sample(range(50), 10)
# addict = {'even': 0, 'odd': 0}
# for element in l:
#     if element % 2 == 0:
#         addict['even'] = addict['even'] + 1
#     else:
#         addict['odd'] = addict['odd'] + 1
# print(addict)

# Task_3
# Для каждого слова из данного текста https://ru.lipsum.com/feed/html подсчитайте,
# сколько раз оно встречалось в этом тексте ранее. Результат в виде словаря

l = list('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque a odio massa. Morbi varius, risus sit amet ullamcorper fringilla, mi erat imperdiet orci, vitae pulvinar nisl arcu nec odio. Proin lacinia aliquam elit, et placerat urna vulputate eget. Nunc fermentum, nulla a pharetra iaculis, velit massa tempor velit, interdum consequat enim enim eget justo. Pellentesque porta nisi suscipit tempus efficitur. Donec sed quam eu purus gravida scelerisque. Donec lorem ex, aliquet sed rhoncus vitae, tempor vel dolor. Duis feugiat odio in felis facilisis, id euismod sem vulputate. Nullam et tellus et ipsum scelerisque sagittis. Suspendisse id efficitur tellus. Cras in dolor ac eros porttitor pulvinar nec in nisl. Etiam scelerisque eros sit amet lacinia tempor. In egestas enim sed ex dapibus, nec malesuada ex dapibus.'.split())
print(l)
addict = {}
for elem in l:
    if elem in l:
        addict[elem] = addict[elem] + 1
    else:
        addict[elem] = 1
print(dict)