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
playerX_change = 0
def player(x,y):
    screen.blit(playerImg,(x,y))

#frames
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.type == pygame.K_LEFT:
                playerX_change = 0
    
    screen.fill((102,178,255))
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 436:
        playerX = 436

    player(playerX,playerY)
    pygame.display.update()
