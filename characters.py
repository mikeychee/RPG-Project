import pygame
import config
from text import Text_Controller
from game_states import Game_States


class Player(pygame.sprite.Sprite):
    def __init__(self, screen, game_map):
        pygame.sprite.Sprite.__init__(self)
        print('player created')
        self.screen = screen
        self.game_map = game_map

        self.image = config.playerIDLE
        self.imageLEFT = config.playerLEFT
        self.imageRIGHT = config.playerRIGHT
        self.imageUP = config.playerBACK
        self.imageDOWN = config.playerFRONT

        self.left = False
        self.right = False
        self.front = False
        self.back = False
        self.walk_count = 0

        self.rect = self.image.get_rect()
        self.rect.x = 5 * config.scale
        self.rect.y = 1 * config.scale

        self.group = pygame.sprite.Group()
        self.group.add(self)

    def update_position(self, dy, dx):

        if self.game_map[int(self.rect.x/config.scale) + dx][int(self.rect.y/config.scale)+dy].movement:
            if not self.game_map[int(self.rect.x/config.scale) + dx][int(self.rect.y/config.scale)+dy].blocked:

                self.rect.x = (self.rect.x + dx * config.scale)
                self.rect.y = (self.rect.y + dy * config.scale)

    def check_collision(self, obstacle):
        collision = pygame.sprite.groupcollide(self.group, obstacle, False, False, collided=None)
        if collision:
            print("player collide")

    def draw(self, screen):
        self.play_animation()

    def remove_sprite(self):
        self.group.remove()

    def play_animation(self):
        if self.walk_count + 1 >= config.fps:
            self.walk_count = 0

        if self.left:
            self.screen.blit(self.imageLEFT[self.walk_count//8], self.rect)
            self.walk_count += 1

        elif self.right:
            self.screen.blit(self.imageRIGHT[self.walk_count//8], self.rect)
            self.walk_count += 1

        elif self.front:
            self.screen.blit(self.imageDOWN[self.walk_count//8], self.rect)
            self.walk_count += 1

        elif self.back:
            self.screen.blit(self.imageUP[self.walk_count//8], self.rect)
            self.walk_count += 1

        else:
            self.screen.blit(self.image, self.rect)


class CharacterController(pygame.sprite.Sprite):
    def __init__(self, obj_name, x, y, screen, image, game_map):
        pygame.sprite.Sprite.__init__(self)

        # TODO: figure out how to make characters not ghosts

        self.obj_name = obj_name
        self.image = image
        self.screen = screen
        self.game_map = game_map

        self.rect = self.image.get_rect()

        self.x = x
        self.y = y
        self.rect.x = x * config.scale
        self.rect.y = y * config.scale

        self.group = pygame.sprite.Group()
        self.group.add(self)

        self.movement_counter = 0

        # properties for ai01
        self.dx1 = config.scale
        self.dy1 = 0

        # properties for ai02
        self.dx2 = 0
        self.dy2 = config.scale

        self.message_list = []

    def remove_sprite(self):
        self.remove()

    def draw(self, screen):

        self.group.draw(screen)

    def check_collision(self, obstacle, game):
        # TODO: figure out how to make the characters unable to pass through each other
        # TODO: character interaction
        collision = pygame.sprite.collide_rect(self, obstacle)
        if collision == 1:
            print("character collide")
            game.game_state = Game_States.play_message
            game.play_message()

    def text_to_speak(self, surface, message, font, position, color, bg_color=None):

        message = Text_Controller(surface, message, font, position, color, back_color=bg_color)
        self.message_list.append(message)

        return message

    def ai_left_right(self):

        # basic ai in moving the character left and right by the scale
        if self.movement_counter >= 5 and self.dx1 == -config.scale:
            self.dx1 = -config.scale
            self.rect.x = (self.rect.x + self.dx1)
            self.rect.y = (self.rect.y + self.dy1)
            self.movement_counter = self.movement_counter + 1
            if self.movement_counter == 10:
                self.movement_counter = 0

        elif self.movement_counter < 5 and self.dx1 == config.scale:
            # ai starts here!
            self.rect.x = (self.rect.x + self.dx1)  # moves the character to the right
            self.rect.y = (self.rect.y + self.dy1)
            self.movement_counter = self.movement_counter + 1  # adds one to the movement checker

        elif self.dx1 == config.scale:
            self.dx1 = -config.scale
            # if the movement counter reaches, to set the direction in the opposite to make him move left

        else:
            self.dx1 = config.scale

    def ai_up_down(self):

        # basic ai in moving the character up and down by the scale
        if self.movement_counter >= 5 and self.dy2 == -config.scale:
            self.dy2 = -config.scale
            self.rect.x = (self.rect.x + self.dx2)
            self.rect.y = (self.rect.y + self.dy2)
            self.movement_counter = self.movement_counter + 1
            if self.movement_counter == 10:
                self.movement_counter = 0

        elif self.movement_counter < 5 and self.dy2 == config.scale:
            # ai starts here!
            self.rect.x = (self.rect.x + self.dx2)  # moves the character down
            self.rect.y = (self.rect.y + self.dy2)
            self.movement_counter = self.movement_counter + 1  # adds one to the movement checker

        elif self.dy2 == config.scale:
            self.dy2 = -config.scale
            # if the movement counter reaches, to set the direction in the opposite to make him move up

        else:
            self.dy2 = config.scale

        # TODO: Create more ais
