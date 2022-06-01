import pygame
from abc import abstractmethod


class Scene:
    def __init__(self, game_manager, clock):
        self.display_surf = pygame.display.get_surface()
        self.game_manager = game_manager
        self.clock = clock

    @abstractmethod
    def run(self):
        raise NotImplementedError()
