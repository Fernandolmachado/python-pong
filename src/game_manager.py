from src import MenuScene, GameScene


class GameManager:
    def __init__(self, clock):
        self.clock = clock

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
            self.current_scene = self.scenes[self.scene_index](self, self.clock)
            self.last_scene = self.scene_index

        self.current_scene.run()
