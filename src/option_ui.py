from src import button_border, button_color, button_hover_color, user_config
from src import UI, Text, ArrowButton, Button


class OptionUI(UI):
    def __init__(self, game_scene, pos, size, color, *groups):
        super().__init__(game_scene, pos, size, color, *groups, round=True)

        # VOLUME OPTIONS
        # volume options label
        lbl_volume = Text((self.image.get_rect().width // 8, (self.image.get_rect().height // 6)), (200, 80),
                          "white", [self.text_group])
        lbl_volume.text = "Volume:"

        # sfx volume label
        lbl_sfx = Text((self.image.get_rect().width // 8 * 2, (self.image.get_rect().height // 6 * 1.5)), (200, 80),
                       "white", [self.text_group])
        lbl_sfx.text = "Efeitos"
        lbl_sfx.set_font(None, 40)

        # sfx options value
        self.vl_sfx = Text((self.image.get_rect().width // 8 * 6, (self.image.get_rect().height // 6 * 1.5)), (200, 80),
                           "white", [self.text_group])
        self.vl_sfx.text = user_config.sxf_volume
        self.vl_sfx.set_font(None, 40)

        btn_left = ArrowButton((self.image.get_rect().width // 8 * 5.2, (self.image.get_rect().height // 6 * 1.5)),
                               (30, 30), button_color, "left", [self.button_group])
        btn_left.hover_color = button_hover_color

        def dec_sxf_volume():
            user_config.dec_sxf_volume()
            self.vl_sfx.text = user_config.sxf_volume

        btn_left.click_function = dec_sxf_volume

        btn_right = ArrowButton((self.image.get_rect().width // 8 * 6.8, (self.image.get_rect().height // 6 * 1.5)),
                                (30, 30), button_color, "right", [self.button_group])
        btn_right.hover_color = button_hover_color

        def inc_sxf_volume():
            user_config.inc_sxf_volume()
            self.vl_sfx.text = user_config.sxf_volume

        btn_right.click_function = inc_sxf_volume

        # music volume label
        lbl_music = Text((self.image.get_rect().width // 8 * 2, (self.image.get_rect().height // 6 * 2.3)), (200, 80),
                         "white", [self.text_group])
        lbl_music.text = "Musica"
        lbl_music.set_font(None, 40)

        # music volume value
        self.vl_music = Text((self.image.get_rect().width // 8 * 6, (self.image.get_rect().height // 6 * 2.3)),
                             (200, 80),
                             "white", [self.text_group])
        self.vl_music.text = user_config.music_volume
        self.vl_music.set_font(None, 40)

        btn_left = ArrowButton((self.image.get_rect().width // 8 * 5.2, (self.image.get_rect().height // 6 * 2.3)),
                               (30, 30), button_color, "left", [self.button_group])
        btn_left.hover_color = button_hover_color

        def dec_music_volume():
            user_config.dec_music_volume()
            self.vl_music.text = user_config.music_volume

        btn_left.click_function = dec_music_volume

        btn_right = ArrowButton((self.image.get_rect().width // 8 * 6.8, (self.image.get_rect().height // 6 * 2.3)),
                                (30, 30), button_color, "right", [self.button_group])
        btn_right.hover_color = button_hover_color

        def inc_music_volume():
            user_config.inc_music_volume()
            self.vl_music.text = user_config.music_volume

        btn_right.click_function = inc_music_volume

        # GAME OPTIONS
        # game options label
        lbl_game = Text((self.image.get_rect().width // 8, (self.image.get_rect().height // 6 * 3)), (200, 80),
                        "white", [self.text_group])
        lbl_game.text = "Jogo:"

        # time option label
        lbl_time = Text((self.image.get_rect().width // 8 * 2, (self.image.get_rect().height // 6 * 3.5)), (200, 80),
                        "white", [self.text_group])
        lbl_time.text = "Tempo"
        lbl_time.set_font(None, 40)

        # time option value
        self.vl_time = Text((self.image.get_rect().width // 8 * 6, (self.image.get_rect().height // 6 * 3.5)),
                            (200, 80),
                            "white", [self.text_group])
        self.vl_time.text = self.format_time(user_config.game_time)
        self.vl_time.set_font(None, 40)

        btn_left = ArrowButton((self.image.get_rect().width // 8 * 5.2, (self.image.get_rect().height // 6 * 3.5)),
                               (30, 30), button_color, "left", [self.button_group])
        btn_left.hover_color = button_hover_color

        def dec_time():
            user_config.dec_time()
            self.vl_time.text = self.format_time(user_config.game_time)

        btn_left.click_function = dec_time

        btn_right = ArrowButton((self.image.get_rect().width // 8 * 6.8, (self.image.get_rect().height // 6 * 3.5)),
                                (30, 30), button_color, "right", [self.button_group])
        btn_right.hover_color = button_hover_color

        def inc_time():
            user_config.inc_time()
            self.vl_time.text = self.format_time(user_config.game_time)

        btn_right.click_function = inc_time

        # BACK MENU BUTTON
        self.btn_menu = Button((self.image.get_rect().centerx, (self.image.get_rect().height // 4) * 3 + 20),
                               (200, 60), button_color, [self.button_group])
        self.btn_menu.round_radius = button_border
        self.btn_menu.text = "Voltar ao Menu"
        self.btn_menu.font_color = "black"
        self.btn_menu.hover_color = button_hover_color

        def on_click_exit():
            self.game.ui_index = 0
            self.save_options()

        self.btn_menu.click_function = on_click_exit

    @staticmethod
    def format_time(time):
        time_sec = time / 1000
        return "{:02d}:{:02d}".format(int(time_sec // 60), int(time_sec % 60))

    def save_options(self):
        # TODO: save options in json file
        pass
