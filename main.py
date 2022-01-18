# importing important modules
import pygame
from sys import exit

# initialising pygame
pygame.init()

# creating the game window and setting up the title and icon
WIDTH = 720
HEIGHT = 1280
TITLE = "My Game"
GAME_ICON = pygame.image.load("assests/icons/game_icon.png") # icon image should always be 32x32 else less than ir
# pygame.display.set_mode((WIDTH, HEIGHT), full-screen, depth)
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption(TITLE)
pygame.display.set_icon(GAME_ICON)

# creating the clock
clock = pygame.time.Clock()

# defining the colors
#      Red   Green  Blue
WHITE = (255, 255, 255)

# game loop
run = True
while run :
    # setting the bg
    screen.fill(WHITE)
    
    # getting user events
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            exit()
    
    # updating the game window and setting the FPS to 60
    pygame.display.update()
    clock.tick(60)
