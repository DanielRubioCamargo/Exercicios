import pygame as pg
from pygame.locals import *
from sys import exit

pg.init()

width = 640
heigth = 480

screen = pg.display.set_mode((width,heigth))
gameName = pg.display.set_caption("Game")

pg.draw.rect(screen,(255,0,0),(50,400,60,60))
pg.draw.circle(screen,(0,0,255),(width/2,heigth/2),50)
pg.draw.line(screen,(255,255,50),(0,0),(300,20),3)

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            exit()
    pg.display.update()