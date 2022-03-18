from calendar import isleap
from tkinter import Button
import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640,480))

xPos = 300
yPos = 300
xOffset = 0
yOffset = 0
isScrollingUp = False
isScrollingDown = False

while True:

    screen.fill((0,0,0))

    mx,my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 4:
                isScrollingUp = True
            if event.button == 5:
                isScrollingDown = True
        if event.type == MOUSEBUTTONUP:
            if event.button == 4:
                isScrollingUp = False
            if event.button == 5:
                isScrollingDown = False

        if isScrollingUp:
            yOffset-=10
        if isScrollingDown:
            yOffset+=10

    image = pygame.draw.rect(screen,(255,255,255),(xPos+xOffset,yPos+yOffset,50,50))
    pygame.display.flip()