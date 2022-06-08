import pygame
import sys

from src import screen_width, screen_height, screen_caption
from src import GameManager

pygame.init()

pygame.display.set_caption(screen_caption)
screen = pygame.display.set_mode((screen_width, screen_height), pygame.SCALED)

buffer_surf = pygame.Surface((screen_width, screen_height))

clock = pygame.time.Clock()
fps = 60

manager = GameManager(clock, buffer_surf)

while True:
    for event in pygame.event.get(pygame.QUIT):
        pygame.quit()
        sys.exit()

    screen.fill('black')
    buffer_surf.fill(0)

    manager.run()

    buffer_render = pygame.transform.scale(buffer_surf, screen.get_size())
    screen.blit(buffer_render, (0, 0))

    pygame.display.update()
    clock.tick(fps)
