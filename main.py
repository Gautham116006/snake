import pygame

from apple import Apple
from snake import Snake

pygame.init()

RESOLUTION = (1280, 720)

surface = pygame.display.set_mode(RESOLUTION)

running = True

snake = Snake(surface)
apple = Apple(surface)

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        # end if

    surface.fill("yellow")
    snake.update_motion()
    apple.spawn_apple()

    pygame.display.flip()

# end while

