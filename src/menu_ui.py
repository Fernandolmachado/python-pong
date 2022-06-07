import sys
import pygame

from src import button_border, button_color, button_hover_color
from src import UI, Button


class MenuUI(UI):
    def __init__(self, game_scene, pos, size, color, *groups):
        super().__init__(game_scene, pos, size, color, *groups, round=True)

        # play button
        self.play_button = Button((self.image.get_rect().centerx, self.image.get_rect().height // 4),
                                  (300, 80), button_color, *[self.button_group])
        self.play_button.round_radius = button_border
        self.play_button.text = "Jogar"
        self.play_button.font_color = "black"
        self.play_button.hover_color = button_hover_color

        def on_click_play():
            self.game.game_manager.scene_index += 1

        self.play_button.click_function = on_click_play

        # option button
        self.option_button = Button(self.image.get_rect().center,
                                    (300, 80), button_color, [self.button_group])
        self.option_button.round_radius = button_border
        self.option_button.text = "Opções"
        self.option_button.font_color = "black"
        self.option_button.hover_color = button_hover_color

        def on_click_option():
            pass
            # TODO: create option

        self.option_button.click_function = on_click_option

        # exit button
        self.exit_button = Button((self.image.get_rect().centerx, (self.image.get_rect().height // 4) * 3 + 2),
                                  (300, 80), button_color, [self.button_group])
        self.exit_button.round_radius = button_border
        self.exit_button.text = "Sair"
        self.exit_button.font_color = "black"
        self.exit_button.hover_color = button_hover_color

        def on_click_exit():
            pygame.quit()
            sys.exit(0)

        self.exit_button.click_function = on_click_exit
