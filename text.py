import config
import pygame


class Text_Controller:
    def __init__(self, screen, display_text, position, color):
        self.screen = screen
        self.display_text = display_text
        self.position = position
        self.color = color

        self.text_surface, self.text_rect = self.set_text()
        self.text_rect.topleft = position

    def set_text(self):
        text_surface = config.proxima_nova.render(self.display_text, False, self.color)

        return text_surface, text_surface.get_rect()

    def draw_text(self):
        self.screen.blit(self.text_surface, self.text_rect)





