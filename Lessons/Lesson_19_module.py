# Task
# Необходимо разработать моделирование игры в виде консольного приложения.
# Участниками являются Компьютер и Игрок. Последовательность ходов определяется случайным образом.
# У каждого из игроков должно быть одинаковое количество здоровья (например 100) и выбор (тоже случайным образом) следующего из шагов:
# 1. должен нанести умеренный урон и имеет небольшой диапазон (например, 18-25)
# 2. должен иметь большой диапазон урона (например 10-35)
# 3. должен исцелить в небольшом диапазоне (в таком же как и в пункте 1)
#
# После каждого действия должно быть напечатано сообщение, которое сообщает что происходило и сколько здоровья у Игрока и Компьютера.
# Когда здоровье Компьютера достигает, например 35 % увеличьте его шанс на излечение.
#
# Игра завершается, если у одного из участников здоровье достигло 0.

import random


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


class Player:

    def __init__(self, name):
        self.name = name
        self.health = 100

    def small_damage(self):
        damage = random.randint(18, 25)
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print('Hit', self.name, 'with', damage, 'health points')

    def big_damage(self):
        damage = random.randint(10, 35)
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print('Hit', self.name, 'with', damage, 'health points')

    def healing(self):
        heal = random.randint(18, 25)
        self.health += heal
        if self.health > 100:
            self.health = 100
        print('Heal', self.name, 'with', heal, 'health points')

    def moves(self):
        moves = {'move1': self.small_damage,
                 'move2': self.big_damage,
                 'move3': self.healing
                 }
        move = random.choice(list(moves))
        if self.name == "Computer" and self.health < 35 and move != "move3":
            print("Warning for Computer!")
            moves[random.choice(["move3", "move2"])]()
        else:
            moves[move]()

