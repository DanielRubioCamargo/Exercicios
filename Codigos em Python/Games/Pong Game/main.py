import pygame
from pygame.locals import *
from sys import exit
from random import randint, choice

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGTH = 480
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
gameTitle = pygame.display.set_caption("Pong Game")

FPS = 30
frameRate = pygame.time.Clock()

ballX = SCREEN_WIDTH/2
ballY = SCREEN_HEIGTH/2
ballColor = (255,255,255)
ballSpeed = 10
ballXconstant = ballSpeed
ballYconstant = 5
ballWidth = 30
ballHeigth = 30

playerWidth = 20
playerHeigth = 100
playerX = SCREEN_WIDTH - playerWidth
playerY = SCREEN_HEIGTH/2
playerColor = (0,255,0)
playerSpeed = 10

player2Width = 20
player2Heigth = 100
player2X = 0
player2Y = SCREEN_HEIGTH/2
player2Color = (255,0,0)
player2Speed = 5


while True:
    frameRate.tick(FPS)
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if ballY > player2Y:
        player2Y += player2Speed
    elif ballY < player2Y:
        player2Y -= player2Speed

    if pygame.key.get_pressed()[K_w]:
        playerY -= playerSpeed
    elif pygame.key.get_pressed()[K_s]:
        playerY += playerSpeed

    if ballX + ballWidth > SCREEN_WIDTH - 5 or ballX < 5:
        break
    if ballY + ballHeigth > SCREEN_HEIGTH or ballY < 0:
        ballYconstant *= -1

    ballX += ballXconstant
    ballY += ballYconstant

    player = pygame.draw.rect(screen,playerColor,(playerX,playerY,playerWidth,playerHeigth))
    player2 = pygame.draw.rect(screen,player2Color,(player2X,player2Y,player2Width,player2Heigth))
    ball = pygame.draw.rect(screen,ballColor,(ballX,ballY,ballWidth,ballHeigth))

    yList = [1,-1]

    if player.colliderect(ball) or player2.colliderect(ball):
        ballXconstant *= -1
        ballYconstant *= choice(yList)

    pygame.display.flip()