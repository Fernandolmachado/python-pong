import pygame

music_menu = ""
music_game = "assets/sounds/music/pong_game.wav"
music_pause = ""
music_endgame = ""

sfx_click = "assets/sounds/sfx/button_click_sfx.ogg"
sfx_hover = "assets/sounds/sfx/button_hover_sfx.ogg"
sfx_wall = "assets/sounds/sfx/wall_collision_sfx.ogg"
sfx_paddle = "assets/sounds/sfx/paddle_collision_sfx.ogg"
sfx_goal = "assets/sounds/sfx/goal_sfx.ogg"


class AudioComposer:
    def __init__(self):
        pygame.mixer.init()

        #music
        self.music = pygame.mixer.music

        # sfx
        self.sfx_click = pygame.mixer.Sound(sfx_click)
        self.sfx_hover = pygame.mixer.Sound(sfx_hover)
        self.sfx_wall = pygame.mixer.Sound(sfx_wall)
        self.sfx_paddle = pygame.mixer.Sound(sfx_paddle)
        self.sfx_goal = pygame.mixer.Sound(sfx_goal)

    def set_music_volume(self, value):
        self.music.set_volume(value/100)

    def set_sfx_volume(self, value):
        self.sfx_click.set_volume(value/100)
        self.sfx_hover.set_volume(value/100)
        self.sfx_wall.set_volume(value/100)
        self.sfx_paddle.set_volume(value/100)
        self.sfx_goal.set_volume(value/100)

    def set_menu(self):
        self.music.load(music_menu)

    def set_game(self):
        self.music.load(music_game)

    def set_pause(self):
        self.music.load(music_pause)

    def set_endgame(self):
        self.music.load(music_endgame)
