import json

from os.path import exists
from src import UserConfig

file = "pong.save"


def save_settings(config: UserConfig):
    f = open(file, "w")
    f.write(str(config.__dict__))
    f.close()


def load_settings() -> UserConfig:
    if not exists(file):
        config = UserConfig()
        save_settings(config)
        return config

    f = open(file, "r")
    state = json.loads(f.read().replace("'", "\""))
    f.close()

    return UserConfig(sxf=state["sxf_volume"], music=state["music_volume"],
                      time=state["game_time"], interval=state["time_interval"])
