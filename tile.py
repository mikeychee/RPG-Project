import pygame
import config


class Map_Tile:
    def __init__(self, movement, blocked):
        self.movement = movement
        self.blocked = blocked


class Obstacles(pygame.sprite.Sprite):
    def __init__(self, image, x, y, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.player = player
        self.rect.x = x * config.scale
        self.rect.y = y * config.scale

        self.groupObs = pygame.sprite.Group()
        self.groupObs.add(self)
        self.check_collide()

    def check_collide(self):
        collision = pygame.sprite.groupcollide(self.player, self.groupObs, False, False)

    def draw(self, screen):
        self.groupObs.draw(screen)


class Non_Obstacle_Tiles(pygame.sprite.Sprite):
    def __init__(self, image, x, y, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.player = player
        self.rect = self.image.get_rect()
        self.rect.x = x * config.scale
        self.rect.y = y * config.scale

        self.groupNObs = pygame.sprite.Group()
        self.groupNObs.add(self)

    def draw(self, screen):
        self.groupNObs.draw(screen)



