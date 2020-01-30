import random, sys, pygame


class Paddle(pygame.Rect):

    def __init__(self, velocity, up_key, down_key, *args, **kwargs):
        self.velocity = velocity
        self.up_key = up_key
        self.down_key = down_key
        super().__init__(*args, **kwargs)

    def move_paddle(self, board_height):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[self.up_key]:
            if self.y - self.velocity > 0:
                self.y -= self.velocity

        if keys_pressed[self.down_key]:
            if self.y + self.velocity < board_height - self.height:
                self.y += self.velocity


class Ball(pygame.Rect):
    def __init__(self, velocity, *args, **kwargs):
        self.velocity = velocity
        self.angle = 0
        super().__init__(*args, **kwargs)

    def move_ball(self):
        self.x += self.velocity
        self.y += self.angle


class Pong:
    HEIGHT = 1000
    WIDTH = 1700
    PADDLE_WIDTH = 10
    PADDLE_HEIGHT = 100
    PADDLE_VELOCITY = 12
    BALL_WIDTH = 10
    BALL_VELOCITY = 7
    BALL_ANGLE = 0
    COLOUR = (255, 0, 0)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.central_line = pygame.Rect(self.WIDTH / 2, 0, 1, self.HEIGHT)
        self.paddles = []
        self.balls = []
        self.paddles.append(Paddle(self.PADDLE_VELOCITY, pygame.K_w, pygame.K_s,
                                   0, self.HEIGHT / 2 - self.PADDLE_HEIGHT / 2,
                                   self.PADDLE_WIDTH, self.PADDLE_HEIGHT))

        self.paddles.append(Paddle(self.PADDLE_VELOCITY, pygame.K_UP, pygame.K_DOWN,
                                   self.WIDTH - self.PADDLE_WIDTH,
                                   self.HEIGHT / 2 - self.PADDLE_HEIGHT / 2,
                                   self.PADDLE_WIDTH, self.PADDLE_HEIGHT))

        self.balls.append(Ball(self.BALL_VELOCITY, self.WIDTH / 2 - self.BALL_WIDTH / 2,
                               self.HEIGHT / 2 - self.BALL_WIDTH / 2,
                               self.BALL_WIDTH, self.BALL_WIDTH))

    def check_ball_hits_wall(self):
        for ball in self.balls:
            if ball.x > self.WIDTH or ball.x < 0:
                sys.exit(1)

            if ball.y > self.HEIGHT - self.BALL_WIDTH or ball.y < 0:
                ball.angle = -ball.angle

    def check_ball_hits_paddle(self):
        for ball in self.balls:
            for paddle in self.paddles:
                if ball.colliderect(paddle): #метод проверки на столкновение двух прямоугольников
                    ball.velocity = -ball.velocity
                    ball.angle = random.randint(-10, 10)
                    break

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

            self.screen.fill((0, 45, 45)) #команда для перекрашивания поля после каждого цикла
            pygame.draw.rect(self.screen, self.COLOUR, self.central_line)

            for paddle in self.paddles:
                paddle.move_paddle(self.HEIGHT)
                pygame.draw.rect(self.screen, self.COLOUR, paddle)

            for ball in self.balls:
                ball.move_ball()
                pygame.draw.rect(self.screen, self.COLOUR, ball)

            self.check_ball_hits_paddle()
            self.check_ball_hits_wall()

            pygame.display.flip() #фигня которая заставляет пайгейм прорисовывать обьекты
            self.clock.tick(40)


if __name__ == '__main__':
    pong = Pong()
    pong.game_loop()
