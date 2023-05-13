import random

import pygame

from snake import Snake

Snake = Snake()


class Apple:
    """
    class for apple
    """
    APPLE = None

    def __new__(cls, *args, **kwargs):
        if cls.APPLE is None:
            cls.APPLE = super().__new__(cls)
        return cls.APPLE

    def __init__(self, surface=None):
        self.APPLE_SPAWNED = False
        self.APPLE_SIZE = Snake.SNAKE_SIZE
        self.APPLE_X = 0
        self.APPLE_Y = 0
        self.SURFACE = surface
        self.APPLE_RECT = 0

    def get_random_val(self):
        random_val_x = random.randint(Snake.SNAKE_SIZE * 2, 1280 - Snake.SNAKE_SIZE * 2)
        random_val_y = random.randint(Snake.SNAKE_SIZE * 2, 720 - Snake.SNAKE_SIZE * 2)

        if random_val_x and random_val_y is not [Snake.X_POS + Snake.SNAKE_SIZE, Snake.X_POS - Snake.SNAKE_SIZE,
                                                 Snake.Y_POS + Snake.SNAKE_SIZE, Snake.Y_POS - Snake.SNAKE_SIZE]:
            return random_val_x, random_val_y
        return self.get_random_val()

    def spawn_apple(self):
        """
        spawn an apple randomly, also if apple is eaten spawn new apple
        """
        if self.APPLE_SPAWNED is False:
            self.APPLE_X, self.APPLE_Y = self.get_random_val()
            self.APPLE_SPAWNED = True
        # end if

        self.APPLE_RECT = pygame.Rect(self.APPLE_X, self.APPLE_Y, self.APPLE_SIZE, self.APPLE_SIZE)
        pygame.draw.rect(self.SURFACE, "white", self.APPLE_RECT)
        # end if
        if self.APPLE_RECT.colliderect(Snake.SNAKE_HEAD):
            self.APPLE_SPAWNED = False
            self.spawn_apple()
            Snake.grow_snake()
        # end if

    # end def_spawn_apple


