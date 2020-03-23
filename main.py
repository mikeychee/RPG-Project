import pygame
from game import Game
from game_states import Game_States
import config


pygame.init()

screen = pygame.display.set_mode((config.screen_width, config.screen_height))
pygame.display.set_caption("RPG!")

game = Game(screen)
game.set_up()

while game.game_state != Game_States.quit:

    if game.game_state == Game_States.running:
        config.clock.tick(config.fps)  # frame rate
        pygame.time.delay(50)

        game.update(config.clock)
        # game.manage_ais()

    elif game.game_state == Game_States.pause:
        game.pause_game()

    elif game.game_state == Game_States.play_message:
        game.play_message()

    elif game.game_state == Game_States.play_scene:
        game.play_scene()

    else:
        game.game_state = Game_States.running

