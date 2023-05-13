import pygame


class Snake:
    """
    methods for updating motion of the snake
    """
    SNAKE = None

    def __new__(cls, *args, **kwargs):
        if cls.SNAKE is None:
            cls.SNAKE = super().__new__(cls)
        return cls.SNAKE

    def __init__(self, surface=None):
        self.MOVING_LEFT = False
        self.MOVING_RIGHT = False
        self.MOVING_UP = False
        self.MOVING_DOWN = False
        self.X_POS = 1280 / 2
        self.Y_POS = 720 / 2
        self.SNAKE_SIZE = 12
        self.SNAKE_SPEED = 0.5
        self.SURFACE = surface
        self.SNAKE_HEAD = None
        self.SNAKE_BODY = []

    def update_motion(self):
        """
        Update x and y position for snake based on key press
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.MOVING_RIGHT = False
            self.MOVING_DOWN = False
            self.MOVING_UP = False
            self.MOVING_LEFT = True
        # end if

        if keys[pygame.K_RIGHT]:
            self.MOVING_LEFT = False
            self.MOVING_DOWN = False
            self.MOVING_UP = False
            self.MOVING_RIGHT = True
        # end if

        if keys[pygame.K_UP]:
            self.MOVING_LEFT = False
            self.MOVING_RIGHT = False
            self.MOVING_DOWN = False
            self.MOVING_UP = True

        if keys[pygame.K_DOWN]:
            self.MOVING_LEFT = False
            self.MOVING_RIGHT = False
            self.MOVING_UP = False
            self.MOVING_DOWN = True

        if self.X_POS >= 1268:
            self.MOVING_RIGHT = False

        if self.X_POS <= 0:
            self.MOVING_LEFT = False

        if self.Y_POS >= 709:
            self.MOVING_DOWN = False

        if self.Y_POS <= 0:
            self.MOVING_UP = False

        if self.MOVING_RIGHT:
            self.X_POS += self.SNAKE_SPEED

        elif self.MOVING_LEFT:
            self.X_POS -= self.SNAKE_SPEED

        elif self.MOVING_UP:
            self.Y_POS -= self.SNAKE_SPEED

        elif self.MOVING_DOWN:
            self.Y_POS += self.SNAKE_SPEED
        # end if

        self.SNAKE_HEAD = pygame.Rect(self.X_POS, self.Y_POS, self.SNAKE_SIZE, self.SNAKE_SIZE)
        pygame.draw.rect(self.SURFACE, "black", self.SNAKE_HEAD)



