from src import MenuScene, GameScene, UserConfig
from src import user_config


class GameManager:
    def __init__(self, clock, display):
        self.clock = clock
        self.display = display

        self.current_scene = None
        self.last_scene = -1
        self.scene_index = 0
        self.scenes = [
            MenuScene,
            GameScene
        ]

    def run(self):
        # check if was prompted another scene
        if self.scene_index != self.last_scene:
            self.current_scene = self.scenes[self.scene_index](self, self.clock, self.display)
            self.last_scene = self.scene_index

        self.current_scene.run()
