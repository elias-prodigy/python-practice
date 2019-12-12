import unittest
from lesson_19_module import *


class TestPlayer(unittest.TestCase):

    def test_players_names(self):
        self.player1 = Player('Elias')
        self.player2 = Player('Computer')
        self.assertEqual(self.player1.name, 'Elias')
        self.assertEqual(self.player2.name, 'Computer')

    # def test_small_damage(self):


