from pickle import TRUE
import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

def set_snake_size(lst:list):
    for i in lst:
        pygame.draw.rect(screen,playerColor,(i[0],i[1],playerWidth,playerHeigth))

# colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)

# screen
SCREEN_WIDTH = 640
SCREEN_HEIGTH = 480
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
gameTitle = pygame.display.set_caption("Snake Game 2")

# fps
frameRate = pygame.time.Clock()
FPS = 30

# player
playerX = SCREEN_WIDTH/2
playerY = SCREEN_HEIGTH/2
playerSpeed = 10
playerXconstant = playerSpeed
playerYconstant = 0
playerColor = GREEN
playerWidth = 10
playerHeigth = 10
playerLength = 5
isPlayerDead = False
playerHeadList = list()

# apple
appleX = randint(20,620)
appleY = randint(20,440)
appleColor = RED
appleWidth = 10
appleHeigth = 10

# main loop
while True:
    frameRate.tick(FPS)
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_d and playerXconstant == 0:
                playerYconstant = 0
                playerXconstant = playerSpeed 
            elif event.key == K_a and playerXconstant == 0:
                playerYconstant = 0
                playerXconstant = -playerSpeed   
            elif event.key == K_w and playerYconstant == 0:
                playerYconstant = -playerSpeed
                playerXconstant = 0  
            elif event.key == K_s and playerYconstant == 0:
                playerYconstant = playerSpeed
                playerXconstant = 0
    
    playerX += playerXconstant
    playerY += playerYconstant

    curHeadList = list()
    curHeadList.append(playerX)
    curHeadList.append(playerY)
    playerHeadList.append(curHeadList)

    if len(playerHeadList) > playerLength:
        playerHeadList.pop(0)

    if playerHeadList.count(curHeadList) > 1:
        isPlayerDead = True

    if isPlayerDead == True:
        break

    set_snake_size(playerHeadList)

    player = pygame.draw.rect(screen,playerColor,(playerX,playerY,playerWidth,playerHeigth))
    apple = pygame.draw.rect(screen,appleColor,(appleX,appleY,appleWidth,appleHeigth))

    if player.colliderect(apple):
        appleX = randint(20,620)
        appleY = randint(20,440)    
        playerLength += 1
        
    pygame.display.flip()