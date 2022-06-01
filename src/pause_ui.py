import pygame

from src import button_border, button_color, button_hover_color
from src import Button


class PauseUI(pygame.sprite.Sprite):
    def __init__(self, game_scene, pos, size, color, groups):
        super().__init__(groups)
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=pos)
        self.color = color

        # game scene attribute
        self.game = game_scene

        # setup pause buttons
        self.button_group = pygame.sprite.Group()

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
            self.game.ball.reset_ball()
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

    def round(self):
        w, h = self.image.get_size()
        pygame.draw.rect(self.image, self.color, (0, 0, w, h), border_radius=20)
        pygame.draw.rect(self.image, "white", (10, 10, w - 20, h - 20), 2, border_radius=18)

    def input(self):
        # get mouse position
        mousex, mousey = pygame.mouse.get_pos()

        # normalize mouse position to the ui surface
        mousex -= self.rect.left
        mousey -= self.rect.top
        mouse_pos = (mousex, mousey)

        for index, button in enumerate(self.button_group.sprites()):
            if button.rect.collidepoint(mouse_pos):
                button.on_hover()
            else:
                button.reset()

        for event in pygame.event.get(pygame.MOUSEBUTTONDOWN):
            for button in self.button_group.sprites():
                if button.rect.collidepoint(mouse_pos):
                    button.on_click()
                    break

    def update(self):
        self.input()

        self.image.fill(0)  # clear tranparent surface
        self.round()
        self.button_group.update()
        self.button_group.draw(self.image)
