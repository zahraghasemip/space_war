import pygame
import random
import math
from pygame import mixer
pygame.init()

#wallpaper
wallpaper = pygame.image.load('./files/background-wallpaper.jpg')

#background music
mixer.music.load('./files/background.mp3')
mixer.music.play(-1)

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
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 5
for i in range(num_of_enemies):
    enemyType = random.randint(1,4)
    if enemyType == 1:
        enemyImg.append(pygame.image.load('./files/enemy1.png'))
    elif enemyType == 2:
        enemyImg.append(pygame.image.load('./files/enemy2.png'))
    elif enemyType == 3:
        enemyImg.append(pygame.image.load('./files/enemy3.png'))
    elif enemyType == 4:
        enemyImg.append(pygame.image.load('./files/enemy4.png'))
    enemyX.append(random.randint(100, 400))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.5)
    enemyY_change.append(10)

#bullet
bulletImg = pygame.image.load('./files/bullet.png')
bulletX = 0
bulletY = 720
bulletX_change = 0.1
bulletY_change = 1
bullet_state = "ready"
score = 0

#display score
score_value = 0
font = pygame.font.Font('./files/Vazirmatn-Black.ttf', 40)
scoreTextX = 10
scoreTextY = 700

def show_score(x,y):
    score = font.render("score " + str(score_value),True , (255,255,255))
    screen.blit(score , (x,y))

def fire_bullet(x,y):
    screen.blit(bulletImg,(x+10,y+20))

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def isCollision(x1,y1,x2,y2):
    distance = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
    if distance < 30:
        return True
    else:
        return False
#frames
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.9
            if event.key == pygame.K_LEFT:
                playerX_change = -0.9
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready' :
                    bulletX = playerX
                    bullet_state = "fire"
                    fire_bullet(bulletX,bulletY)
                    fire_sound = mixer.Sound('./files/laser.wav')
                    fire_sound.play()

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
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 :
            enemyX_change[i] = 0.1
            enemyY[i] += enemyY_change[i] 
        elif enemyX[i] >= 536 :
            enemyX_change[i] = -0.1
            enemyY[i] += enemyY_change[i]
        #bullet collision
        collision = isCollision(enemyX[i], enemyY[i] , bulletX , bulletY)
        if collision:
            bullet_state = 'ready'
            bulletY = 720
            score_value += 1
            enemyX[i] = random.randint(100, 400)
            enemyY[i] = random.randint(50,150)
            collision_sound = mixer.Sound('./files/explosion.wav')
            collision_sound.play()

        enemy(enemyX[i],enemyY[i],i)
        

    #bullet movement
    if bullet_state is "fire":
        if bulletY <= 0:
            bullet_state = "ready"
            bulletY = 720
            
        fire_bullet(bulletX , bulletY)
        bulletY -= bulletY_change

       

    player(playerX,playerY)
    show_score(scoreTextX,scoreTextY)
    pygame.display.update()
