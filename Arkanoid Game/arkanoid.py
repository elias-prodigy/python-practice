import sys, random, pygame


class Paddle(pygame.Rect):

    def __init__(self, velocity, left_key, right_key, *args, **kwargs):
        self.velocity = velocity
        self.left_key = left_key
        self.right_key = right_key
        super().__init__(*args, **kwargs)

    def move_paddle(self, board_width):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[self.left_key]:
            if self.x - self.velocity > 0:
                self.x -= self.velocity

        if keys_pressed[self.right_key]:
            if self.x + self.velocity < board_width - self.width:
                self.x += self.velocity


class Ball(pygame.Rect):
    def __init__(self, velocity, *args, **kwargs):
        self.velocity = velocity
        self.angle = 0
        super().__init__(*args, **kwargs)

    def move_ball(self):
        self.y += self.velocity
        self.x += self.angle


class Arkanoid:
    HEIGHT = 800
    WIDTH = 890
    PADDLE_WIDTH = 100
    PADDLE_HEIGHT = 10
    PADDLE_VELOCITY = 12
    BALL_WIDTH = 10
    BALL_VELOCITY = 7
    BALL_ANGLE = 0
    BRICK_WIDTH = 100
    BRICK_HEIGHT = 50
    STATE_BALL_IN_PADDLE = 0
    STATE_PLAYING = 1
    STATE_WON = 2
    STATE_GAME_OVER = 3
    COLOUR = (255, 0, 0)

    def __init__(self):
        pygame.init()
        self.lives = 3
        self.score = 0
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.font = pygame.font.Font(None, 30)
        self.clock = pygame.time.Clock()
        self.state = self.STATE_BALL_IN_PADDLE

        self.paddles = []
        self.paddles.append(Paddle(self.PADDLE_VELOCITY, pygame.K_LEFT, pygame.K_RIGHT,
                                   self.WIDTH / 2 - self.PADDLE_WIDTH / 2,
                                   self.HEIGHT - self.PADDLE_HEIGHT,
                                   self.PADDLE_WIDTH, self.PADDLE_HEIGHT))

        self.balls = []
        self.balls.append(Ball(self.BALL_VELOCITY, self.WIDTH / 2 - self.BALL_WIDTH / 2,
                               self.HEIGHT - self.PADDLE_HEIGHT * 2,
                               self.BALL_WIDTH, self.BALL_WIDTH))

        self.bricks = []
        y_ofs = 30
        for i in range(4):
            x_ofs = 10
            for j in range(8):
                self.bricks.append(pygame.Rect(x_ofs, y_ofs, self.BRICK_WIDTH, self.BRICK_HEIGHT))
                x_ofs += self.BRICK_WIDTH + 10
            y_ofs += self.BRICK_HEIGHT + 5

    def check_ball_hits_wall(self):
        for ball in self.balls:
            if ball.y > self.HEIGHT:
                self.lives -= 1
                if self.lives > 0:
                    self.state = self.STATE_BALL_IN_PADDLE
                else:
                    self.state = self.STATE_GAME_OVER
                break

            if ball.x > self.WIDTH - self.BALL_WIDTH or ball.x < 0:
                ball.angle = -ball.angle
            elif ball.y < 0:
                ball.velocity = -ball.velocity

    def check_ball_hits_paddle(self):
        for ball in self.balls:
            for paddle in self.paddles:
                if ball.colliderect(paddle):
                    ball.velocity = -ball.velocity
                    ball.angle = random.randint(-10, 10)

    def check_ball_hits_brick(self):
        for ball in self.balls:
            for brick in self.bricks:
                if ball.colliderect(brick):
                    self.score += 3
                    ball.velocity = -ball.velocity
                    self.bricks.remove(brick)
                    break

        if len(self.bricks) == 0:
            self.state = self.STATE_WON

    def show_stats(self):
        if self.font:
            font_surface = self.font.render("SCORE: " + str(self.score) + " LIVES: "
                                            + str(self.lives), False, (255, 255, 255))
            self.screen.blit(font_surface, (self.WIDTH / 2 - 100, 5))

    def show_message(self, message):
        if self.font:
            size = self.font.size(message)
            font_surface = self.font.render(message, False, self.COLOUR)
            x = (self.WIDTH - size[0]) / 2
            y = (self.HEIGHT - size[1]) / 2
            self.screen.blit(font_surface, (x, y))

    def check_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.state == self.STATE_BALL_IN_PADDLE:
            self.state = self.STATE_PLAYING

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

            self.screen.fill((0, 45, 45))
            self.check_input()

            for paddle in self.paddles:
                paddle.move_paddle(self.WIDTH)
                pygame.draw.rect(self.screen, self.COLOUR, paddle)

            for ball in self.balls:
                ball.move_ball()
                pygame.draw.rect(self.screen, self.COLOUR, ball)

            for brick in self.bricks:
                pygame.draw.rect(self.screen, self.COLOUR, brick)

            if self.state == self.STATE_PLAYING:
                self.check_ball_hits_brick()
                self.check_ball_hits_paddle()
                self.check_ball_hits_wall()
            elif self.state == self.STATE_BALL_IN_PADDLE:
                self.balls[0].left = self.paddles[0].left + self.paddles[0].width / 2
                self.balls[0].top = self.paddles[0].top - 2 * self.balls[0].height + 2
                self.show_message("PRESS SPACE TO LAUNCH THE BALL")
            elif self.state == self.STATE_GAME_OVER:
                self.show_message("GAME OVER. PRESS ESC TO EXIT THE GAME")
            elif self.state == self.STATE_WON:
                self.show_message("YOU WON! ESC TO EXIT THE GAME")

            self.show_stats()
            pygame.display.flip()
            self.clock.tick(40)


if __name__ == '__main__':
    arkanoid = Arkanoid()
    arkanoid.game_loop()
