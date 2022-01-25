import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

screenWidth = 640
screenHeigth = 480

groundWidth = screenWidth
groundHeigth = 50
groundX = 0
groundY = screenHeigth - groundHeigth

playerWidth = 50
playerHeigth = 50
playerX = screenWidth/2
playerY = screenHeigth - playerHeigth - groundHeigth
playerSpeed = 10

deaths = 0
font = pygame.font.SysFont("arial",25,True,False)

pygame.mixer.music.set_volume(0.25)
backgroundSong = pygame.mixer.music.load("Codigos em Python\\Games\\Teste\\Chaves   Tema de Abertura Original Televisa Completo.mp3")
pygame.mixer.music.play(-1)
deathSound = pygame.mixer.Sound("Codigos em Python\\Games\\Teste\\y2meta.com - cavalo (128 kbps).mp3")

screen = pygame.display.set_mode((screenWidth,screenHeigth))
gameName = pygame.display.set_caption("Game")

ground = pygame.draw.rect(screen,(0,255,0),(groundX,groundY,groundWidth,groundHeigth))

frameRate = pygame.time.Clock()

ballRadius = 50
ballX = randint(0,screenWidth-ballRadius)
ballY = 0
ballSpeed = 20


while True:
    deathMessage = "You died {} time(s)!".format(deaths)
    deathText = font.render(deathMessage,True,(245,255,50))
    frameRate.tick(30)
    screen.fill((0,0,100),(0,0,screenWidth,screenHeigth-groundHeigth))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    ballY += ballSpeed
    ball = pygame.draw.circle(screen,(255,0,0),(ballX,ballY),ballRadius)
    player = pygame.draw.rect(screen,(0,0,255),(playerX,playerY,playerWidth,playerHeigth))
    
    if pygame.key.get_pressed()[K_d]:
        playerX += playerSpeed
    if pygame.key.get_pressed()[K_a]:
        playerX -= playerSpeed
    if playerX > screenWidth:
        playerX = 0
    if playerX < 0:
        playerX = screenWidth-playerWidth
    
    if ballY >= screenHeigth - groundHeigth - ballRadius:
        ballY = 0
        ballX = randint(0,screenWidth-ballRadius)

    if player.colliderect(ball):
        deathSound.play()
        ballY = 0
        ballX = randint(0,screenWidth-ballRadius)
        deaths += 1
        playerX = screenWidth/2

    screen.blit(deathText,(300,30))
    pygame.display.update()
            