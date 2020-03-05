class Text_Controller:
    def __init__(self, screen, display_text, font, position, color, back_color=None):
        self.screen = screen
        self.display_text = display_text
        self.position = position
        self.color = color
        self.back_color = back_color

        self.text_surface, self.text_rect = self.set_text(font)
        self.text_rect.topleft = position

    def set_text(self, font):
        if self.back_color:
            text_surface = font.render(self.display_text, False, self.color, self.back_color)
        else:
            text_surface = font.render(self.display_text, False, self.color)
        return text_surface, text_surface.get_rect()

    @staticmethod
    def text_font(font):
        font_obj = font.render("-", False, (0, 0, 0))
        font_rect = font_obj.get_rect()

        return font_rect

    def set_game_message(self, game_message_list):
        game_message_list.append((self.set_text, self.color))

    def draw_text(self):
        self.screen.blit(self.text_surface, self.text_rect)
