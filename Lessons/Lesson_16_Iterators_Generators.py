# Task_1
# Создать класс Карта с свойствами масть и значение.
# Создать класс Колода, которая будет итератором для
# экземпляров класса Карт.


class Card:

    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    def __str__(self):
        return f"{self._suit} {self._value}"


class CardIterator:
    def __init__(self, collections, cursor1):
        self._collections = collections
        self.cursor = cursor1

    def __next__(self):
        if self.cursor + 1 >= len(self._collections):
            raise StopIteration()
        self.cursor += 1
        return self._collections[self.cursor]


class Deck:

    def __init__(self, collections):
        self._collections = collections

    def __iter__(self):
        return CardIterator(self._collections, -1)


cards = (Card("Ace", "Spades"), Card("King", "Spades"), Card("Queen", "Spades"))
deck = Deck(cards)

for card in deck:
    print(card)

