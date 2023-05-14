import pygame


class Snake:
    """
    methods for updating motion of the snake
    """
    SNAKE = None
    BLACK = "black"
    WHITE = "white"

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
        self.SNAKE_SPEED = 1
        self.SURFACE = surface
        self.SNAKE_HEAD = SnakeHead(1280 / 2, 720 / 2)
        self.SNAKE_BODY = [self.SNAKE_HEAD, SnakeHead(640, 720), SnakeHead(639, 720), SnakeHead(638, 720),
                           SnakeHead(637, 720), SnakeHead(636, 720), SnakeHead(635, 720), SnakeHead(634, 720),
                           SnakeHead(633, 720), SnakeHead(632, 720), SnakeHead(631, 720), SnakeHead(630, 720)]
        self.APPLE_EATEN = False

    def grow_snake(self):
        self.SNAKE_BODY.extend([SnakeHead(0, 0)] * 8)
        self.APPLE_EATEN = True

    def update_body(self):
        """
        update body of snake based on head movement
        """
        for body_index in range(len(self.SNAKE_BODY) - 1, 0, -1):
            self.SNAKE_BODY[body_index] = self.SNAKE_BODY[body_index - 1]
        # end for

    # end def update_body

    def update_motion(self):
        """
        Update x and y position for snake head based on key press
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

        self.update_body()
        self.SNAKE_HEAD = SnakeHead(self.X_POS, self.Y_POS, self.WHITE)
        self.SNAKE_BODY[0] = self.SNAKE_HEAD

        if self.MOVING_RIGHT:
            self.X_POS += self.SNAKE_SPEED

        elif self.MOVING_LEFT:
            self.X_POS -= self.SNAKE_SPEED

        elif self.MOVING_UP:
            self.Y_POS -= self.SNAKE_SPEED

        elif self.MOVING_DOWN:
            self.Y_POS += self.SNAKE_SPEED
        # end if

        # snake_head = pygame.Rect(self.SNAKE_HEAD.X_POS, self.SNAKE_HEAD.Y_POS, self.SNAKE_SIZE, self.SNAKE_SIZE)
        # pygame.draw.rect(self.SURFACE, "black", snake_head)

        for snake_part in self.SNAKE_BODY:
            snake = pygame.Rect(snake_part.X_POS, snake_part.Y_POS, 12, 12)
            if self.APPLE_EATEN:
                pygame.draw.rect(self.SURFACE, self.WHITE, snake)
                self.APPLE_EATEN = False
            else:
                pygame.draw.rect(self.SURFACE, self.BLACK, snake)


class SnakeHead:
    def __init__(self, x, y, color="black"):
        self.MOVING_LEFT = False
        self.MOVING_RIGHT = False
        self.MOVING_UP = False
        self.MOVING_DOWN = False
        self.X_POS = x
        self.Y_POS = y
        self.COLOR = color

    def get_rect_object(self):
        return pygame.Rect(self.X_POS, self.Y_POS, 12, 12)
