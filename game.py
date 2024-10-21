import pygame
pygame.init()

#main game
screen = pygame.display.set_mode((500,600))

#title & icon
pygame.display.set_caption("Space War")

icon = pygame.image.load('./files/icon.png')
pygame.display.set_icon(icon)
#player
playerImg = pygame.image.load('./files/player.png')
playerX = 225
playerY = 450

def player():
    screen.blit(playerImg,(playerX,playerY))

#frames
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((102,178,255))
    player()
    pygame.display.update()
