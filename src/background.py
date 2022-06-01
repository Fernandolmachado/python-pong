import pygame


class Background(pygame.Surface):
    def __init__(self, rect, back_color, line_color):
        super().__init__(rect.size)
        self.rect = rect
        self.display_surf = pygame.display.get_surface()
        self.draw_surface(back_color, line_color)

    def draw_surface(self, back_color, line_color):
        self.fill(back_color)
        pygame.draw.rect(self, line_color, (0, 0, self.rect.width, self.rect.height), 1, border_radius=10)
        pygame.draw.line(self, line_color, (self.rect.width / 2, 0), (self.rect.width / 2, self.rect.height), 1)

    def draw(self):
        self.display_surf.blit(self, self.rect.topleft)

    def get_field_rect(self):
        return self.rect
