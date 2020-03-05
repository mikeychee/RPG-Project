import pygame

pygame.init()
black = [0, 0, 0]
white = [255, 255, 255]

scale = 40

fps = 16
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

# TODO: NPC animations
text_background = pygame.transform.scale(text_background, (screen_width, 180))

playerIDLE = pygame.image.load("textures/player/playerIDLE.png")
playerIDLE = pygame.transform.scale(playerIDLE, (scale, scale))

playerL1 = pygame.image.load("textures/player/playerL1.png")
playerL2 = pygame.image.load("textures/player/playerL2.png")

playerR1 = pygame.image.load("textures/player/playerR1.png")
playerR2 = pygame.image.load("textures/player/playerR2.png")

playerF1 = pygame.image.load("textures/player/playerF1.png")
playerF2 = pygame.image.load("textures/player/playerF2.png")

playerB1 = pygame.image.load("textures/player/playerB1.png")
playerB2 = pygame.image.load("textures/player/playerB2.png")

playerL1 = pygame.transform.scale(playerL1, (scale, scale))
playerL2 = pygame.transform.scale(playerL2, (scale, scale))

playerR1 = pygame.transform.scale(playerR1, (scale, scale))
playerR2 = pygame.transform.scale(playerR2, (scale, scale))

playerF1 = pygame.transform.scale(playerF1, (scale, scale))
playerF2 = pygame.transform.scale(playerF2, (scale, scale))

playerB1 = pygame.transform.scale(playerB1, (scale, scale))
playerB2 = pygame.transform.scale(playerB2, (scale, scale))

playerLEFT = [playerL1, playerL2]
playerRIGHT = [playerR1, playerR2]
playerFRONT = [playerF1, playerF2]
playerBACK = [playerB1, playerB2]