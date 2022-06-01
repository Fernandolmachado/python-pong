import pygame

# screen attributes
screen_width = 1200
screen_height = 700
screen_caption = "Pong"

# paddle attributes
paddle_size = pygame.math.Vector2(30, 200)
paddle_speed = 5

# ball attributes
ball_speed = 10
ball_radius = 10

# ball restart delay
start_delay = 1000
STARTEVENT = pygame.USEREVENT+1

# pause button attributes
button_color = (60, 60, 50, 150)
button_hover_color = (160, 160, 100, 150)
button_border = 10

# game attributes
match_time = 120000     # msec

menu_color = pygame.Color(40, 40, 40, 180)
