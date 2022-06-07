import pygame

from src import UI, Text


class BoardUI(UI):
    def __init__(self, game_scene, pos, size, color, groups):
        super().__init__(game_scene, pos, size, color, groups)

        # timer
        self.timer = Text((50, 25), (100, 50), "white", [self.text_group])
        self.timer.text = "01:00"
        self.timer.set_font(None, 50)

        # player1 board
        self.board1 = Text((self.image.get_rect().centerx - 50, 25), (100, 50), "white", [self.text_group])
        self.board1.text = "00"
        self.board1.set_font(None, 60)

        # player2 board
        self.board2 = Text((self.image.get_rect().centerx + 50, 25), (100, 50), "white", [self.text_group])
        self.board2.text = "00"
        self.board2.set_font(None, 60)

    def update_timer(self):
        self.timer.text = self.game.game_time.get_countdown()

    def update_score(self):
        self.board1.text = self.game.paddle1.get_score()
        self.board2.text = self.game.paddle2.get_score()

    def on_update(self):
        self.update_timer()
        self.update_score()
