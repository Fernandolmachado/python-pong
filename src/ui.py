import pygame


class UI(pygame.sprite.Sprite):
    def __init__(self, game_scene, pos, size, color, *groups, round=False):
        super().__init__(groups)
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=pos)
        self.color = color

        self.rounded = round

        # game scene attribute
        self.game = game_scene

        # setup text
        self.text_group = pygame.sprite.Group()

        # setup buttons
        self.button_group = pygame.sprite.Group()
        self.button_size = (300, 80)

    def round(self):
        if not self.rounded:
            return

        w, h = self.image.get_size()
        pygame.draw.rect(self.image, self.color, (0, 0, w, h), border_radius=20)
        pygame.draw.rect(self.image, "white", (10, 10, w - 20, h - 20), 2, border_radius=18)

    def input(self):
        # get mouse position
        mouseX, mouseY = pygame.mouse.get_pos()

        # normalize mouse position to the ui surface
        mouseX -= self.rect.left
        mouseY -= self.rect.top
        mouse_pos = (mouseX, mouseY)

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

    def on_update(self):
        pass

    def update(self):
        self.input()

        self.image.fill(0)  # clear tranparent surface
        self.round()

        self.on_update()

        self.text_group.update()
        self.button_group.update()
        self.text_group.draw(self.image)
        self.button_group.draw(self.image)
