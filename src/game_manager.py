from src import MenuScene, GameScene


class GameManager:
    def __init__(self, clock):
        self.scene_index = 0
        self.scenes = [
            MenuScene(self, clock),
            GameScene(self, clock)
        ]

    def run(self):
        self.scenes[self.scene_index].run()
