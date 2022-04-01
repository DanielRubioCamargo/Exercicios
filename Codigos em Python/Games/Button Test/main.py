import pygame
from pygame.locals import *
from sys import exit

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGTH = 480
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
gameTitle = pygame.display.set_caption("Button Class")

clock = pygame.time.Clock()
FPS = 30

timesClicked = 0
currentTime = 0
clickedTime = 0

GREEN = (0,255,0)
RED = (255,0,0)

hasClicked = False
color = RED

while True:
    clock.tick(FPS)
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    currentTime =  pygame.time.get_ticks()
    print(currentTime)

    mousePos = pygame.mouse.get_pos()
    button = pygame.draw.rect(screen,color,(100,200,200,50))

    if button.collidepoint(mousePos):
        if pygame.mouse.get_pressed()[0] and hasClicked == False:
            if timesClicked > 0 and currentTime - clickedTime < 4000:
                pass
            else:
                clickedTime = pygame.time.get_ticks()
                color = GREEN
                print("Clicou")
                hasClicked = True
                timesClicked += 1
        
    if pygame.mouse.get_pressed()[0] == False:
        color = RED
        hasClicked = False

    pygame.display.flip()