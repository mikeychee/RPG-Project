import pygame
import config
import time


class Player(pygame.sprite.Sprite):
    def __init__(self, screen, game_map):
        super().__init__()
        print('player created')
        self.screen = screen
        self.game_map = game_map

        self.image = config.player01
        self.rect = self.image.get_rect()
        self.rect.x = 1
        self.rect.y = 1

        self.group = pygame.sprite.Group()
        self.group.add(self)

    def update_position(self, dy, dx):
        if self.game_map[int(self.rect.x/config.scale)+ dx][int(self.rect.y/config.scale)+dy].movement:

            self.rect.x = (self.rect.x + dx * config.scale)
            self.rect.y = (self.rect.y + dy * config.scale)

    def draw(self, screen):
        self.group.draw(screen)

    def remove_sprite(self):
        self.group.remove()


class Character_Controller(pygame.sprite.Sprite):
    def __init__(self, obj_name, x, y, screen, image, game_map):
        pygame.sprite.Sprite.__init__(self)

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

    def remove_sprite(self):
        self.remove()

    def draw(self, screen):

        self.group.draw(screen)

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
            self.rect.x = (self.rect.x + self.dx1) # moves the character to the right
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
            self.rect.x = (self.rect.x + self.dx2) # moves the character down
            self.rect.y = (self.rect.y + self.dy2)
            self.movement_counter = self.movement_counter + 1 # adds one to the movement checker

        elif self.dy2 == config.scale:
            self.dy2 = -config.scale
            # if the movement counter reaches, to set the direction in the opposite to make him move up

        else:
            self.dy2 = config.scale



