import pygame

from src import paddle_speed


class Paddle(pygame.sprite.Sprite):
    def __init__(self, pos, size, color, boundaries):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(center=pos)

        # field limits
        self.boundaries = boundaries

        # player movements
        self.speed = paddle_speed
        self.velocity = pygame.math.Vector2()

        # score
        self.score = 0

    def get_score(self):
        return "{:02d}".format(self.score)

    def increase_scored(self):
        self.score += 1

    def move(self):
        # move player and reset velocity
        self.rect.move_ip(0, self.velocity.y * self.speed)
        self.velocity = pygame.math.Vector2()

        # clamp player inside background field
        self.rect.clamp_ip(self.boundaries)

    def update(self):
        self.move()
