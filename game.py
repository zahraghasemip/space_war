import pygame
pygame.init()

#main game
screen = pygame.display.set_mode((800,400))

#title & icon
pygame.display.set_caption("Space War")

#frames
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('q')
            running = False
