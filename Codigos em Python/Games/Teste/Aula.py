from turtle import speed
import pygame as pg
from pygame.locals import *
from sys import exit
from random import randint

def draw_snake(lst : list):
    for pos in lst:
        pg.draw.rect(screen,(0,255,0),(pos[0],pos[1],20,20))

pg.init()

width = 640
heigth = 480
xSnake = width/2
ySnake = heigth/2
xApple = 300
yApple = 200
snakeSpeed = 5
xControl = snakeSpeed
yControl = 0
snakeLength = 0

pg.mixer.music.set_volume(0.0)
backgroundSong = pg.mixer.music.load("Codigos em Python\\Games\\Teste\\Chaves   Tema de Abertura Original Televisa Completo.mp3")
pg.mixer.music.play(-1)
#collisionSound = pg.mixer.Sound("Codigos em Python\\Games\\Teste\\y2meta.com - cavalo (128 kbps).mp3")

points = 0
font = pg.font.SysFont("arial",40,True,True)
screen = pg.display.set_mode((width,heigth))
gameName = pg.display.set_caption("Game")
clock = pg.time.Clock()

snakeList = list()

while True:
    clock.tick(30)
    screen.fill((0,0,0))
    message = "Pontos : {}".format(points)
    text = font.render(message,True,(255,255,255))
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                if xControl != snakeSpeed:
                    xControl = -snakeSpeed
                    yControl = 0
            elif event.key == K_d:
                if xControl != -snakeSpeed:
                    xControl = snakeSpeed
                    yControl = 0
            elif event.key == K_w:
                if yControl != snakeSpeed:
                    yControl = -snakeSpeed
                    xControl = 0
            elif event.key == K_s:
                if yControl != -snakeSpeed:
                    yControl = snakeSpeed
                    xControl = 0
            
    xSnake = xSnake + xControl
    ySnake = ySnake + yControl

    if len(snakeList) > snakeLength:
        snakeList.pop(0)
               
    snake = pg.draw.rect(screen,(0,255,0),(xSnake,ySnake,20,20))
    apple = pg.draw.rect(screen,(255,0,0),(xApple,yApple,20,20))

    headList = list()
    headList.append(xSnake)
    headList.append(ySnake)
    snakeList.append(headList)

    draw_snake(snakeList)

    if snake.colliderect(apple):
        xApple = randint(0,590)
        yApple = randint(0,430)
        points+=1
        #collisionSound.play()
        snakeLength += 1
        snakeSpeed += 1

    screen.blit(text,(400,50))

    pg.display.update()
    

