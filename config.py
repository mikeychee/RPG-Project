import pygame

pygame.init()
black = [0, 0, 0]
white = [255, 255, 255]

scale = 40

fps = 60
clock = pygame.time.Clock()

screen_height = 480
screen_width = 640

fps_Counter = pygame.font.Font("fonts/proxima_nova.ttf", 20)
game_messages = pygame.font.Font("fonts/Connection.otf", 30)

grass01 = pygame.image.load("textures/grass01.png")
water01 = pygame.image.load("textures/water02.png")
tree01 = pygame.image.load("textures/tree01.png")
NPC01 = pygame.image.load("textures/NPC01.png")
NPC02 = pygame.image.load("textures/NPC02.png")
text_background = pygame.image.load("textures/Text Background.png")

grass01 = pygame.transform.scale(grass01, (scale, scale))
water01 = pygame.transform.scale(water01, (scale, scale))
tree01 = pygame.transform.scale(tree01, (scale, scale))
NPC01 = pygame.transform.scale(NPC01, (scale, scale))
NPC02 = pygame.transform.scale(NPC02, (scale, scale))
text_background = pygame.transform.scale(text_background, (screen_width, 180))

player01 = pygame.image.load("textures/player01.png")
player01 = pygame.transform.scale(player01, (scale, scale))
