import pygame

pygame.init()
BALL_RADIUS = 2
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 70
WIN_WIDTH, WIN_HEIGHT = 1000, 500
BALL_VELO = 3
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
BLACK = (255, 255, 255)
WHITE = (0, 0, 0)


class ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = BALL_RADIUS
        self.isRight = True
        self.isUp = True

    def move(self):
        if self.y <= 0:
            self.isUp = False
        if self.y >= WIN_HEIGHT:
            self.isUp = True

        if self.x <= 0:
            self.isRight = True
        if self.x >= WIN_WIDTH:
            self.isRight = False

        if self.isRight:
            self.x += BALL_VELO
        else:
            self.x -= BALL_VELO

        if self.isUp:
            self.y -= BALL_VELO
        else:
            self.y += BALL_VELO
    def draw(self):
        pygame.draw.circle(WIN, BLACK, (self.x, self.y), BALL_RADIUS)

    def updateBall(self):
        self.move()
        self.draw()


class paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT

    def draw(self):
        pygame.draw.rect(WIN, BLACK, (self.x, self.y, PADDLE_WIDTH, PADDLE_HEIGHT))

    def updatePaddle(self):
        self.draw()


paddle_left = paddle(10, WIN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
paddle_right = paddle(WIN_WIDTH - PADDLE_WIDTH - 10, WIN_HEIGHT // 2 - PADDLE_HEIGHT // 2)

mainBall = ball(250, 500)


def gameLoop():
    mainBall.updateBall()
    paddle_left.updatePaddle()
    paddle_right.updatePaddle()
    pass


def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        gameLoop()
        pygame.display.update()
        WIN.fill(WHITE)
    pygame.quit()


main()
