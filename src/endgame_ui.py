import sys
import pygame

from src import button_border, button_color, button_hover_color
from src import UI, Text, Button


class EndgameUI(UI):
    def __init__(self, game_scene, pos, size, color, *groups):
        super().__init__(game_scene, pos, size, color, *groups, round=True)

        # win text
        self.win_text = Text((self.image.get_rect().centerx, self.image.get_rect().height // 4), (300, 80),
                             "white", [self.text_group])
        self.win_text.text

        # play again button
        self.play_button = Button(self.image.get_rect().center, (300, 80), button_color, *[self.button_group])
        self.play_button.round_radius = button_border
        self.play_button.text = "Jogar novamente"
        self.play_button.font_color = "black"
        self.play_button.hover_color = button_hover_color

        def on_click_play():
            self.game.ball.reset_ball(self.game.clock)
            self.game.end = False
            self.game.game_time.stop()
            self.game.game_time.start()
            self.game.paddle1.score = 0
            self.game.paddle2.score = 0

        self.play_button.click_function = on_click_play

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

    def set_win(self, player=None):
        if player is None:
            self.win_text.text = "Empate!"
        else:
            self.win_text.text = "Jogador {} venceu".format(str(player))
