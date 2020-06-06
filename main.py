import pygame
from PIL import Image

pygame.init()

window_size = (1280, 720)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("WhiteLight_remake")


class World:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.room_size_x = 17
        self.room_size_y = 10

        img = Image.open("map.png")
        pixels = img.load()
        x, y = img.size

        self.size = 80

        self.world_map = [[0 for _ in range(y)] for _ in range(x)]
        for i in range(x):
            for j in range(y):
                self.world_map[i][j] = 1 if (pixels[i, j] == (0, 0, 0)) else 0

        self.images = []
        tiles = pygame.transform.scale(pygame.image.load("tiles.png"), (self.size * 2, self.size))
        for i in range(2):
            for j in range(1):
                surf = pygame.Surface((self.size, self.size))
                surf.blit(tiles, (-self.size * i, -self.size * j))
                self.images.append(surf)

    def draw(self):
        x0 = (self.room_size_x - 1) * self.x
        y0 = (self.room_size_y - 1) * self.y
        x1 = (self.room_size_x - 1) * (self.x + 1) + 1
        y1 = (self.room_size_y - 1) * (self.y + 1) + 1
        for i in range(x0, x1):
            for j in range(y0, y1):
                window.blit(self.images[self.world_map[i][j]],
                            ((i - x0) * self.size - self.size // 2,
                             (j - y0) * self.size - self.size // 2)
                            )

    def check_collision(self, x, y, w, h):
        x0 = (x + self.size // 2) // self.size + (self.room_size_x - 1) * self.x
        y0 = (y + self.size // 2) // self.size + (self.room_size_y - 1) * self.y
        x1 = (x + w - 1 + self.size // 2) // self.size + (self.room_size_x - 1) * self.x
        y1 = (y + h - 1 + self.size // 2) // self.size + (self.room_size_y - 1) * self.y

        return (self.world_map[x0][y0] == 0 and self.world_map[x1][y0] == 0 and
                self.world_map[x0][y1] == 0 and self.world_map[x1][y1] == 0)

    def update_visible_room(self, x, y, w, h):
        x0 = x
        y0 = y
        x1 = x + w
        y1 = y + h

        if (x0 < 0):
            self.x -= 1
        if (y0 < 0):
            self.y -= 1
        if (x1 >= window_size[0]):
            self.x += 1
        if (y1 >= window_size[1]):
            self.y += 1


world = World()


class Player:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

        self.maxHealth = 100
        self.health = 100
        self.maxWarm = 100
        self.warm = 100
        self.maxCoins = 3
        self.coins = 3

    def move(self, direction):
        dx, dy = direction

        dx *= self.speed
        dy *= self.speed

        newX = self.x + dx
        newY = self.y + dy

        if (world.check_collision(newX, newY, self.width, self.height)):
            world.update_visible_room(newX, newY, self.width, self.height)
            self.x = newX % (window_size[0] - self.width)
            self.y = newY % (window_size[1] - self.height)

    def draw(self):
        pygame.draw.rect(
            window,
            (125, 255, 40),
            (self.x, self.y, self.width, self.height)
        )

    def draw_parametrs(self):
        pygame.draw.rect(window, (64, 0, 0), (20, 20, 300, 40))
        pygame.draw.rect(
            window, (255, 0, 0),
            (20, 20,
             self.health * 3, 40)
        )

        pygame.draw.rect(window, (0, 0, 64), (20, 70, 200, 20))
        pygame.draw.rect(
            window, (0, 0, 255),
            (20, 70,
             self.warm * 2, 20)
        )

        for i in range(self.maxCoins):
            pygame.draw.rect(window, (64, 64, 0), (240 + i * 30, 70, 20, 20))

        for i in range(self.coins):
            pygame.draw.rect(
                window, (255, 255, 0),
                (240 + i * 30, 70,
                 20, 20)
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
        if (keys[pygame.K_1]):
            self.actor.health -= 1
        if (keys[pygame.K_2]):
            self.actor.warm -= 1
        if (keys[pygame.K_3]):
            self.actor.coins -= 1


player = Player(100, 100, 60, 90, 10)
playerInputHandler = InputHanlder(player)

run = True

while (run):
    pygame.time.delay(20)

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = False

    playerInputHandler.update(pygame.key.get_pressed())

    window.fill((0, 0, 0))

    world.draw()
    player.draw()
    player.draw_parametrs()
    pygame.display.update()

pygame.quit()
