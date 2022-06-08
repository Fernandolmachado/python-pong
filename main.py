import pygame
import sys

from src import screen_width, screen_height, screen_caption
from src import GameManager

pygame.init()

pygame.display.set_caption(screen_caption)
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()
fps = 60

manager = GameManager(clock)

while True:
    for event in pygame.event.get(pygame.QUIT):
        pygame.quit()
        sys.exit()

    screen.fill('black')
    manager.run()
    # TODO: create a buffer surface, that will make window size flexible
    pygame.display.update()
    clock.tick(fps)
