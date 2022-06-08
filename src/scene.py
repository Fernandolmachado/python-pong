import pygame
from abc import abstractmethod


class Scene:
    def __init__(self, game_manager, clock, display):
        self.display_surf = display
        self.game_manager = game_manager
        self.clock = clock

    @abstractmethod
    def run(self):
        raise NotImplementedError()
