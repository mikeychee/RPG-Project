import pygame


class Scene:
    def __init__(self, screen):
        self.screen = screen
        self.background_image = None

    def set_background(self, image, screen):
        self.background_image = image
        screen.blit(self.background_image, (0, 0))
