import pygame


class Text(pygame.sprite.Sprite):
    def __init__(self, pos, size, color, groups):
        super().__init__(groups)
        # sprite attriutes
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=pos)

        # text attributes
        self.font_color = color
        self.font_size = 30
        self.text = ""
        self.font = pygame.font.Font(None, self.font_size)

    def update(self):
        self.image.fill(0)
        self.label()

    def label(self):
        text_surf = self.font.render(str(self.text), True, self.font_color)
        text_rect = text_surf.get_rect(center=self.image.get_rect().center)
        self.image.blit(text_surf, text_rect)

    def set_font(self, font, size):
        self.font = pygame.font.Font(font, size)
