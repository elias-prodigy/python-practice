import urllib.request
# import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://hard.rozetka.com.ua/videocards/c80087/"
html = urlopen(url)

card_obj = BeautifulSoup(html.read(), features="lxml")


videocards = card_obj.find_all('li')

for videocard in videocards:
    names = videocard.find_all("span")
    pictures = videocard.find_all("img")
    # prices = videocard.find_all
    print(names)
    print(pictures)
