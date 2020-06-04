import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Cubes Game")

x = 50
y = 440
width = 40
height = 60
speed = 5

isJump = False
jumpCount = 10

run = True

while (run):
    pygame.time.delay(20)

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = False

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] and x > 0):
        x -= speed
    if (keys[pygame.K_RIGHT] and x < 500 - width):
        x += speed
    if (not (isJump)):
        if (keys[pygame.K_UP] and y > 0):
            y -= speed
        if (keys[pygame.K_DOWN] and y < 500 - height):
            y += speed
        if (keys[pygame.K_SPACE]):
            isJump = True
    else:
        if (jumpCount >= -10):
            if (jumpCount < 0):
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2

            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (125, 255, 90), (x, y, width, height))
    pygame.display.update()

pygame.quit()
