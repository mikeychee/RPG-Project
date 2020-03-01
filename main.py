import pygame
from game import Game
from game_states import Game_States
import config


pygame.init()

screen = pygame.display.set_mode((config.screen_width, config.screen_height))
pygame.display.set_caption("Attempt at RPG")

game = Game(screen)
game.set_up()


while game.game_state == Game_States.running:
    config.clock.tick(config.fps)  # frame rate
    #pygame.time.delay(100)

    game.update(config.clock)
    game.manage_ais()
