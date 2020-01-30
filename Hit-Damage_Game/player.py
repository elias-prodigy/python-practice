import random


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
