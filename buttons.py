import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, screen, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.group = pygame.sprite.Group()
        self.group.add(self)

    def draw(self):
        self.group.draw(self.screen)


