import unittest
from lesson_18_testing import *
from unittest.mock import patch, mock_open, Mock


class TestPerson(unittest.TestCase):

    def test_create_person(self):
        vasia = Person("Vasia", 'Petrov')
        self.assertEqual(vasia.name, 'Vasia')
        self.assertEqual(vasia.surname, 'Petrov')

    def test_magic_str(self):
        vasia = Person('Vasia', "Petrov")
        self.assertEqual(str(vasia), "Vasia Petrov")


class TestBook(unittest.TestCase):

    def test_create_book(self):
        book = Book("Storm", "Lenon", "/sum_path")
        self.assertEqual(book.book, "Storm")
        self.assertEqual(book.author, "Lenon")
        self.assertEqual(book.file_path, "/sum_path")
        self.assertIsNotNone(book.id)

    # @patch("library_test.test", mock_open(read_data='\n'))
    # def test_readabiliti(self):
    #     book = Book("Storm", "Lenon", "/sum_path")
    #     assert book.count_of_lines == 1


class TestBiblioteck(unittest.TestCase):
    def setUp(self):
        self.library = Biblioteck()
        self.person = Person("Vasia", "Petrov")
        self.book = Book("Storm", "Lenon", "/sum_path")

    def test_is_person_registered(self):
        # self.library.person_cards.append(PersonCard(self.person, id=uuid4()))
        self.library.person_cards.append(Mock(person=self.person))
        is_reg = self.library.is_person_registered(self.person)
        self.assertTrue(is_reg)
        self.library.person_cards.clear()

    def test_is_person_not_registered(self):
        is_not_reg = self.library.is_person_registered(self.person)
        self.assertFalse(is_not_reg)

    @patch('lesson_18_testing.uuid4')
    def test_register_person(self, mock_uuid):
        mock_uuid.return_value = 123456
        self.library.register_person(self.person)
        self.assertEqual(self.library.person_cards[0].id, 123456)

    def test_get_person_card(self):
        self.library.person_cards.append(Mock(person=self.person))
        get_per_card = self.library.get_person_card(self.person)
        self.assertEqual(get_per_card.person, self.person)
        self.library.person_cards.clear()

    def test_dont_get_person_card(self):
        with self.assertRaises(Exception):
            self.library.get_person_card(self.person)

    @patch('lesson_18_testing.Biblioteck.is_person_registered')
    def test_get_book(self, mock_ipr):
        mock_ipr.return_value = False
        self.library.get_book(self.person, self.book)
        mock_ipr.assert_called()
        self.library.person_cards.clear()


if __name__ == "__main__":
    unittest.main()
