from enum import Enum


class Game_States(Enum):
    running = 1
    quit = 2
    none = 0
    pause = 3
    play_message = 4
    play_scene = 5