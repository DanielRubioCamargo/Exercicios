import pygame
from pygame.locals import *
from sys import exit
from random import randint
from time import sleep

pygame.init()

def fireworks():
    initialPosX = randint(0,screenWidth)
    initialPosY = randint(0,screenHeigth)
    bombSpeed = 1
    x1 = initialPosX
    y1 = initialPosY
    cx1 = bombSpeed
    cy1 = -bombSpeed
    pygame.draw.rect(screen,(randint(0,255),randint(0,255),randint(0,255)),(x1,y1,5,5))
    x2 = initialPosX
    y2 = initialPosY
    cx2 = -bombSpeed
    cy2 = -bombSpeed
    pygame.draw.rect(screen,(randint(0,255),randint(0,255),randint(0,255)),(x2,y2,5,5))
    x3 = initialPosX
    y3 = initialPosY
    cx3 = -bombSpeed
    cy3 = bombSpeed
    pygame.draw.rect(screen,(randint(0,255),randint(0,255),randint(0,255)),(x3,y3,5,5))
    x4 = initialPosX
    y4 = initialPosY
    cx4 = bombSpeed
    cy4 = bombSpeed
    pygame.draw.rect(screen,(randint(0,255),randint(0,255),randint(0,255)),(x4,y4,5,5))
    x1 += cx1
    y1 += cy1
    x2 += cx2
    y2 += cy2
    x3 += cx3
    y3 += cy3
    x4 += cx4
    y4 += cy4

def confetti():
    for i in range(90):
        initialPosX = randint(0,screenWidth)
        initialPosY = randint(0,screenHeigth)
        bombSpeed = 1
        x1 = initialPosX
        y1 = initialPosY
        cx1 = bombSpeed
        cy1 = -bombSpeed
        pygame.draw.rect(screen,(randint(0,255),randint(0,255),randint(0,255)),(x1,y1,5,5))
        x2 = initialPosX
        y2 = initialPosY
        cx2 = -bombSpeed
        cy2 = -bombSpeed
        pygame.draw.rect(screen,(randint(0,255),randint(0,255),randint(0,255)),(x2,y2,5,5))
        x3 = initialPosX
        y3 = initialPosY
        cx3 = -bombSpeed
        cy3 = bombSpeed
        pygame.draw.rect(screen,(randint(0,255),randint(0,255),randint(0,255)),(x3,y3,5,5))
        x4 = initialPosX
        y4 = initialPosY
        cx4 = bombSpeed
        cy4 = bombSpeed
        pygame.draw.rect(screen,(randint(0,255),randint(0,255),randint(0,255)),(x4,y4,5,5))
        x1 += cx1
        y1 += cy1
        x2 += cx2
        y2 += cy2
        x3 += cx3
        y3 += cy3
        x4 += cx4
        y4 += cy4


# Win Message
winFont = pygame.font.SysFont("Arial",30,True,True)

# Win Song
pygame.mixer.music.set_volume(0.2)
winSong = pygame.mixer.Sound("Codigos em Python\\Games\\Teste\\Chaves   Tema de Abertura Original Televisa Completo.mp3")

# Images
spaceBackground = pygame.image.load("Codigos em Python\\Games\\Teste\\Space Invaders\\spaceImage.jpg")
winImage = pygame.image.load("Codigos em Python\\Games\\Teste\\Space Invaders\\Win.png")

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# Screen
screenWidth = 640
screenHeigth = 480
screen = pygame.display.set_mode((screenWidth,screenHeigth))
gameTitle = pygame.display.set_caption("Jonas Invaders")

# FPS
fps = 60
frameRate = pygame.time.Clock()
fpsFont = pygame.font.SysFont("arial",15,True,False)

# Player
playerWidth = 40
playerHeigth = 30
playerX = (screenWidth/2) - (playerWidth/2)
playerY = screenHeigth - playerHeigth - 5
playerSpeed = 10
playerColor = GREEN
playerDamage = 10
playerHP = 100

# Spell
spellWidth = 20
spellHeigth = 20
spellX = playerX + ((playerWidth - spellWidth)/2)
spellY = playerY + ((playerHeigth - spellHeigth)/2)
spellSpeed = 50
spellColor = RED
spellControlY = 0
isMoving = False

# Enemies
enemy = list()
enemyTotalPos = list()
enemyPos = list()
enemyColor = WHITE
enemiesWidth = 30
enemiesHeigth = 30
for i in range(0,5):
        enemiesY = 45*(i+1)
        for j in range(0,10):
            enemiesX = 55*(j+1)      
            enemyPos.append(enemiesX)
            enemyPos.append(enemiesY)
            enemyTotalPos.append(enemyPos[:])
            enemyPos.clear()
collidedList = list()
colCont = 0
for i,c in enumerate(enemyTotalPos):
    collidedList.append(False)
turn = list()
for i in range(len(enemyTotalPos)):
    turn.append(0)

# Main Loop
while True:
    winMessage = "You Won!"
    winText = winFont.render(winMessage,True,(randint(0,255),randint(0,255),randint(0,255)))
    frameRate.tick(fps)
    fpsMessage = f"FPS : {fps}"
    fpsText = fpsFont.render(fpsMessage,False,WHITE)
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                isMoving = True
                spellControlY = 20

    # ----UPDATE---- 

    # Spell Movement

    if spellControlY == 0:
        isMoving = False
    spellY -= spellControlY
    if isMoving == False:
        spellX  = playerX + ((playerWidth - spellWidth)/2)
    if spellY < -spellHeigth:
        spellControlY = 0
        spellX = playerX + ((playerWidth - spellWidth)/2)
        spellY = playerY + ((playerHeigth - spellHeigth)/2)
    
    # Player Movement

    if playerX + playerWidth < 0:
        playerX = screenWidth
    if playerX > screenWidth:
        playerX = -playerWidth
    if pygame.key.get_pressed()[K_d]:
        playerX += playerSpeed
    elif pygame.key.get_pressed()[K_a]:
        playerX -= playerSpeed

    # Draw

    #screen.blit(spaceBackground,(0,0))
    spell = pygame.draw.rect(screen,spellColor,(spellX,spellY,spellWidth,spellHeigth))
    for i,c in enumerate(enemyTotalPos):
        enemy = pygame.draw.rect(screen,enemyColor,(c[0],c[1],enemiesWidth,enemiesHeigth))
        if enemy.colliderect(spell):
            collidedList[i] = True
        if collidedList[i] == False:
            pass
        else:
            turn[i] += 1
            enemy = pygame.draw.rect(screen,enemyColor,(c[0],c[1],enemiesWidth,enemiesHeigth))
            screen.fill(BLACK,(c[0],c[1],enemiesWidth,enemiesHeigth))
            #screen.blit(spaceBackground,(c[0],c[1]))
            if turn[i] == 1:
                colCont += 1
                spellControlY = 0
                spellX = playerX + ((playerWidth - spellWidth)/2)
                spellY = playerY + ((playerHeigth - spellHeigth)/2)
            spell = pygame.draw.rect(screen,spellColor,(spellX,spellY,spellWidth,spellHeigth))

    if colCont == len(collidedList):
        screen.blit(winImage,((screenWidth/2)-115,(screenHeigth/2)-130))
        screen.blit(winText,((screenWidth/2)-60,(screenHeigth/2)+65))
        winSong.play()
        confetti()
        #fireworks()
        
    player = pygame.draw.rect(screen,playerColor,(playerX,playerY,playerWidth,playerHeigth))
    
    screen.blit(fpsText,(screenWidth - 70,15))  

    pygame.display.flip()
