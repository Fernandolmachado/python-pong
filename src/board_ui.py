import pygame

from src import Text


class BoardUI(pygame.sprite.Sprite):
    def __init__(self, game_scene, pos, size, color, groups):
        super().__init__(groups)
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=pos)
        self.color = color

        # game scene attribute
        self.game = game_scene

        self.obj_group = pygame.sprite.Group()

        # timer
        self.timer = Text((50, 25), (100, 50), "white", [self.obj_group])
        self.timer.text = "01:00"
        self.timer.set_font(None, 50)

        # player1 board
        self.board1 = Text((self.image.get_rect().centerx - 50, 25), (100, 50), "white", [self.obj_group])
        self.board1.text = "00"
        self.board1.set_font(None, 60)

        # player2 board
        self.board2 = Text((self.image.get_rect().centerx + 50, 25), (100, 50), "white", [self.obj_group])
        self.board2.text = "00"
        self.board2.set_font(None, 60)

    def update_timer(self):
        self.timer.text = self.game.game_time.get_countdown()

    def update_score(self):
        self.board1.text = self.game.paddle1.get_score()
        self.board2.text = self.game.paddle2.get_score()

    def update(self):
        self.image.fill(0)  # clear tranparent surface

        self.update_timer()
        self.update_score()

        self.obj_group.update()
        self.obj_group.draw(self.image)
