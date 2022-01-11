import pygame as pg
from pygame.locals import *
from sys import exit
from random import randint

pg.init()

width = 640
heigth = 480
xRed = width/2
yRed = heigth/2
xBlue = 300
yBlue = 200

points = 0
font = pg.font.SysFont("arial",40,True,True)
screen = pg.display.set_mode((width,heigth))
gameName = pg.display.set_caption("Game")
clock = pg.time.Clock()

while True:
    clock.tick(30)
    screen.fill((0,0,0))
    message = "Pontos : {}".format(points)
    text = font.render(message,True,(255,255,255))
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            exit()
            '''
        if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20
                '''
               
    redRect = pg.draw.rect(screen,(255,0,0),(xRed,yRed,60,60))
    blueRect = pg.draw.rect(screen,(0,0,255),(xBlue,yBlue,60,60))
    
    if pg.key.get_pressed()[K_a]:
        xRed = xRed - 20
    if pg.key.get_pressed()[K_d]:
        xRed = xRed + 20
    if pg.key.get_pressed()[K_w]:
        yRed = yRed - 20
    if pg.key.get_pressed()[K_s]:
        yRed = yRed + 20

    if xRed > width:
        xRed = 0
    if xRed < 0:
        xRed = width-60
    if yRed > heigth:
        yRed = 0
    if yRed < 0:
        yRed = heigth-60
    

    if redRect.colliderect(blueRect):
        xBlue = randint(0,590)
        yBlue = randint(0,430)
        points+=1

    screen.blit(text,(400,50))

    pg.display.update()
    

