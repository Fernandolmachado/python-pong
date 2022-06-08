import pygame

from src import menu_color
from src import Scene, Background, MenuUI, OptionUI


class MenuScene(Scene):
    def __init__(self, game_manager, clock, display):
        super().__init__(game_manager, clock, display)

        self.background = Background(
            pygame.Rect(0 + 50, 0 + 50, self.display_surf.get_width() - 100, self.display_surf.get_height() - 100),
            "black", "white", self.display_surf)

        self.ui_group = pygame.sprite.GroupSingle()

        # setup menu ui
        self.menu_ui = MenuUI(self, (self.display_surf.get_width() * 0.5, self.display_surf.get_height() * 0.5),
                              (self.display_surf.get_width() *0.5, self.display_surf.get_height() * 0.5), menu_color)

        # setup option ui
        self.option_ui = OptionUI(self, (self.display_surf.get_width() * 0.5, self.display_surf.get_height() * 0.5),
                                  (self.display_surf.get_width() * 0.5, self.display_surf.get_height() * 0.5), menu_color)

        self.ui_list = [self.menu_ui, self.option_ui]
        self.last_index = -1
        self.ui_index = 0

    def set_visible_ui(self):
        if self.ui_index != self.last_index:
            self.ui_group.remove(self.ui_list[self.last_index])
            self.ui_group.add(self.ui_list[self.ui_index])
            self.last_index = self.ui_index

    def run(self):
        self.background.draw()

        self.set_visible_ui()

        self.ui_group.update()
        self.ui_group.draw(self.display_surf)
