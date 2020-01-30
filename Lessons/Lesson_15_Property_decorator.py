# Task_1
# Написать класс Distance с приватным атрибутом _distance
# (в метрах). Объявить для этого атрибута setter, getter,
# deleter, который будет показывать дистанцию в метрах.
# Создать вычисляемый атрибут для перевода дистанции в шаги
# (in_feet, 1м = 0.67 шагов)


class Distance:

    def __init__(self, distance):
        self._distance = distance

    @property
    def dist(self):
        return self._distance / 0.67

    @dist.setter
    def dist(self, distance):
        self._distance = distance

    @dist.deleter
    def dist(self):
        del self._distance


my_way = Distance(10)
print(my_way.dist)
my_way.dist = 20
print(my_way.dist)
# del my_way.dist
print(my_way.dist)

# Task_2
# Написать класс Wallet с приватными атрибутами класса:
# dollars, cents. Написать setter, deleter, getter для
# cents и вычисляемый атрибут для общего количества денег.


class Wallet:

    def __init__(self, dollars, cents):
        self._dollars = dollars
        self._cents = cents

    @property
    def coins(self):
        return self._dollars + self._cents // 100 + (self._cents % 100)/100

    @coins.setter
    def coins(self, value):
        dollars, cents = value[0], value[1]
        self._dollars = dollars
        self._cents = cents

    @coins.deleter
    def coins(self):
        del self._dollars
        del self._cents


my_wallet = Wallet(2, 35)
print(my_wallet.coins)
my_wallet.coins = (2, 35)
print(my_wallet.coins)

# Task_3
# Создать класс Celcius с приватным атрибутом _temperature.
# Объявить для этого атрибута setter, getter, deleter.
# Создать вычисляемый атрибут для перевода по фаренгейту.


class Celsius:

    def __init__(self, temperature):
        self._temperature = temperature

    @property
    def cels(self):
        return self._temperature / 0.38

    @cels.setter
    def cels(self, temperature):
        self._temperature = temperature

    @cels.deleter
    def cels(self):
        del self._temperature


my_temp = Celsius(38)
print(my_temp.cels)
my_temp.cels = 38
print(my_temp.cels)

# Task_4
# Создать класс USDCurrencyConverter, с приватным атрибутом
# current_value (в USD) и вычисляемыми атрибутами для
# перевода из USD в другие валюты, например EUR, UAH.

class USDCurrencyConverter:

    def __init__(self, current_value):
        self._current_value = current_value

    @property
    def uah(self):
        return self._current_value * 25

    @uah.setter
    def uah(self, current_value):
        self._current_value = current_value

    @uah.deleter
    def uah(self):
        del self._current_value

    @property
    def eur(self):
        return self._current_value * 1.1

    @eur.setter
    def eur(self, current_value):
        self._current_value = current_value

    @eur.deleter
    def eur(self):
        del self._current_value


my_currency = USDCurrencyConverter(30)
print(my_currency.uah)
print(my_currency.eur)

# Task_5
# Создать класс Карта с атрибутами значение и масть,
# перегрузить методы __lt__, __gt__, __eq__ для сравнения
# карт

class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __eq__(self, other):
        if self.value == other.value and self.suit == other.suit:
            print("both objects are equal")
            return True
        else:
            print("both objects are not equal")
            return False

    def __lt__(self, other):
        if self.value < other.value and self.suit < other.suit:
            print("both objects are less")
            return True
        else:
            print("both objects are greater <lt>")
            return False

    def __gt__(self, other):
        if self.value > other.value and self.suit > other.suit:
            print("both objects are greater")
            return True
        else:
            print("both objects are less <gt>")
            return False

my_cards = Card()


# Task_6
# Создать иерархию наследования классов: место (локация),
# город, область, мегаполис

class Location:

    def __init__(self, place, coordinates):
        self.place = place
        self.coordinates = coordinates

    def __str__(self):
        return f"{self.place} {self.coordinates}"


class Region(Location):

    def __init__(self, place, coordinates, region_name, list_of_cities):
        super().__init__(place, coordinates)
        self.list_of_cities = list_of_cities
        self.region_name = region_name

    def __str__(self):
        return f"{self.place} {self.coordinates} {self.region_name}"

    @property
    def dist(self):
        return [city.city_name for city in self.list_of_cities]


class Megapolis(Location):

    def __init__(self, place, coordinates, megapolis_name):
        super().__init__(place, coordinates)
        self.megapolis_name = megapolis_name

    def __str__(self):
        return f"{self.place} {self.coordinates} {self.megapolis_name}"


class City(Location):

    def __init__(self, place, coordinates, city_name):
        super().__init__(place, coordinates)
        self.city_name = city_name

    def __str__(self):
        return f"{self.place} {self.coordinates} {self.city_name}"


city1 = City("В черном черном месте", "на краю географии стоит", "New York")
city2 = City("В черном черном месте", "на краю географии стоит", "Moscow")
location4 = Region("В черном черном месте", "на краю географии", "находится город Запирожье", [city1, city2])

print(str(location4))
print(location4.dist)

# Task_7
# Создать иерархию наследования классов: Человек, Мужчина,
# Женщина,
# Супермен (с приватным атрибутом force и методом
# save_world)

from datetime import datetime


class Human:

    def __init__(self, name, surname, date_of_birth):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f"Human({self.name} {self.surname} {self.date_of_birth})"


class Men(Human):

    def __init__(self, name, surname, date_of_birth, hair_type, hair_color):
        super().__init__(name, surname, date_of_birth)
        self.hair_type = hair_type
        self.hair_color = hair_color

    def __str__(self):
        return f"Men({self.name} {self.surname} {self.date_of_birth} {self.hair_type} {self.hair_color})"

