import pygame
import random
pygame.init()

#wallpaper
wallpaper = pygame.image.load('./files/background-wallpaper.jpg')
#main game
screen = pygame.display.set_mode((600,957))

#title & icon
pygame.display.set_caption("Space War")

icon = pygame.image.load('./files/icon.png')
pygame.display.set_icon(icon)
#player
playerImg = pygame.image.load('./files/player.png')
playerX = 268
playerY = 720
playerX_change = 0


#enemy
enemyType = random.randint(1,4)
if enemyType == 1:
    enemyImg = pygame.image.load('./files/enemy1.png')
elif enemyType == 2:
    enemyImg = pygame.image.load('./files/enemy2.png')
elif enemyType == 3:
    enemyImg = pygame.image.load('./files/enemy3.png')
elif enemyType == 4:
    enemyImg = pygame.image.load('./files/enemy4.png')
enemyX = random.randint(100, 400)
enemyY = random.randint(50,150)
enemyX_change = 0.1
enemyY_change = 11

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    screen.blit(enemyImg,(x,y))

#frames
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.type == pygame.K_LEFT:
                playerX_change = 0
    
    screen.fill((102,178,255))
    screen.blit(wallpaper,(0,0))

    #player movement
    playerX += playerX_change
    if playerX <= 0 :
        playerX = 0
    elif playerX >= 536 :
        playerX = 536

    #enemy movement
    enemyX += enemyX_change
    if enemyX <= 0 :
        enemyX_change = 0.2
        enemyY += enemyY_change
    elif enemyX >= 536 :
        enemyX_change = -0.2
        enemyY += enemyY_change

    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()
