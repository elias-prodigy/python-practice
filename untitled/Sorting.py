import random

sortinglist = [3, 0, 1, 8, 7, 2, 5, 4, 6, 9]

for element in sortinglist:
    for element1 in sortinglist:
        print(element, "element")
        print(element1, "element1")
        print("______________")
        if element < element1:
            index = sortinglist.index(element)
            index1 = sortinglist.index(element1)
            sortinglist[index], sortinglist[index1] = sortinglist[index1], sortinglist[index]
            element, element1 = element1, element
            print(sortinglist)
            # print(index+1, "- ый проход цикла - ", end=" ")
            # print(sortinglist)
print(sortinglist)

sortinglist1 = [3, 0, 1, 8, 7, 2, 5, 4, 6, 9]
n = len(sortinglist1)
for j in range(0, n-1):
    for i in range(0, n-j-1):
        if sortinglist1[i] > sortinglist1[i+1]:
            sortinglist1[i], sortinglist1[i + 1] = sortinglist1[i + 1], sortinglist1[i]
    print(j+1, "- ый проход цикла - ", end=" ")
    print(sortinglist1)
print(sortinglist1)

