import pygame, sys


class Pong:
    HEIGHT = 800
    WIDTH = 1600

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


if __name__ == '__main__':
    pong = Pong()
    pong.game_loop()
