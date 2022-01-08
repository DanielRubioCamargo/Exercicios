import pygame
from pygame.locals import *
from sys import exit

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGTH = 480

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
gameName = pygame.display.set_caption("Game")

pygame.draw.rect(screen,(255,255,255),(200,300,30,40))
pygame.draw.circle(screen,(255,0,0),(50,50),40)
pygame.draw.line(screen,(255,255,0),(30,30),(300,300),5)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
