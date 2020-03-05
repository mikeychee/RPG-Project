import pygame

# Window size
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 300
WINDOW_SURFACE = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE

DARK_BLUE = (3, 5, 54)
WHITE_ISH = (230, 230, 197)


def playMessage(window, font, message, start_point=(20, 20)):
    line_separation = 3  # pixels between lines
    line_cursor = 0

    # Make a blurred copy of the background for updating, by shrinking then
    # expanding the current content of the window, oh and darken it too
    # for better constrast
    skrinked = pygame.transform.smoothscale(window, (window.get_width() // 4, window.get_height() // 4))
    dark = pygame.Surface((skrinked.get_width(), skrinked.get_height()), flags=pygame.SRCALPHA)
    dark.fill((100, 100, 100, 0))
    skrinked.blit(dark, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
    background = pygame.transform.smoothscale(skrinked, (window.get_width(), window.get_height()))

    # cleanup messages, remove blank lines, et.al
    message_lines = []
    for line in message.split('\n'):
        line = line.strip()
        if (len(line) > 0):
            message_lines.append(line)

    # Make every text line into a bitmap
    for i, line in enumerate(message_lines):
        message_lines[i] = font.render(line, True, WHITE_ISH)

    # Start the render
    clock = pygame.time.Clock()
    done = False
    while not done:

        window.blit(background, (0, 0))
        x_pos, y_pos = start_point
        for i in range(0, line_cursor):
            text_rect = message_lines[i].get_rect()
            text_rect.x = x_pos
            text_rect.y = y_pos
            window.blit(message_lines[i], text_rect)
            # offset next line
            y_pos += text_rect.height + line_separation
        pygame.display.flip()

        # Handle user-input
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.event.post(pygame.event.Event(pygame.QUIT) )  # re-post this to handle in the main loop
                done = True
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    done = True
                elif (event.key == pygame.K_SPACE):
                    line_cursor += 1
                    if (line_cursor > len(message_lines)):
                        done = True    # space at end to dismiss

        clock.tick_busy_loop(16)  # don't need big FPS for read


### initialisation
pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), WINDOW_SURFACE)
pygame.display.set_caption("text player")

### Message Text For Displaying
poke_font = pygame.font.Font('Pokemon Solid.ttf', 24)  # ref: https://fontmeme.com/fonts/pokmon-font/
message = "You were eated all up by a Wild Wampus!\nAnd you never found the Key in the Dark Forest!\nRedo From Start."

### Background image
grassy_background = pygame.image.load("textures/grass01.png")  # ref: http://www.plaintextures.com/
grassy_background = pygame.transform.scale(grassy_background, (WINDOW_WIDTH, WINDOW_HEIGHT))

### Main Loop
clock = pygame.time.Clock()
done = False
while not done:

    # Handle user-input
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            done = True
        elif (event.type == pygame.MOUSEBUTTONUP):
            # On mouse-click
            playMessage(window, poke_font, message)

    # Movement keys
    keys = pygame.key.get_pressed()
    if ( keys[pygame.K_UP] ):
        print("up")

    # Update the window, but not more than 60fps
    window.blit(grassy_background, (0, 0))
    pygame.display.flip()

    # Clamp FPS
    clock.tick_busy_loop(60)

pygame.quit()