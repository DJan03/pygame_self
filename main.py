import pygame

pygame.init()

window_size = (1280, 720)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("WhiteLight_remake")

world = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
]


class Player:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def move(self, direction):
        dx, dy = direction

        dx *= self.speed
        dy *= self.speed

        newX = self.x + dx
        newY = self.y + dy

        if (
                world[newX // 80][newY // 80] == 0 and
                world[newX // 80][(newY + self.height - 1) // 80] == 0 and
                world[(newX + self.width - 1) // 80][newY // 80] == 0 and
                world[(newX + self.width - 1) // 80][(newY + self.height - 1) // 80] == 0
        ):
            self.x = newX
            self.y = newY

    def draw(self):
        pygame.draw.rect(
            window,
            (125, 255, 40),
            (self.x, self.y, self.width, self.height)
        )


class InputHanlder:
    def __init__(self, actor):
        self.actor = actor

    def update(self, keys):
        if (keys[pygame.K_LEFT]):
            self.actor.move((-1, 0))
        if (keys[pygame.K_RIGHT]):
            self.actor.move((1, 0))
        if (keys[pygame.K_UP]):
            self.actor.move((0, -1))
        if (keys[pygame.K_DOWN]):
            self.actor.move((0, 1))


player = Player(500, 500, 60, 90, 10)
playerInputHandler = InputHanlder(player)

run = True

while (run):
    pygame.time.delay(20)

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = False

    playerInputHandler.update(pygame.key.get_pressed())

    window.fill((0, 0, 0))

    for i in range(len(world)):
        for j in range(len(world[i])):
            if (world[i][j] == 1):
                pygame.draw.rect(window, (255, 0, 0), (i * 80, j * 80, 80, 80))

    player.draw()
    pygame.display.update()

pygame.quit()
