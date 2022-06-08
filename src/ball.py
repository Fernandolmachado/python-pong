import pygame
import random

from src import ball_speed, start_delay, ball_radius, audio_composer
from src import Timer


class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, color, boundaries):
        super().__init__()
        # Setup sprite
        self.image = pygame.Surface((ball_radius*2, ball_radius*2), pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect(center=pos)
        self.draw_circle(ball_radius, color)

        self.boundaries = boundaries

        # setup ball movement
        self.pos = pos
        self.speed = ball_speed
        self.velocity = pygame.math.Vector2()

        # set default position and control start delay
        self.timer = None
        self.reset = False

        # setup ball grip
        self.grip = 0.08

    def draw_circle(self, radius, color):
        pygame.draw.circle(self.image, color, self.image.get_rect().center, radius)

    def set_velocity(self):
        selection = [1, -1]
        self.velocity = pygame.math.Vector2(random.choice(selection), random.choice(selection)).normalize()

    def reset_ball(self, clock):
        if self.timer is None:
            self.timer = Timer(clock, start_delay)

        self.rect.center = self.pos
        self.velocity = pygame.math.Vector2()

        self.timer.start()
        self.reset = True

    def move(self):
        self.rect.center += self.velocity * self.speed

        # Vertical boundy
        if self.rect.top <= self.boundaries.top:
            self.rect.top = self.boundaries.top + 1
            self.velocity.y *= -1
            audio_composer.sfx_wall.play()
        elif self.rect.bottom >= self.boundaries.bottom:
            self.rect.bottom = self.boundaries.bottom - 1
            self.velocity.y *= -1
            audio_composer.sfx_wall.play()

    def update(self):
        # capture event created early
        if self.reset and self.timer.time_reached():
            self.set_velocity()

            # reset timer controls
            self.reset = False
            self.timer.stop()

        self.timer.update()
        self.move()
