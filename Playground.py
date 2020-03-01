import pygame
import config


class Sprites(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = config.player01
        self.group = pygame.sprite.Group()

    def remove_sprite(self):
        self.remove()


class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        print('player created')
        self.screen = screen

        self.image = config.player01
        self.rect = self.image.get_rect()
        self.rect.x = 1
        self.rect.y = 1

        self.group = pygame.sprite.Group()
        self.group.add(self)

    def update_position(self, dy, dx):
        if self.screen[int(self.rect.x/config.scale)][int(self.rect.y/config.scale)].movement:

            self.rect.x = (self.rect.x + dx * config.scale)
            self.rect.y = (self.rect.y + dy * config.scale)

    def draw(self, screen):
        self.group.draw(screen)

    def remove_sprite(self):
        self.group.remove()


class Character_Controller:
    def __init__(self, obj_name, x, y, screen, image, character=None):
        self.obj_name = obj_name
        self.y = y
        self.x = x
        self.screen = screen
        self.image = image

        if character:
            self.character = character
            character.owner = self

    def draw(self, screen):
        screen.blit(self.image, (self.x * config.scale, self.y * config.scale))

# Components


class NPC:
    def __init__(self, instance_name):
        self.instance_name = instance_name

# TODO: More components