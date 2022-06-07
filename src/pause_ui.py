import pygame

from src import button_border, button_color, button_hover_color
from src import UI, Button


class PauseUI(UI):
    def __init__(self, game_scene, pos, size, color, groups):
        super().__init__(game_scene, pos, size, color, groups, round=True)

        # play button
        self.play_button = Button((self.image.get_rect().centerx, self.image.get_rect().height // 4),
                                  (300, 80), button_color, [self.button_group])
        self.play_button.round_radius = button_border
        self.play_button.text = "Jogar"
        self.play_button.font_color = "black"
        self.play_button.hover_color = button_hover_color

        def on_click_play():
            self.game.paused = False

        self.play_button.click_function = on_click_play

        # restart button
        self.restart_button = Button(self.image.get_rect().center,
                                     (300, 80), button_color, [self.button_group])
        self.restart_button.round_radius = button_border
        self.restart_button.text = "Reiniciar"
        self.restart_button.font_color = "black"
        self.restart_button.hover_color = button_hover_color

        def on_click_restart():
            self.game.ball.reset_ball(self.game.clock)
            self.game.paused = False
            self.game.game_time.stop()
            self.game.game_time.start()
            self.game.paddle1.score = 0
            self.game.paddle2.score = 0

        self.restart_button.click_function = on_click_restart

        # menu button
        self.exit_button = Button((self.image.get_rect().centerx, (self.image.get_rect().height // 4) * 3 + 2),
                                  (300, 80), button_color, [self.button_group])
        self.exit_button.round_radius = button_border
        self.exit_button.text = "Voltar ao Menu"
        self.exit_button.font_color = "black"
        self.exit_button.hover_color = button_hover_color

        def on_click_exit():
            self.game.game_manager.scene_index -= 1

        self.exit_button.click_function = on_click_exit
