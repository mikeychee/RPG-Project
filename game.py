import time

import pygame
from characters import Player, CharacterController
from game_states import Game_States
from tile import Map_Tile, Obstacles
from text import Text_Controller
import config
#TODO: MAKE THE ACTUAL GAME LOL


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.game_messages = []
        self.game_state = Game_States.none
        self.map = []
        self.characters = []
        self.text_background = pygame.Surface((config.screen_width, 180))
        self.message_count = 0

        self.grid_index_X = int(config.screen_width / config.scale) - 1
        self.grid_index_Y = int(config.screen_height / config.scale)

        self.main_map = pygame.Surface((config.screen_width, config.screen_height))

        self.game_map = [[Map_Tile(True, False) for y in range(0, config.screen_height)] for x in
                         range(0, config.screen_width)]

        for x in range(5, 12):
            for y in range(5, 7):
                self.game_map[x][y].movement = False
                self.game_map[x][y].movement = False

        self.player = Player(self.screen, self.game_map)  # initialise player

        # initialise first tester npc
        self.tester_npc = CharacterController("NPC1", 7, 8, self.screen, config.NPC01, self.game_map)
        self.message1 = self.tester_npc.text_to_speak(self.screen, "Hi there! How are you doing?",
                                                      config.game_messages,
                                                      (1 * config.scale, 9 * config.scale),
                                                      config.black)
        self.message2 = self.tester_npc.text_to_speak(self.screen, "I like you very much!", config.game_messages,
                                                      (1 * config.scale, 9 * config.scale),
                                                      config.black)

        # TODO: find out a better way to do this

        # sets the tree objects
        self.tester_npc2 = CharacterController("NPC2", 3, 3, self.screen, config.NPC02, self.game_map)

        self.treesXb = [Obstacles(config.tree01, x, 11, self.player.group)
                        for x in range(self.grid_index_X)]
        self.treesXt = [Obstacles(config.tree01, x, 0, self.player.group)
                        for x in range(self.grid_index_X)]

        self.treesYl = [Obstacles(config.tree01, 0, y, self.player.group)
                        for y in range(self.grid_index_Y)]
        self.treesYr = [Obstacles(config.tree01, self.grid_index_X, y, self.player.group)
                        for y in range(self.grid_index_Y)]

        self.trees = [self.treesXb, self.treesXt, self.treesYl, self.treesYr]

        # adds the tree border to the game

        for x in range(self.grid_index_X):
            self.game_map[x][self.grid_index_Y - 1].blocked = True
            self.game_map[x][0].blocked = True
        for y in range(self.grid_index_Y):
            self.game_map[0][y].blocked = True
            self.game_map[self.grid_index_X][y].blocked = True

    def set_up(self):
        print("setting up")
        self.game_state = Game_States.running

        self.objects.append(self.tester_npc)
        self.objects.append(self.tester_npc2)

        self.characters.append(self.tester_npc)
        self.characters.append(self.tester_npc2)

        # TODO: find out a better way to do this

        for tree_list in self.trees:
            for tree in tree_list:
                self.objects.append(tree)

        self.objects.append(self.player)  # adds player to object list

        self.render_map(self.game_map)
        self.screen.blit(self.main_map, (0, 0))

        pygame.display.flip()  # update screen

    def update(self, clock):

        self.game_messages = [self.message1, self.message2]

        fps_count = Text_Controller(self.screen, "FPS: " + str(int(clock.get_fps())),
                                    config.fps_Counter, (5, 5), config.black)

        self.screen.blit(self.main_map, (0, 0))
        self.render_blocked_tiles(self.game_map)
        self.manage_events()

        for obj in self.objects:  # draws all objects into the screen
            obj.image.convert()
            obj.draw(self.screen)
            fps_count.draw_text()

        self.player.rect.topleft = self.player.rect.x, self.player.rect.y  # updates player's rect

        for character in self.characters:
            self.player.check_collision(character.group)
            character.check_collision(self.player, self)  # the one that identifies it

        pygame.display.flip()

    def manage_ais(self):
        self.tester_npc.ai_left_right()
        self.tester_npc2.ai_up_down()

    def manage_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = Game_States.quit

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    self.game_state = Game_States.quit

                elif event.key == pygame.K_a:  # left
                    self.player.update_position(0, -1)
                    self.player.left = True
                    self.player.right = False
                    self.player.front = False
                    self.player.back = False

                elif event.key == pygame.K_d:  # right
                    self.player.update_position(0, 1)
                    self.player.left = False
                    self.player.right = True
                    self.player.front = False
                    self.player.back = False

                elif event.key == pygame.K_w:  # up
                    self.player.update_position(-1, 0)
                    self.player.front = False
                    self.player.back = True
                    self.player.left = False
                    self.player.right = False

                elif event.key == pygame.K_s:  # down
                    self.player.update_position(1, 0)
                    self.player.front = True
                    self.player.back = False
                    self.player.left = False
                    self.player.right = False

                else:
                    self.player.left = False
                    self.player.right = False
                    self.player.back = False
                    self.player.front = False
                    self.player.walk_count = 0

                if event.key == pygame.K_p:  # pause
                    self.pause_game()

    def render_map(self, drawn_map):

        for x in range(0, config.screen_width):
            for y in range(0, config.screen_height):

                if drawn_map[x][y].movement:
                    self.main_map.blit(config.grass01, (x * config.scale, y * config.scale))

    def render_blocked_tiles(self, drawn_map):
        for x in range(0, config.screen_width):
            for y in range(0, config.screen_height):

                if not drawn_map[x][y].movement:
                    self.screen.blit(config.water01, (x * config.scale, y * config.scale))

    def pause_game(self):
        self.game_state = Game_States.pause

        for event in pygame.event.get():  # pause sequence
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.game_state = Game_States.running

                elif event.key == pygame.K_ESCAPE:
                    quit()

    def play_message(self):
        count = 0
        done = False

        self.text_background.blit(config.text_background, (0, 0))
        self.screen.blit(self.text_background, (0, 300))
        self.game_messages[0].draw_text()
        pygame.display.flip()

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        quit()

                    elif event.key == pygame.K_SPACE:
                        count += 1

                        for t in range(len(self.game_messages)):
                            self.screen.blit(self.text_background, (0, 300))
                            self.game_messages[t].draw_text()

                            pygame.display.flip()

                            if count == len(self.game_messages):
                                self.game_state = Game_States.running
                                done = True
