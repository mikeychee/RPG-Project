import pygame
from characters import Player, Character_Controller
from game_states import Game_States
from tile import Map_Tile
from text import Text_Controller
import config


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.game_state = Game_States.none
        self.map = []
        self.camera = [0,0]

        self.main_map = pygame.Surface((config.screen_width, config.screen_height))

        self.game_map = [[Map_Tile(True) for y in range(0, config.screen_height)] for x in range(0, config.screen_width)]

        self.game_map[5][5].movement = False
        self.game_map[6][5].movement = False
        self.game_map[7][5].movement = False
        self.game_map[8][5].movement = False

        self.player = Player(self.screen, self.game_map) # initialise player

        self.tester_npc = Character_Controller("NPC1", 7, 5, self.screen, config.NPC01, self.game_map)
        self.tester_npc2 = Character_Controller("NPC2", 3, 3, self.screen, config.NPC02, self.game_map)



    def set_up(self):
        print("setting up")

        config.grass01.convert()
        config.water01.convert()
        config.NPC01.convert()

        self.objects.append(self.tester_npc)
        self.objects.append(self.tester_npc2)
        self.objects.append(self.player)

        self.game_state = Game_States.running

        self.render_map(self.game_map)
        self.screen.blit(self.main_map, (0,0))





        pygame.display.flip()  # update screen


    def update(self, clock):
        print("update")

        fps_count = Text_Controller(self.screen, "FPS: " + str(int(clock.get_fps())), (5, 5), config.black)
        fps_count.draw_text()

        self.manage_events()
        self.screen.blit(self.main_map, (0,0))
        self.render_blocked_tiles(self.game_map)

        for obj in self.objects: # draws all objects into the screen
            obj.draw(self.screen)
            fps_count.draw_text()

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
                elif event.key == pygame.K_a:
                    self.player.update_position(0, -1)
                elif event.key == pygame.K_d:
                    self.player.update_position(0, 1)
                elif event.key == pygame.K_w:
                    self.player.update_position(-1, 0)
                elif event.key == pygame.K_s:
                    self.player.update_position(1, 0)

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







