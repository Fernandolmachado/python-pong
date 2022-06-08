import pygame

from src import Button


class ArrowButton(Button):
    def __init__(self, pos, size, color, direction, *groups):
        super().__init__(pos, size, color, *groups)

        if direction == "up":
            self.triangle_function = self.up_triangle
        elif direction == "down":
            self.triangle_function = self.down_triangle
        elif direction == "left":
            self.triangle_function = self.left_triangle
        elif direction == "right":
            self.triangle_function = self.right_triangle

    def draw_triangle(self):
        self.triangle_function()

    def up_triangle(self):
        rect = self.image.get_rect()
        pygame.draw.polygon(self.image, self.color, [(rect.width*0.5, 0), (0, rect.height), (rect.width, rect.height)])

    def down_triangle(self):
        rect = self.image.get_rect()
        pygame.draw.polygon(self.image, self.color, [(0, 0), (rect.width, 0), (rect.width*0.5, rect.height)])

    def left_triangle(self):
        rect = self.image.get_rect()
        pygame.draw.polygon(self.image, self.color, [(rect.width, 0), (rect.width, rect.height), (0, rect.height*0.5)])

    def right_triangle(self):
        rect = self.image.get_rect()
        pygame.draw.polygon(self.image, self.color, [(0, 0), (rect.width, rect.height*0.5), (0, rect.height)])

    def update(self):
        self.draw_triangle()
