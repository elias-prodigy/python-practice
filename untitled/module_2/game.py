import random
from player import Player


class Game:

    def __init__(self):
        self.p1 = Player('Elias')
        self.p2 = Player('Computer')

    def exe(self):
        players = [self.p1, self.p2]
        player = None
        while self.p1.health > 0 and self.p2.health > 0:
            player = random.choice(players)
            player.moves()
            print(self.p1.name, 'HP left', self.p1.health)
            print(self.p2.name, 'HP left', self.p2.health, '\n')
        if self.p1.health > self.p2.health:
            print('Player', self.p1.name, 'has won')
        else:
            print('Player', self.p2.name, 'has won')

