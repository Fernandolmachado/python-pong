import pygame

from src import menu_color
from src import Scene, Background, MenuUI


class MenuScene(Scene):
    def __init__(self, game_manager, clock):
        super().__init__(game_manager, clock)

        self.background = Background(
            pygame.Rect(0 + 50, 0 + 50, self.display_surf.get_width() - 100, self.display_surf.get_height() - 100),
            "black", "white")

        self.ui_group = pygame.sprite.Group()
        self.menu_ui = MenuUI(self, (self.display_surf.get_width()/2, self.display_surf.get_height()/2),
                              (self.display_surf.get_width()/2, self.display_surf.get_height()/2), menu_color,
                              [self.ui_group])

    def run(self):
        self.background.draw()

        self.ui_group.update()
        self.ui_group.draw(self.display_surf)
