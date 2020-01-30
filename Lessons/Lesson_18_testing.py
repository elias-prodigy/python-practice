# Task
# Организовать работу библиотеки - выдача книг людям, если книга свободна.
#     Если книга свободна и ее хотят взять: записывать кем книга была взята и
#     когда она будет возвращена ( + 1 месяц от текущей даты)

from datetime import datetime, timedelta
from uuid import uuid4


class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}"


class Book:

    def __init__(self, book, author, file_path):
        self.book = book
        self.author = author
        self.file_path = file_path
        self.id = uuid4()

    @property
    def count_of_lines(self):
        with open(self.file_path) as book:
            lines_in_book = len(book.readlines())
        return lines_in_book


class PersonCard:

    def __init__(self, person, id):
        self.date_of_registration = datetime.now()
        self.person = person
        self.id = id
        self.taken_books = []

    def take_book(self, order):
        self.taken_books.append(order)


class Biblioteck:

    all_books = []
    person_cards = []

    def add_book(self, *args):
        self.all_books.extend(args)

    def is_person_registered(self, person):
        for person_card in self.person_cards:
            if person == person_card.person:
                return True
        return False

    def register_person(self, person):
        new_person_card = PersonCard(person, id=uuid4())
        self.person_cards.append(new_person_card)

    def get_person_card(self, person):
        for card in self.person_cards:
            if person == card.person:
                return card
        else:
            raise Exception("Not exists")

    def get_book(self, person, book):
        if not self.is_person_registered(person):
            self.register_person(person)
        person_card = self.get_person_card(person)

        if book in self.all_books:
            order = {
                "book_name": book,
                "when_was_taken": datetime.now(),
                "expiration_date": datetime.now() + timedelta(days=30)
            }
            person_card.take_book(order)
        else:
            print("Book is not available")

    @property
    def book_count(self):
        return len(self.all_books)

    def show_all_books_info(self):
        pass


# def all_available_books(biblioteck):
#     # Сделать с помощью списковых включений
#     available_books = []
#     taken_books = []
#
#     for person_books in biblioteck["person_cards"]:
#         for person_book in person_books["taken_books"]:
#             taken_books.append(person_book["book_name"])
#
#     for book in books:
#         if book["name"] not in taken_books:
#             available_books.append(book["name"])
#     return available_books
#
#
# def add_book(biblioteck, book):
#     # добавить книгу в библиотеку
#     biblioteck["available_books"].append(book)
#
#
# def get_book_back(biblioteck, person, book_name):
#     # вернуть книгу обратно в библиотеку
#     person_card = get_person_card(biblioteck, person)
#     for book in person_card["taken_books"]:
#         if book["book_name"] == book_name:
#             person_card["taken_books"].remove(book_name)