class UserConfig:
    def __init__(self):
        self.sxf_volume = 100
        self.music_volume = 100
        self.game_time = 60000
        self.time_interval = 30000

    def inc_sxf_volume(self):
        self.sxf_volume += 1
        self.clamp_sfx()

    def dec_sxf_volume(self):
        self.sxf_volume -= 1
        self.clamp_sfx()

    def inc_music_volume(self):
        self.music_volume += 1
        self.clamp_music()

    def dec_music_volume(self):
        self.music_volume -= 1
        self.clamp_music()

    def inc_time(self):
        self.game_time += self.time_interval
        self.clamp_time()

    def dec_time(self):
        self.game_time -= self.time_interval
        self.clamp_time()

    def clamp_sfx(self):
        if self.sxf_volume > 100:
            self.sxf_volume = 100
        elif self.sxf_volume < 0:
            self.sxf_volume = 0

    def clamp_music(self):
        if self.music_volume > 100:
            self.music_volume = 100
        elif self.music_volume < 0:
            self.music_volume = 0

    def clamp_time(self):
        if self.game_time > 300000:
            self.game_time = 300000
        elif self.game_time < 30000:
            self.game_time = 30000
