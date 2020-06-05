import pygame

pygame.init()

window_size = (1280, 720)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("WhiteLight_remake")

ROOM_EMPTY = 1
ROOM_X = 2

room_lib = {
    ROOM_EMPTY: [
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    ROOM_X: [
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
}


class World:
    def __init__(self):
        self.rooms = [
            [None, None, None],
            [room_lib[ROOM_EMPTY], room_lib[ROOM_X], room_lib[ROOM_EMPTY]],
            [None, room_lib[ROOM_X], None]
        ]
        self.x = 1
        self.y = 1

        self.size = 80

    def get_room(self):
        return self.rooms[self.x][self.y]

    def is_collised(self, x, y, w, h):
        x0 = x // 80
        y0 = y // 80
        x1 = (x + w - 1) // 80
        y1 = (y + h - 1) // 80

        room = self.rooms[self.x][self.y]
        return (room[x0][y0] == 0 and room[x1][y0] == 0 and
                room[x0][y1] == 0 and room[x1][y1] == 0)

    def draw(self):
        room = list(self.rooms[self.x][self.y])

        for i in range(len(room)):
            for j in range(len(room[0])):
                if (room[i][j] == 1):
                    pygame.draw.rect(window, (255, 0, 0), (i * self.size, j * self.size, self.size, self.size))


world = World()


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

        if (world.is_collised(newX, newY, self.width, self.height)):
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

    world.draw()
    player.draw()
    pygame.display.update()

pygame.quit()
