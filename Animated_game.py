import pygame

# Intialize pygame
pygame.init()

# Setup screen
(width, height) = (1000, 1000)
screen = pygame.display.set_mode((width, height))
bg = pygame.transform.scale(pygame.image.load("mapEurope.jpg"),(width, height))

# Title and icon
pygame.display.set_caption("Flight game")
icon = pygame.image.load("travel.png")
pygame.display.set_icon(icon)

# Airplane
airplaneImg = pygame.transform.scale(pygame.image.load("airplane.png"),(80,80))

# Hide mouse cursor
pygame.mouse.set_visible(False)

# Set clock
clock = pygame.time.Clock()

# Game loop
run = True
while run:
    # Add clock
    clock.tick(60)
    # Set background
    screen.blit(bg, (0,0))
    # Get mouse position
    pos = pygame.mouse.get_pos()

    # Draw new cursor
    screen.blit(airplaneImg, pos)

    # Check screen close or not
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()