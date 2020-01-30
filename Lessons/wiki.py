import wikipedia

my_request = input("Enter request ")
page = wikipedia.search(my_request)
value = 1
for i in page:
    print(str(value), " ", i)
    value += 1
lop = page[int(input("Your choice "))-1]
oop = wikipedia.page(lop)
links = oop.links
value2 = 1
while j in links and value2 <= 7:
    print(str(value2), " ", j)
    value2 += 1

# try:
#     oop = wikipedia.summary(page[int(input("Your choice "))-1])
# except wikipedia.exceptions.DisambiguationError as e:
#     print(e.options)
