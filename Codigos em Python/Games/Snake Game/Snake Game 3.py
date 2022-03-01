import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

def draw_body(lst:list):
    global playerWidth,playerHeigth
    for i in lst:
        square = pygame.draw.rect(screen,(0,255,0),(i[0],i[1],playerWidth,playerHeigth))

SCREEN_WIDTH = 640
SCREEN_HEIGTH = 480
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
gameTitle = pygame.display.set_caption("Snake Game 3")

playerX = 300
playerY = 250
playerWidth = 10
playerHeigth = 10
playerColor = (0,255,0)
playerSpeed = 0.2
playerXconstant = playerSpeed
playerYconstant = 0
playerLength = 5


appleX = randint(20,600)
appleY = randint(20,400)
appleWidth = 10
appleHeigth = 10
appleColor = (255,0,0)

playerList = list()

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_d and playerXconstant == 0:
                playerXconstant = playerSpeed
                playerYconstant = 0
            elif event.key == K_a and playerXconstant == 0:
                playerXconstant = -playerSpeed
                playerYconstant = 0
            elif event.key == K_w and playerYconstant == 0:
                playerXconstant = 0
                playerYconstant = -playerSpeed
            elif event.key == K_s and playerYconstant == 0:
                playerXconstant = 0
                playerYconstant = playerSpeed            

    playerX += playerXconstant
    playerY += playerYconstant

    headList = list()
    headList.append(playerX)
    headList.append(playerY)
    playerList.append(headList)

    if playerList.count(headList) > 1:
        break

    if len(playerList) > playerLength:
        playerList.pop(0)

    draw_body(playerList)

    player = pygame.draw.rect(screen,playerColor,(playerX,playerY,playerWidth,playerHeigth))
    apple = pygame.draw.rect(screen,appleColor,(appleX,appleY,appleWidth,appleHeigth))

    if player.colliderect(apple):
        playerLength += 15
        appleX = randint(20,600)
        appleY = randint(20,400)

    pygame.display.flip()