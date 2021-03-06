import pygame

from src import screen_width, screen_height, paddle_size, menu_color, user_config, audio_composer
from src import Background, Paddle, Ball
from src import Timer
from src import BoardUI, PauseUI, EndgameUI
from src import Scene


class GameScene(Scene):
    def __init__(self, game_manager, clock, display):
        super().__init__(game_manager, clock, display)

        # setup background
        self.background = Background(pygame.Rect(0, 50, screen_width, screen_height - 50),
                                     "black", "white", self.display_surf)
        back_rect = self.background.get_field_rect()

        # setup players
        self.paddle1 = Paddle((paddle_size.x / 2, back_rect.top + back_rect.height / 2),
                              paddle_size, "blue", back_rect)
        self.paddle2 = Paddle((back_rect.width - paddle_size.x / 2, back_rect.top + back_rect.height / 2),
                              paddle_size, "red", back_rect)

        # setup ball
        self.initial_ball_pos = (back_rect.width / 2, back_rect.top + back_rect.height / 2)
        self.ball = Ball(self.initial_ball_pos, "white", back_rect)
        self.ball.reset_ball(self.clock)

        # setup visible sprites
        self.visible_group = pygame.sprite.Group()
        self.visible_group.add(self.paddle1)
        self.visible_group.add(self.paddle2)
        self.visible_group.add(self.ball)

        # setup UI attributes
        self.ui_group = pygame.sprite.GroupSingle()

        disp_rect = self.display_surf.get_rect()
        self.ui = BoardUI(self, (disp_rect.width / 2, 25), (disp_rect.width, 50),
                          pygame.Color(40, 40, 40, 180), [self.ui_group])

        # setup pause attributes
        self.pause_group = pygame.sprite.GroupSingle()
        self.pause_ui = PauseUI(self, (disp_rect.width / 2, disp_rect.height / 2),
                                (disp_rect.width * 0.5, disp_rect.height * 0.5), menu_color, [self.pause_group])

        # pause attributes
        self.paused = False
        self.pause_timer = Timer(self.clock, 300)
        self.pause_timer.reached = True

        # setup end-game ui
        self.endgame_group = pygame.sprite.GroupSingle()
        self.endgame_ui = EndgameUI(self, (disp_rect.width / 2, disp_rect.height / 2),
                                    (disp_rect.width * 0.5, disp_rect.height * 0.5), menu_color, [self.endgame_group])

        # game attributes
        self.game_time = Timer(self.clock, user_config.game_time)
        self.game_time.start()

        self.end = False

        # setup game music
        audio_composer.set_game()
        audio_composer.music.play(-1)

    def input(self):
        keys = pygame.key.get_pressed()

        # check pause request
        if keys[pygame.K_ESCAPE] and self.pause_timer.time_reached():
            self.pause_timer.stop()
            self.pause_timer.start()

            if self.paused:
                self.paused = False
                audio_composer.music.unpause()
            else:
                self.paused = True
                audio_composer.music.pause()

        if not self.paused:
            # check player 1 input
            if keys[pygame.K_w]:
                self.paddle1.velocity = pygame.math.Vector2(0, -1)
            elif keys[pygame.K_s]:
                self.paddle1.velocity = pygame.math.Vector2(0, 1)

            # check player 2 input
            if keys[pygame.K_UP]:
                self.paddle2.velocity = pygame.math.Vector2(0, -1)
            elif keys[pygame.K_DOWN]:
                self.paddle2.velocity = pygame.math.Vector2(0, 1)

    def make_shot(self):
        if self.paddle1.rect.colliderect(self.ball.rect):
            audio_composer.sfx_paddle.play()
            if (self.paddle1.rect.top > self.ball.rect.centery and self.ball.velocity.y > 0) \
                    or self.paddle1.rect.bottom < self.ball.rect.centery and self.ball.velocity.y < 0:
                # check is collision is lateral
                self.ball.velocity.y *= -1
            else:
                # use grip to reedirect the ball
                self.grip(self.paddle1.velocity)

            self.ball.rect.left = self.paddle1.rect.right
            self.ball.velocity.x *= -1

        if self.paddle2.rect.colliderect(self.ball.rect):
            audio_composer.sfx_paddle.play()
            if (self.paddle2.rect.top > self.ball.rect.centery and self.ball.velocity.y > 0) \
                    or (self.paddle2.rect.bottom < self.ball.rect.centery and self.ball.velocity.y < 0):
                # check is collision is lateral
                self.ball.velocity.y *= -1
            else:
                # use grip to reedirect the ball
                self.grip(self.paddle2.velocity)

            self.ball.rect.right = self.paddle2.rect.left
            self.ball.velocity.x *= -1

    def grip(self, velocity):
        self.ball.velocity = (self.ball.velocity + (velocity * self.ball.grip)).normalize()

    def make_goal(self):
        if self.ball.rect.left <= 0:
            self.ball.reset_ball(self.clock)
            self.paddle2.increase_scored()
            audio_composer.sfx_goal.play()
        elif self.ball.rect.right >= self.background.get_width():
            self.ball.reset_ball(self.clock)
            self.paddle1.increase_scored()
            audio_composer.sfx_goal.play()

    def rules(self):
        self.game_time.update()
        self.make_shot()
        self.make_goal()
        self.endgame()

    def endgame(self):
        if self.game_time.time_reached():
            audio_composer.music.stop()
            self.end = True
            if self.paddle1.score > self.paddle2.score:
                self.endgame_ui.set_win(1)
            elif self.paddle1.score < self.paddle2.score:
                self.endgame_ui.set_win(2)
            else:
                self.endgame_ui.set_win()

    def run(self):
        self.input()
        self.pause_timer.update()  # hold esc button activate to not process every frame

        if not self.paused and not self.end:
            self.rules()
            self.visible_group.update()
            self.ui_group.update()

        self.background.draw()
        self.visible_group.draw(self.display_surf)
        self.ui_group.draw(self.display_surf)

        if self.paused:
            self.pause_group.update()
            self.pause_group.draw(self.display_surf)

        if self.end:
            self.endgame_group.update()
            self.endgame_group.draw(self.display_surf)
