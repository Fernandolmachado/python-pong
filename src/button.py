import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, pos, size, color, groups):
        super().__init__(groups)
        # sprite attriutes
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=pos)

        # rect attributes
        self.base_color = color
        self.color = self.base_color
        self.round_radius = 0

        # text attributes
        self.font_color = "black"
        self.font_size = 30
        self.text = ""
        self.font = pygame.font.Font(None, self.font_size)

        # effects attributes
        self.hover_color = "white"
        self.click_function = None
        self.release_function = None

    def on_hover(self):
        self.color = self.hover_color

    def on_click(self):
        self.click_function()

    def on_release(self):
        self.release_function()

    def reset(self):
        self.color = self.base_color

    def update(self):
        self.round()
        self.label()

    def round(self):
        w, h = self.image.get_size()
        pygame.draw.rect(self.image, self.color, (0, 0, w, h), border_radius=self.round_radius)
        pygame.draw.rect(self.image, "white", (2, 2, w - 4, h - 4), 1, border_radius=self.round_radius-2)

    def label(self):
        text_surf = self.font.render(str(self.text), True, self.font_color)
        text_rect = text_surf.get_rect(center=self.image.get_rect().center)
        pygame.draw.rect(self.image, self.color, text_rect)
        self.image.blit(text_surf, text_rect)

    def set_font(self, font, size):
        self.font = pygame.font.Font(font, size)
